# Employee Report Automation 📊

Aplicación web desarrollada con **Python y Streamlit** para automatizar el análisis de información de empleados, visualizar estadísticas salariales y generar reportes descargables.

Este proyecto forma parte de mi portafolio de desarrollo de software y demuestra habilidades en procesamiento de datos, automatización e interfaces web con Python.

## 🌐 Demo en vivo

**[Abrir aplicación web](https://employee-report-automation-hld7rk9dgt6manozprxjkk.streamlit.app/)**

Puedes probar el dashboard directamente desde tu navegador, sin instalar nada.

## 🚀 Funcionalidades

- Cargar archivos CSV con información de empleados.
- Visualizar el total de empleados y estadísticas salariales.
- Identificar los salarios más altos y más bajos.
- Filtrar empleados por cargo.
- Consultar gráficos de distribución y comparación salarial.
- Descargar reportes en formatos CSV y TXT.
- Ejecutar una versión alternativa desde la consola.

## 🛠️ Tecnologías utilizadas

- **Python:** procesamiento de información y lógica de negocio.
- **Streamlit:** desarrollo de la interfaz web interactiva.
- **Pandas:** manipulación y análisis de datos.
- **CSV:** lectura y exportación de información.
- **Git y GitHub:** control de versiones.
- **Streamlit Community Cloud:** despliegue de la aplicación.

## 💻 Instalación y ejecución local

**Requisitos:** Python 3.10 o superior.

Clona el repositorio o descarga el código fuente y abre una terminal en la carpeta del proyecto.

Instala las dependencias:

```powershell
python -m pip install -r requirements.txt
```

Inicia la aplicación:

```powershell
python -m streamlit run app.py
```

Abre en tu navegador:

http://localhost:8501

## 📋 Cómo utilizar la aplicación

1. Explora los cinco empleados ficticios incluidos en `data/empleados.csv`.
2. Opcionalmente, carga tu propio archivo CSV con las columnas `nombre,cargo,salario`.
3. Consulta las métricas y filtra empleados por cargo.
4. Revisa los gráficos y descarga los reportes generados.

**Formato de ejemplo:**

```csv
nombre,cargo,salario
Carlos,Desarrollador,2500000
Ana,Diseñadora,2800000
Laura,Analista,3200000
```

El salario debe ser un número entero no negativo, sin separadores de miles.

Utiliza datos ficticios o autorizados y evita subir información personal real a servicios públicos.

## 🖥️ Versión de consola

El proyecto también incluye una versión ejecutable desde la terminal:

```powershell
python main.py
```

Esta versión procesa los datos del CSV y genera:

- `reportes/resumen.txt`
- `reportes/empleados_procesados.csv`

## 📁 Estructura del proyecto

```text
employee-report-automation/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── data/
│   └── empleados.csv
└── reportes/
    ├── resumen.txt
    └── empleados_procesados.csv
```

## 🎯 Objetivo del proyecto

Desarrollar una herramienta sencilla de automatización y análisis de datos, integrando procesamiento de archivos, cálculos estadísticos, visualización interactiva y generación de reportes mediante Python.

El proyecto está diseñado para demostrar conocimientos prácticos de programación y desarrollo de aplicaciones web.