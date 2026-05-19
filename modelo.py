import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

# cargar csv
df = pd.read_csv("Ropa.csv")

# convertir texto a números
le_color = LabelEncoder()
le_estilo = LabelEncoder()
le_genero = LabelEncoder()

df["Color_num"] = le_color.fit_transform(df["Color"])
df["Estilo_num"] = le_estilo.fit_transform(df["Estilo"])
df["Genero_num"] = le_genero.fit_transform(df["Genero"])

# entrenamiento IA
X = df[["Color_num", "Estilo_num", "Genero_num"]]

modelo = NearestNeighbors(n_neighbors=1)
modelo.fit(X)

def recomendar(color, estilo, genero):

    entrada = [[
        le_color.transform([color])[0],
        le_estilo.transform([estilo])[0],
        le_genero.transform([genero])[0]
    ]]

    distancia, indice = modelo.kneighbors(entrada)

    fila = df.iloc[indice[0][0]]

    return {
        "prenda": fila["Prenda"],
        "imagen": fila["Imagen"]
    }