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
    if (dados.titulo !== undefined) {
      tarefa.titulo = dados.titulo;
    }
    if (dados.descricao !== undefined) {
      tarefa.descricao = dados.descricao;
    }
    if (dados.concluida !== undefined) {
      tarefa.concluida = dados.concluida;
    }
    return tarefa;
  }
}

function deletarTarefa(id) {
  tarefas = tarefas.filter(t => t.id !== id);
}

// Testando as funções
console.log("Criando tarefas...");
criarTarefa("Estudar JavaScript", "Focar em CRUD");
criarTarefa("Ler documentação", "MDN e outras fontes");

console.log("\nTarefas:");
console.log(listarTarefas());

console.log("\nAtualizando tarefa 1...");
atualizarTarefa(1, { concluida: true });

console.log("\nTarefas após atualização:");
console.log(listarTarefas());

console.log("\nDeletando tarefa 2...");
deletarTarefa(2);

console.log("\nTarefas finais:");
console.log(listarTarefas());