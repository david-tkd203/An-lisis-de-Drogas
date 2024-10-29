import pandas as pd

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

print(largo())