import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(BASE_DIR, "Ropa.csv")

df = pd.read_csv(ruta_csv)

def recomendar(color, estilo, genero):
    
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