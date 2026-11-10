import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
ENTRADA = BASE / 'data' / 'empleados.csv'
SALIDA = BASE / 'reportes'


def cargar_empleados(ruta):
    empleados = []
    with ruta.open('r', encoding='utf-8-sig', newline='') as archivo:
        lector = csv.DictReader(archivo)
        campos = {'nombre', 'cargo', 'salario'}
        if not lector.fieldnames or not campos.issubset(lector.fieldnames):
            raise ValueError('El CSV debe contener las columnas nombre,cargo,salario')
        for numero, fila in enumerate(lector, start=2):
            nombre = (fila.get('nombre') or '').strip()
            cargo = (fila.get('cargo') or '').strip()
            try:
                salario = int((fila.get('salario') or '').strip())
            except ValueError as exc:
                raise ValueError(f'Salario inválido en la fila {numero}') from exc
            if not nombre or not cargo or salario < 0:
                raise ValueError(f'Datos inválidos en la fila {numero}')
            empleados.append({'nombre': nombre, 'cargo': cargo, 'salario': salario})
    if not empleados:
        raise ValueError('El CSV no contiene empleados')
    return empleados


def generar_reportes(empleados):
    SALIDA.mkdir(exist_ok=True)
    total = len(empleados)
    salarios = [e['salario'] for e in empleados]
    promedio = sum(salarios) / total
    mayor = max(empleados, key=lambda e: e['salario'])
    menor = min(empleados, key=lambda e: e['salario'])
    cargos = Counter(e['cargo'] for e in empleados)

    reporte_txt = SALIDA / 'resumen.txt'
    lineas = [
        'REPORTE DE EMPLEADOS',
        f'Generado: {datetime.now():%Y-%m-%d %H:%M}',
        f'Total de empleados: {total}',
        f'Salario promedio: ${promedio:,.0f}',
        f'Salario máximo: {mayor["nombre"]} - ${mayor["salario"]:,.0f}',
        f'Salario mínimo: {menor["nombre"]} - ${menor["salario"]:,.0f}',
        '', 'EMPLEADOS POR CARGO',
    ]
    lineas += [f'{cargo}: {cantidad}' for cargo, cantidad in sorted(cargos.items())]
    reporte_txt.write_text('\n'.join(lineas) + '\n', encoding='utf-8')

    reporte_csv = SALIDA / 'empleados_procesados.csv'
    with reporte_csv.open('w', encoding='utf-8-sig', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'cargo', 'salario'])
        escritor.writeheader()
        escritor.writerows(empleados)
    return lineas


def main():
    try:
        empleados = cargar_empleados(ENTRADA)
        lineas = generar_reportes(empleados)
        print('\n'.join(lineas))
        print(f'\nReportes guardados en: {SALIDA}')
    except (FileNotFoundError, PermissionError, ValueError, OSError) as error:
        print(f'Error: {error}')
        raise SystemExit(1)


if __name__ == '__main__':
    main()
