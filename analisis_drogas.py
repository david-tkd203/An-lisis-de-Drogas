import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter



def obtener_recomendaciones():
    # Reemplaza 'COMPILADO MM.CC.xlsx' con el nombre de tu archivo Excel
    nombre_archivo = 'compilado MM.CC.xlsx'
    hojas_seleccionadas = ['24HorasTVN', 'cooperativa']

    # Lista de palabras clave a buscar
    palabras_clave = ['drogas', 'narcotráfico', 'estupefacientes', 'microtráfico']

    # Inicializa un diccionario para almacenar los resultados
    resultados = {}

    # Itera sobre las hojas seleccionadas
    for hoja in hojas_seleccionadas:
        # Lee la hoja específica del archivo Excel
        df = pd.read_excel(nombre_archivo, sheet_name=hoja)

        # Convierte la columna "text" a minúsculas
        df['text'] = df['text'].str.lower()

        # Inicializa el contador para cada palabra clave en esta hoja
        conteo_palabras_clave = {palabra: 0 for palabra in palabras_clave}

        # Función para contar la cantidad de ocurrencias de palabras clave en el texto
        def contar_ocurrencias(texto):
            for palabra_clave in palabras_clave:
                conteo_palabras_clave[palabra_clave] += texto.count(palabra_clave)

        # Aplica la función a cada texto en la columna "text"
        df['text'].apply(contar_ocurrencias)

        # Almacena el resultado en el diccionario
        resultados[hoja] = conteo_palabras_clave

    # Muestra los resultados
    for hoja, conteo_palabras in resultados.items():
        print(f"\nHoja: {hoja}")
        for palabra, conteo in conteo_palabras.items():
            print(f"{palabra}: {conteo} ocurrencias")

        # Gráfico de barras con etiquetas
        plt.figure(figsize=(10, 6))
        bars = plt.bar(conteo_palabras.keys(), conteo_palabras.values(), color='blue')
        plt.title(f"Conteo de palabras clave en {hoja}")
        plt.xlabel("Palabras Clave")
        plt.ylabel("Número de Ocurrencias")

        # Agregar etiquetas con los valores numéricos en las barras
        for bar, conteo in zip(bars, conteo_palabras.values()):
            plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 0.1, str(conteo), ha='center')

        plt.show()
def obtener_hashtag():
    # Reemplaza 'COMPILADO MM.CC.xlsx' con el nombre de tu archivo Excel
    nombre_archivo = 'compilado_MM.CC.xlsx'
    hojas_seleccionadas = ['24HorasTVN', 'cooperativa']

    # Inicializa un diccionario para almacenar los resultados
    resultados = {}

    # Itera sobre las hojas seleccionadas
    for hoja in hojas_seleccionadas:
        # Lee la hoja específica del archivo Excel
        df = pd.read_excel(nombre_archivo, sheet_name=hoja)

        # Filtra y convierte la columna 'entities.hashtags' a listas
        df['entities.hashtags'] = df['entities.hashtags'].apply(lambda x: [] if pd.isna(x) else eval(x))

        # Obtiene todos los hashtags en la hoja
        all_hashtags = [hashtag for hashtags_list in df['entities.hashtags'] for hashtag in hashtags_list]

        # Encuentra los hashtags más utilizados
        top_hashtags = dict(Counter(all_hashtags).most_common())

        # Almacena el resultado en el diccionario
        resultados[hoja] = top_hashtags

    # Muestra y exporta los resultados en formato de tabla
    for hoja, conteo_hashtags in resultados.items():
        print(f"\nHoja: {hoja}")
        df_resultado = pd.DataFrame(list(conteo_hashtags.items()), columns=['Hashtag', 'Número de Ocurrencias'])
        print(df_resultado)

        # Exporta el DataFrame a un archivo Excel
        nombre_archivo_salida = f'resultados_{hoja}.xlsx'
        df_resultado.to_excel(nombre_archivo_salida, index=False)
        print(f"\nResultados exportados a {nombre_archivo_salida}")

def obtener_ciudades_region():

    # Reemplaza 'COMPILADO MM.CC.xlsx' con el nombre de tu archivo Excel
    nombre_archivo = 'compilado_MM.CC.xlsx'
    hojas_seleccionadas = ['24HorasTVN', 'cooperativa']

    # Hashtags a incluir
    hashtags_a_incluir = {
        'Chillán': ['#Chillán', '#ChillánViejo', '#Pemuco'],
        'Valparaíso': ['#Valparaíso', '#ViñadelMar', '#Quilpué', '#Limache'],
        'Rancagua': ['#Rancagua', '#Coltauco', '#CooperartivaRegiones'],
        'Punta Arenas': ['#PuntaArenas'],
        'Iquique': ['#Iquique'],
        'Coquimbo': ['#Coquimbo', '#Ovalle', '#LaSerena'],
        'San Fernando': ['#SanFernando'],
        'Coyhaique': ['#Coyhaique'],
        'Santa Cruz': ['#SantaCruz'],
        'Curicó': ['#Curicó'],
        'Osorno': ['#Osorno'],
        'La Araucanía': ['#LaAraucanía', '#Talca'],
        'Concepción': ['#Concepción'],
        'Llay Llay': ['#LlayLlay'],
        'Pichilemu': ['#Pichilemu'],
        'Monte Patria': ['#MontePatria', '#Peralillo'],
        'Los Ríos': ['#LosRíos'],
        'Combarbalá': ['#Combarbalá'],
        'Efecto China': ['#EfectoChina'],
        'Colchane': ['#Colchane'],
        'Magallanes': ['#Magallanes', '#PuertoNatales'],
        'Nogales': ['#Nogales'],
        'Bulnes': ['#Bulnes'],
        'Tarapacá': ['#Tarapaca'],
        'Puerto': ['#Puerto', '#PuertoNatales', '#PuertoNatales'],
        'Perquenco': ['#Perquenco']
    }

    # Inicializa un diccionario para almacenar los resultados
    resultados = {}

    # Itera sobre las hojas seleccionadas
    for hoja in hojas_seleccionadas:
        # Lee la hoja específica del archivo Excel
        df = pd.read_excel(nombre_archivo, sheet_name=hoja)

        # Filtra y convierte la columna 'entities.hashtags' a listas
        df['entities.hashtags'] = df['entities.hashtags'].apply(lambda x: [] if pd.isna(x) else eval(x))

        # Inicializa un diccionario para almacenar los resultados de esta hoja
        resultados_hoja = {}

        # Itera sobre las regiones y ciudades
        for region_ciudad, hashtags_region_ciudad in hashtags_a_incluir.items():
            # Obtiene todos los hashtags en la hoja para la región o ciudad específica
            all_hashtags = [hashtag for hashtags_list in df['entities.hashtags'] for hashtag in hashtags_list
                            if hashtag in hashtags_region_ciudad]

            # Encuentra los hashtags más utilizados para esta región o ciudad
            top_hashtags = dict(Counter(all_hashtags).most_common())

            # Almacena el resultado en el diccionario de esta hoja
            resultados_hoja[region_ciudad] = top_hashtags

            # Almacena el resultado en el diccionario general
            if region_ciudad not in resultados:
                resultados[region_ciudad] = top_hashtags
            else:
                resultados[region_ciudad].update(top_hashtags)

        # Muestra los resultados en formato de tabla para esta hoja
        print(f"\nHoja: {hoja}")
        for region_ciudad, conteo_hashtags in resultados_hoja.items():
            print(f"\n{region_ciudad}:")
            df_resultado = pd.DataFrame(list(conteo_hashtags.items()), columns=['Hashtag', f'{region_ciudad} - Número de Ocurrencias'])
            print(df_resultado)

    # Combina todos los resultados en un único DataFrame
    df_final = pd.DataFrame()

    for region_ciudad, conteo_hashtags in resultados.items():
        df_resultado = pd.DataFrame(list(conteo_hashtags.items()), columns=['Hashtag', f'{region_ciudad} - Número de Ocurrencias'])
        df_final = pd.concat([df_final, df_resultado], axis=1)

    # Exporta el DataFrame final a un archivo Excel con el nombre de la región como índice
    nombre_archivo_salida = 'resultados_totales.xlsx'
    df_final.to_excel(nombre_archivo_salida, index_label='Región')
    print(f"\nResultados totales exportados a {nombre_archivo_salida}")

def obtener_metricas_publicaciones():

    # Reemplaza 'COMPILADO MM.CC.xlsx' con el nombre de tu archivo Excel
    nombre_archivo = 'compilado_MM.CC.xlsx'
    hojas_seleccionadas = ['24HorasTVN', 'cooperativa']

    # Itera sobre las hojas seleccionadas
    for hoja in hojas_seleccionadas:
        # Lee la hoja específica del archivo Excel
        df = pd.read_excel(nombre_archivo, sheet_name=hoja)

        # Asegúrate de que la columna 'created_at' sea de tipo datetime
        df['created_at'] = pd.to_datetime(df['created_at'])

        # Crea un DataFrame con la suma de métricas para cada publicación según la fecha
        columnas_a_sumar = ['public_metrics.impression_count',
                            'public_metrics.reply_count',
                            'public_metrics.retweet_count',
                            'public_metrics.quote_count',
                            'public_metrics.like_count']

        leyendas = {
            'public_metrics.impression_count': 'Impresiones',
            'public_metrics.reply_count': 'Comentarios',
            'public_metrics.retweet_count': 'Retweet',
            'public_metrics.quote_count': 'Retweet con Comentario',
            'public_metrics.like_count': 'Likes'
        }

        tabla_publicaciones = df.groupby(['created_at'])[columnas_a_sumar].sum().reset_index()

        # Imprime el DataFrame para esta hoja
        print(f"\nTabla de publicaciones para la hoja '{hoja}':")
        print(tabla_publicaciones)

        # Exporta el DataFrame a un archivo Excel
        nombre_archivo_salida = f'tabla_publicaciones_{hoja}.xlsx'
        tabla_publicaciones.to_excel(nombre_archivo_salida, index=False)
        print(f"\nTabla exportada a '{nombre_archivo_salida}'")

        # Graficar las métricas
        plt.figure(figsize=(10, 6))
        for columna in columnas_a_sumar:
            plt.plot(tabla_publicaciones['created_at'], tabla_publicaciones[columna], label=f"{leyendas[columna]} Total: {tabla_publicaciones[columna].sum()}")

        plt.title(f'Gráfico de métricas para la hoja {hoja}')
        plt.xlabel('Fecha')
        plt.ylabel('Valor')
        plt.legend()
        plt.show()


def promedio_dias_publicaciones():
    # Reemplaza 'COMPILADO MM.CC.xlsx' con el nombre de tu archivo Excel
    nombre_archivo = 'compilado_MM.CC.xlsx'
    hojas_seleccionadas = ['24HorasTVN', 'cooperativa']

    # Lista para almacenar los resultados
    resultados = []

    try:
        # Itera sobre las hojas seleccionadas
        for hoja in hojas_seleccionadas:
            # Lee la hoja específica del archivo Excel
            df = pd.read_excel(nombre_archivo, sheet_name=hoja)

            # Asegúrate de que la columna 'created_at' sea de tipo datetime
            df['created_at'] = pd.to_datetime(df['created_at'], format='%d/%m/%Y %H:%M')

            # Ordena el DataFrame por 'created_at'
            df = df.sort_values(by='created_at')

            # Calcula la diferencia de días entre cada fecha y la siguiente
            df['dias_desde_anterior'] = (df['created_at'] - df['created_at'].shift(1)).dt.days

            # Calcula el promedio de la diferencia de días y agrega el resultado a la lista
            promedio_dias = df['dias_desde_anterior'].mean()

            # Calcula la diferencia de horas entre cada fecha y la fecha anterior
            df['horas_desde_anterior'] = (df['created_at'] - df['created_at'].shift(1)).dt.total_seconds() / 3600

            # Calcula el promedio de la diferencia de horas
            promedio_horas = df['horas_desde_anterior'].mean()

            resultados.append((hoja, promedio_dias, promedio_horas))

        # Muestra los resultados
        for hoja, promedio_dias, promedio_horas in resultados:
            print(f"\nHoja: {hoja}")
            print(f"Promedio de días entre publicaciones sucesivas: {promedio_dias:.2f} días")
            print(f"Promedio de horas entre publicaciones sucesivas: {promedio_horas:.2f} horas")

        # Exporta los resultados a un archivo Excel
        df_resultados = pd.DataFrame(resultados, columns=['Hoja', 'Promedio_Dias', 'Promedio_Horas'])
        df_resultados.to_excel('resultados.xlsx', index=False)  # Corregido el nombre del archivo

        print("\nResultados exportados a 'resultados.xlsx'")

    except Exception as e:
        print(f"Error: {e}")

def largo():
    # Reemplaza 'nombre_del_archivo.xlsx' con el nombre de tu archivo Excel
    archivo = 'compilado_MM.CC.xlsx'

    # Lista de hojas a considerar
    hojas_a_considerar = ['cooperativa', '24HorasTVN']

    # Itera sobre las hojas y obtiene el número de filas para cada una
    for hoja in hojas_a_considerar:
        # Lee el archivo Excel en un DataFrame de pandas para la hoja actual
        df = pd.read_excel(archivo, sheet_name=hoja)

        # Obtiene el número de filas en el DataFrame
        numero_de_filas = len(df)

        # Imprime el resultado para cada hoja
        print(f'Número de filas en la hoja "{hoja}": {numero_de_filas}')



menu="""[1]Obtener recomendaciones
[2]Obtener hashtag
[3]Obtener Hashtag de ciudades y regiones
[4]Obtener metricas de las publicaciones
[5]Obtener promedio de dias con el que se hacia publicaciones
[6]Saber el largo
[7]Salir del programa
"""
opcion=0
while opcion != 7:
    print(menu)
    opcion=int(input("Escoja una opciona de las mencionadas anteriormente: "))

    if opcion in [1,2,3,4,5]:
        if opcion == 1:
            print(obtener_recomendaciones())
        if opcion == 2:
            print(obtener_hashtag())
        if opcion == 3:
            print(obtener_ciudades_region())
        if opcion == 4:
            print(obtener_metricas_publicaciones())
        if opcion == 5:
            print(promedio_dias_publicaciones())
        if opcion == 6:
            print(largo())