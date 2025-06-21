let tarefas = [];
let proximoId = 1;

function criarTarefa(titulo, descricao) {
  const tarefa = {
    id: proximoId++,
    titulo,
    descricao,
    concluida: false,
  };
  tarefas.push(tarefa);
  return tarefa;
}

function listarTarefas() {
  return tarefas;
}

function atualizarTarefa(id, dados) {
  const tarefa = tarefas.find(t => t.id === id);
  if (tarefa) {
    if (dados.titulo !== undefined) tarefa.titulo = dados.titulo;
    if (dados.descricao !== undefined) tarefa.descricao = dados.descricao;
    if (dados.concluida !== undefined) tarefa.concluida = dados.concluida;
  }
  return tarefa;
}

function deletarTarefa(id) {
  tarefas = tarefas.filter(t => t.id !== id);
}
