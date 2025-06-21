from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///produtos.db"
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float)
    estoque = db.Column(db.Integer)

with app.app_context():
    db.create_all()

@app.route("/produtos", methods=["GET"])
def listar():
    produtos = Produto.query.all()
    return jsonify([{
        "id": p.id,
        "nome": p.nome,
        "preco": p.preco,
        "estoque": p.estoque
    } for p in produtos])

@app.route("/produtos", methods=["POST"])
def adicionar():
    data = request.get_json()
    novo = Produto(nome=data["nome"], preco=data["preco"], estoque=data["estoque"])
    db.session.add(novo)
    db.session.commit()
    return jsonify({
        "id": novo.id,
        "nome": novo.nome,
        "preco": novo.preco,
        "estoque": novo.estoque
    }), 201

@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar(id):
    data = request.get_json()
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    produto.nome = data.get("nome", produto.nome)
    produto.preco = data.get("preco", produto.preco)
    produto.estoque = data.get("estoque", produto.estoque)
    db.session.commit()
    return jsonify({
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco,
        "estoque": produto.estoque
    })

@app.route("/produtos/<int:id>", methods=["DELETE"])
def deletar(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    db.session.delete(produto)
    db.session.commit()
    return jsonify({"mensagem": f"Produto {id} deletado com sucesso."})

if __name__ == "__main__":
    app.run(debug=True)
