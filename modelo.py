import pandas as pd
import os

print("CARGANDO MODELO...")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(BASE_DIR, "Ropa.csv")

try:
    df = pd.read_csv(ruta_csv, encoding="utf-8")
    print("CSV cargado correctamente")
    print(df.head())
except Exception as e:
    print("ERROR CARGANDO CSV:", e)
    df = pd.DataFrame(columns=["Prenda", "Imagen", "Color", "Estilo", "Genero"])

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