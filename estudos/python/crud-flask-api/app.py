from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tarefas = []
proximo_id = 1

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    global proximo_id
    dados = request.get_json()
    nova_tarefa = {
        'id': proximo_id,
        'titulo': dados.get('titulo'),
        'descricao': dados.get('descricao'),
        'concluida': False
    }
    tarefas.append(nova_tarefa)
    proximo_id += 1
    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['titulo'] = dados.get('titulo', tarefa['titulo'])
            tarefa['descricao'] = dados.get('descricao', tarefa['descricao'])
            tarefa['concluida'] = dados.get('concluida', tarefa['concluida'])
            return jsonify(tarefa)
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id]
    return jsonify({'mensagem': f'Tarefa {id} deletada'})

if __name__ == '__main__':
    app.run(debug=True)
