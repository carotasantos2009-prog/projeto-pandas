
import os
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

    dados = {
        "Aluno": ["Ana", "João", "Maria", "Pedro"],
        "Nota": [8, 6, 9, 7]
    }

    tabela = pd.DataFrame(dados)

    media = tabela["Nota"].mean()
    maior = tabela["Nota"].max()
    menor = tabela["Nota"].min()

    tabela["Situação"] = tabela["Nota"].apply(
        lambda nota: "Aprovado" if nota >= 7 else "Recuperação"
    )

    alunos = tabela.to_dict(orient="records")

    return render_template(
        "index.html",
        alunos=alunos,
        media=media,
        maior=maior,
        menor=menor
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
