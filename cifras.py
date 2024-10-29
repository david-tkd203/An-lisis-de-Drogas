import pandas as pd

# Reemplaza 'compilado_MM.CC.xlsx' con el nombre de tu archivo Excel
nombre_archivo = 'compilado_MM.CC.xlsx'

# Lista de hojas a considerar
hojas_a_considerar = ['cooperativa', '24HorasTVN']

# Diccionario para almacenar los resultados
resultados = {}

# Itera sobre las hojas y realiza las operaciones deseadas
for hoja in hojas_a_considerar:
    # Lee el archivo Excel en un DataFrame de pandas para la hoja actual
    df = pd.read_excel(nombre_archivo, sheet_name=hoja)

    # Asegúrate de que la columna 'created_at' sea de tipo datetime
    df['created_at'] = pd.to_datetime(df['created_at'], format='%d/%m/%Y %H:%M')

    # Filtra las filas para obtener solo las que están en los años 2022 y 2023
    filas_2022_2023 = df[(df['created_at'].dt.year >= 2022) & (df['created_at'].dt.year <= 2023)]

    # Cuenta el número de filas en los años 2022 y 2023
    total_filas_2022_2023 = len(filas_2022_2023)

    # Divide el número total de filas por 16,115 para el año 2022
    if 2022 in filas_2022_2023['created_at'].dt.year.unique():
        resultado_por_16115 = (total_filas_2022_2023 / 16115)*100
    else:
        resultado_por_16115 = 0

    # Almacena los resultados en el diccionario
    resultados[hoja] = {
        'total_filas_2022_2023': total_filas_2022_2023,
        'resultado_por_16115': resultado_por_16115
    }

# Imprime los resultados
for hoja, datos in resultados.items():
    print(f"\nHoja: {hoja}")
    print(f"Total de filas en los años 2022 y 2023: {datos['total_filas_2022_2023']}")
    print(f"Resultado dividido por 16,115 para el año 2022: {datos['resultado_por_16115']:.4f}%")
