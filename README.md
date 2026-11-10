# Employee Report Automation 📊

Aplicación web en **Python + Streamlit** para cargar un CSV de empleados, analizar salarios, filtrar por cargo, visualizar gráficos y descargar reportes. También conserva una versión de consola.

## Ejecutar la aplicación web

Requiere Python 3.10 o superior. Abre una terminal en la carpeta del proyecto:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Se abrirá la aplicación en el navegador (normalmente en `http://localhost:8501`).

## Uso

1. Explora los cinco empleados ficticios que vienen en `data/empleados.csv`.
2. Opcionalmente, sube tu propio CSV con las columnas `nombre,cargo,salario`.
3. Consulta métricas, filtra empleados por cargo y revisa los gráficos.
4. Descarga un resumen TXT y un CSV procesado.

El salario debe ser un entero no negativo, sin separadores de miles. Usa datos ficticios o autorizados; evita subir datos personales reales a servicios públicos.

## Versión de consola

```powershell
python main.py
```

Genera `reportes/resumen.txt` y `reportes/empleados_procesados.csv` a partir del archivo de ejemplo.

## Tecnologías

Python, Streamlit, Pandas, CSV, Git y GitHub.
