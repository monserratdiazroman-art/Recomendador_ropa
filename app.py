from flask import Flask, render_template, request
from modelo import recomendar
import os
print("APP INICIANDO...")

app = Flask(__name__, template_folder="templates")

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/recomendar", methods=["GET","POST"])
def recomendar_outfit():

    color = request.form["color"]
    estilo = request.form["estilo"]
    genero = request.form["genero"]

    resultado = recomendar(color, estilo, genero)

    return render_template(
        "index.html",
        prenda=resultado["prenda"],
        imagen=resultado["imagen"],
        color=color,
        estilo=estilo,
        genero=genero
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print("Puerto:", port)
    app.run(host="0.0.0.0", port=port)
    