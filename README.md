# Employee Report Automation

Aplicación de consola en Python para procesar un CSV de empleados y generar un resumen de salarios y un CSV normalizado.

## Requisitos

Python 3.10 o superior. No requiere dependencias externas.

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

## Entrada

Edita `data/empleados.csv` con las columnas `nombre,cargo,salario`. El salario debe ser un entero no negativo, sin separadores de miles.

## Salidas

Se generan `reportes/resumen.txt` y `reportes/empleados_procesados.csv`.

## Funcionalidades

- Lectura y validación de CSV
- Total de empleados, salario promedio, máximo y mínimo
- Conteo de empleados por cargo
- Exportación de resultados y manejo de errores

Los datos de ejemplo son ficticios.
