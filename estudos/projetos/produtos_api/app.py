from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

produtos = []
proximo_id = 1

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    global proximo_id
    dados = request.get_json()
    produto = {
        "id": proximo_id,
        "nome": dados.get("nome"),
        "preco": dados.get("preco"),
        "estoque": dados.get("estoque")
    }
    produtos.append(produto)
    proximo_id += 1
    return jsonify(produto), 201

@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.get_json()
    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = dados.get("nome", produto["nome"])
            produto["preco"] = dados.get("preco", produto["preco"])
            produto["estoque"] = dados.get("estoque", produto["estoque"])
            return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route("/produtos/<int:id>", methods=["DELETE"])
def remover_produto(id):
    global produtos
    produtos = [p for p in produtos if p["id"] != id]
    return jsonify({"mensagem": f"Produto {id} removido com sucesso."})

if __name__ == "__main__":
    app.run(debug=True)
