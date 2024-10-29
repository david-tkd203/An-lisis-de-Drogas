# Análisis de Drogas - Análisis de Contenido de Redes Sociales y Medios

Este proyecto contiene un conjunto de scripts en Python para analizar contenido relacionado con drogas y narcotráfico en redes sociales y medios de comunicación. Utilizando hojas de Excel específicas, se procesan datos para obtener recomendaciones, hashtags populares, y otras métricas. 

## Requisitos

- Python 3.8 o superior
- Pandas: `pip install pandas`
- Matplotlib: `pip install matplotlib`

## Funciones Principales

1. **Obtener recomendaciones**: Extrae palabras clave relacionadas con drogas y narcotráfico en hojas específicas del archivo Excel.
2. **Obtener hashtag**: Encuentra los hashtags más comunes en las publicaciones.
3. **Obtener Hashtags de ciudades y regiones**: Filtra y agrupa hashtags por ciudades o regiones predeterminadas.
4. **Obtener métricas de publicaciones**: Calcula y grafica métricas como impresiones, retweets, y likes.
5. **Obtener promedio de días de publicaciones**: Calcula el promedio de días y horas entre publicaciones.
6. **Obtener largo de la hoja**: Cuenta el número de filas en cada hoja seleccionada.

## Ejecución

1. Abre el archivo `compilado_MM.CC.xlsx` en la misma carpeta que el script.
2. Ejecuta el archivo principal y sigue el menú interactivo para seleccionar la función deseada.

## Estructura de Archivos

- `compilado_MM.CC.xlsx`: Archivo Excel con las hojas de datos de medios de comunicación.
- `resultados_hoja.xlsx`: Exportación de resultados por hoja.
- `resultados_totales.xlsx`: Resultados combinados de hashtags por ciudades o regiones.
- `resultados.xlsx`: Exportación del promedio de días entre publicaciones.

## Gráficos y Resultados

Cada función incluye la opción de visualización de gráficos o exportación de los resultados a un archivo Excel.

## Contacto

Para cualquier consulta, puedes contactar a [david-tkd203](https://github.com/david-tkd203).
