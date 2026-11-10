"""Interfaz web del generador de reportes de empleados."""
import csv
import io
from collections import Counter
from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(page_title='Employee Report Automation', page_icon='📊', layout='wide')
st.title('📊 Employee Report Automation')
st.caption('Analiza empleados, compara salarios y descarga reportes. Datos de ejemplo ficticios.')

archivo = st.file_uploader('Sube un archivo CSV con columnas nombre, cargo, salario', type=['csv'])
if archivo is None:
    st.info('Puedes probar la aplicación con los datos de ejemplo incluidos.')
    origen = 'data/empleados.csv'
else:
    origen = archivo

try:
    df = pd.read_csv(origen, encoding='utf-8-sig', dtype={'nombre': 'string', 'cargo': 'string'})
    df.columns = df.columns.str.strip()
    requeridas = {'nombre', 'cargo', 'salario'}
    if not requeridas.issubset(df.columns):
        raise ValueError('El CSV debe tener las columnas: nombre, cargo, salario.')
    df = df[['nombre', 'cargo', 'salario']].copy()
    if df.empty:
        raise ValueError('El CSV está vacío.')
    for columna in ['nombre', 'cargo']:
        df[columna] = df[columna].astype('string').str.strip()
        if df[columna].isna().any() or df[columna].eq('').any():
            raise ValueError(f'La columna {columna} tiene valores vacíos.')
    salarios = pd.to_numeric(df['salario'], errors='coerce')
    if salarios.isna().any() or (salarios < 0).any() or (salarios % 1 != 0).any():
        raise ValueError('Todos los salarios deben ser números enteros no negativos, sin separadores de miles.')
    df['salario'] = salarios.astype('int64')
except (ValueError, UnicodeError, pd.errors.ParserError, OSError) as error:
    st.error(f'No se pudo procesar el archivo: {error}')
    st.stop()

formato = lambda numero: f'${numero:,.0f}'
mayor = df.loc[df['salario'].idxmax()]
menor = df.loc[df['salario'].idxmin()]

c1, c2, c3, c4 = st.columns(4)
c1.metric('Empleados', len(df))
c2.metric('Salario promedio', formato(df['salario'].mean()))
c3.metric('Salario máximo', formato(mayor['salario']))
c4.metric('Salario mínimo', formato(menor['salario']))

st.subheader('Explorar empleados')
cargos = sorted(df['cargo'].unique().tolist())
seleccion = st.multiselect('Filtrar por cargo', cargos, default=cargos)
filtrados = df[df['cargo'].isin(seleccion)]
st.dataframe(filtrados, use_container_width=True, hide_index=True)

izq, der = st.columns(2)
with izq:
    st.subheader('Empleados por cargo')
    st.bar_chart(df['cargo'].value_counts())
with der:
    st.subheader('Salario promedio por cargo')
    st.bar_chart(df.groupby('cargo')['salario'].mean())

lineas = [
    'REPORTE DE EMPLEADOS',
    f'Generado: {datetime.now():%Y-%m-%d %H:%M}',
    f'Total de empleados: {len(df)}',
    f'Salario promedio: {formato(df["salario"].mean())}',
    f'Salario máximo: {mayor["nombre"]} - {formato(mayor["salario"])}',
    f'Salario mínimo: {menor["nombre"]} - {formato(menor["salario"])}',
    '', 'EMPLEADOS POR CARGO',
]
lineas += [f'{cargo}: {cantidad}' for cargo, cantidad in sorted(Counter(df['cargo']).items())]

st.subheader('Descargar reportes')
a, b = st.columns(2)
with a:
    st.download_button('📄 Descargar resumen TXT', '\n'.join(lineas) + '\n', 'resumen.txt', 'text/plain')
with b:
    csv_bytes = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button('📥 Descargar empleados CSV', csv_bytes, 'empleados_procesados.csv', 'text/csv')
