import pandas as pd

def promedio_dias_publicaciones():
    nombre_archivo = 'compilado_MM.CC.xlsx'
    hojas_seleccionadas = ['24HorasTVN', 'cooperativa']

    resultados = []

    try:
        for hoja in hojas_seleccionadas:
            df = pd.read_excel(nombre_archivo, sheet_name=hoja)
            df['created_at'] = pd.to_datetime(df['created_at'], format='%d/%m/%Y %H:%M')

            # Ordena y calcula diferencias en una sola pasada
            df_sorted = df.sort_values(by='created_at')
            df_sorted['dias_desde_anterior'] = (df_sorted['created_at'] - df_sorted['created_at'].shift(1)).dt.days
            df_sorted['horas_desde_anterior'] = (df_sorted['created_at'] - df_sorted['created_at'].shift(1)).dt.total_seconds() / 3600

            if len(df_sorted) > 1:
                df_sorted = df_sorted.iloc[1:]

            promedio_dias = df_sorted['dias_desde_anterior'].mean()
            promedio_horas = df_sorted['horas_desde_anterior'].mean()

            resultados.append((hoja, promedio_dias, promedio_horas))

        for hoja, promedio_dias, promedio_horas in resultados:
            print(f"\nHoja: {hoja}")
            print(f"Promedio de días entre publicaciones sucesivas: {promedio_dias:.2f} días")
            print(f"Promedio de horas entre publicaciones sucesivas: {promedio_horas:.2f} horas")

        df_resultados = pd.DataFrame(resultados, columns=['Hoja', 'Promedio_Dias', 'Promedio_Horas'])
        df_resultados.to_excel('resultados.xlsx', index=False)

        print("\nResultados exportados a 'resultados.xlsx'")

    except Exception as e:
        print(f"Error: {e}")

# Llama a la función
promedio_dias_publicaciones()
