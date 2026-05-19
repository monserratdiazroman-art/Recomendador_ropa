import pandas as pd

df = pd.read_csv("Ropa.csv")

def recomendar(color, estilo, genero):

    resultado = df[
        (df["Color"] == color) &
        (df["Estilo"] == estilo) &
        (df["Genero"] == genero)
    ]

    # si encuentra coincidencia exacta
    if not resultado.empty:
        fila = resultado.iloc[0]
    else:
        # fallback por si no existe combinación exacta
        fila = df.iloc[0]

    return {
        "prenda": fila["Prenda"],
        "imagen": fila["Imagen"]
    }