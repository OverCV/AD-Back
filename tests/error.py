import pandas as pd

# Supongamos que estos son los resultados de EMD para cada red y estrategia
resultados = {
    'Red 4 Nodos': {
        'Programación Dinámica': [0, 0, 0, 0, 0],
        'Branch and Bound': [0, 0, 0, 0, 0],
        'Algoritmos Genéticos': [0, 0, 1.59476, 0.87499, 1.0653]
    },
    'Red 6 Nodos': {
        'Programación Dinámica': [0.9375, 0.109375, 0.45818, 0.125, 0.58487395, 0.03125, 0.21875],
        'Branch and Bound': [0.9375, 1.74609375, 1.625, 1.125, 1.9921875, 10, 1.125],
        'Algoritmos Genéticos': [1.383483, 1.0625, 0, 0.6875, 0.273437, 0.03125, 1.738952]
    },
    'Red 8 Nodos (primera)': {
        'Programación Dinámica': [0.5, 0, 0, 0, 0],
        'Branch and Bound': [0, 0, 0, 0, 0],
        'Algoritmos Genéticos': [0.5, 0.5, 0, 0, 0]
    },
    'Red 8 Nodos (segunda)': {
        'Programación Dinámica': [0, 0, 0, 0, 0],
        'Branch and Bound': [0, 0, 0, 0, 0],
        'Algoritmos Genéticos': [0.5, 0, 0, 0, 0]
    },
    'Red 10 Nodos': {
        'Programación Dinámica': [1.125, 1.7875938415527344, 1.7875938415527344, 0.054931640625],
        'Branch and Bound': [1.125, 0.625, 10, 10],
        'Algoritmos Genéticos': [0.48046875, 0.48046875, 1.7875938415527344, 0.054931640625]
    }
    # Añadir aquí los resultados para las demás redes
}

# Etiquetas de instancias para cada red
etiquetas_instancias = {
    'Red 4 Nodos': [
        'ABCD | ABCD', 'ABC | ABCD', 'ABCD | AC', 'AC | ABC', 'ABC | ABC'
    ],
    'Red 6 Nodos': [
        'ABC | AC', 'ABC | ABC', 'ABC | ABCDE', 'ABC | ABCE', 'ABC | ACDE', 'ABC | ACDEF', 'BCDEF | ABEF'
    ],
    'Red 8 Nodos (primera)': [
        'ABCDEFGH | ABCDEFGH',  'ABCGH | ABCDEFGH', 'ABCDEFGH | BCDEFGH', 'ABCDEFGH | DEFGH', 'ABCD | DEFGH'
    ],
    'Red 8 Nodos (segunda)': [
        'ABCDEFGH | ABCDEFGH', 'ABCDEFGH | ACDEFGH', 'CDEFGH | EFGH', 'CDEFGH | ABC', 'ABC | ABC'
    ],
    'Red 10 Nodos': [
        'ABCDEFGHIJ | ABCDEFGHIJ', 'ABCDEFJ | ABCDEFGHIJ', 'ABCDEFJ | ADEFGHIJ', 'ABCDEFGJ | ABDEFGHIJ'
    ]
    # Añadir etiquetas para otras redes
}

# Crear un DataFrame para cada red y exportarlo a Excel
with pd.ExcelWriter('resultados_emd.xlsx') as writer:
    for red, data in resultados.items():
        df = pd.DataFrame(data)
        if red in etiquetas_instancias:
            etiquetas = etiquetas_instancias[red]
            if len(etiquetas) == len(df):
                df.index = etiquetas
            else:
                print(f"Advertencia: La longitud de las etiquetas para {
                      red} no coincide con los datos.")
        df.to_excel(writer, sheet_name=red)

print("Resultados exportados a 'resultados_emd.xlsx'")

# Función para calcular el error relativo


def calcular_error(df):
    df['EMD Mínimo'] = df.min(axis=1)
    for estrategia in df.columns[:-1]:
        df[f'Error {estrategia}'] = df[estrategia] - df['EMD Mínimo']
    return df


# Aplicar la función a cada DataFrame y exportar los resultados
with pd.ExcelWriter('resultados_emd_con_errores.xlsx') as writer:
    for red, data in resultados.items():
        df = pd.DataFrame(data)
        if red in etiquetas_instancias:
            etiquetas = etiquetas_instancias[red]
            if len(etiquetas) == len(df):
                df.index = etiquetas
            else:
                print(f"Advertencia: La longitud de las etiquetas para {
                      red} no coincide con los datos.")
        df = calcular_error(df)
        df.to_excel(writer, sheet_name=red)

print("Resultados con errores exportados a 'resultados_emd_con_errores.xlsx'")
