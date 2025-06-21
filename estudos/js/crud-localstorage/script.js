let tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];
let proximoId = tarefas.length ? Math.max(...tarefas.map(t => t.id)) + 1 : 1;

function salvarLocalStorage() {
  localStorage.setItem("tarefas", JSON.stringify(tarefas));
}

function renderizarTarefas() {
  const container = document.getElementById("tarefas-container");
  container.innerHTML = "";

  tarefas.forEach(tarefa => {
    const div = document.createElement("div");
    div.className = "tarefa";
    div.innerHTML = `
      <strong>${tarefa.titulo}</strong> - ${tarefa.descricao} 
      [${tarefa.concluida ? "✅ Concluída" : "❌ Pendente"}]
      <br>
      <button onclick="atualizarTarefa(${tarefa.id})">Concluir</button>
      <button onclick="deletarTarefa(${tarefa.id})">Excluir</button>
    `;
    container.appendChild(div);
  });
}

function criarTarefa() {
  const titulo = document.getElementById("titulo").value.trim();
  const descricao = document.getElementById("descricao").value.trim();

  if (!titulo || !descricao) {
    alert("Preencha todos os campos!");
    return;
  }

  const novaTarefa = {
    id: proximoId++,
    titulo,
    descricao,
    concluida: false
  };

  tarefas.push(novaTarefa);
  salvarLocalStorage();
  renderizarTarefas();

  document.getElementById("titulo").value = "";
  document.getElementById("descricao").value = "";
}

function atualizarTarefa(id) {
  const tarefa = tarefas.find(t => t.id === id);
  if (tarefa) {
    tarefa.concluida = !tarefa.concluida;
    salvarLocalStorage();
    renderizarTarefas();
  }
}

function deletarTarefa(id) {
  tarefas = tarefas.filter(t => t.id !== id);
  salvarLocalStorage();
  renderizarTarefas();
}

renderizarTarefas();
