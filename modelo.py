import pandas as pd
import os

def cargar_datos():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(BASE_DIR, "Ropa.csv")
    return pd.read_csv(ruta_csv)

def recomendar(color, estilo, genero):
    
    df = cargar_datos()

    resultado = df[
        (df["Color"] == color) &
        (df["Estilo"] == estilo) &
        (df["Genero"] == genero)
    ]

    if not resultado.empty:
        fila = resultado.iloc[0]
    else:
        fila = df.iloc[0]

    return {
        "prenda": fila["Prenda"],
        "imagen": fila["Imagen"]
    }