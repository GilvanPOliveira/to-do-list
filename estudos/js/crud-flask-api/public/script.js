const API_URL = "http://localhost:5000/tarefas";

async function carregarTarefas() {
  const resp = await fetch(API_URL);
  const tarefas = await resp.json();

  const container = document.getElementById("tarefas-container");
  container.innerHTML = "";

  tarefas.forEach(tarefa => {
    const div = document.createElement("div");
    div.className = "tarefa";
    div.innerHTML = `
      <strong>${tarefa.titulo}</strong> - ${tarefa.descricao} 
      [${tarefa.concluida ? "✅" : "❌"}]
      <br>
      <button onclick="concluirTarefa(${tarefa.id}, ${!tarefa.concluida})">Concluir</button>
      <button onclick="deletarTarefa(${tarefa.id})">Excluir</button>
    `;
    container.appendChild(div);
  });
}

async function criarTarefa() {
  const titulo = document.getElementById("titulo").value.trim();
  const descricao = document.getElementById("descricao").value.trim();

  if (!titulo || !descricao) {
    alert("Preencha os campos!");
    return;
  }

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ titulo, descricao })
  });

  document.getElementById("titulo").value = "";
  document.getElementById("descricao").value = "";

  carregarTarefas();
}

async function concluirTarefa(id, novoStatus) {
  await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ concluida: novoStatus })
  });
  carregarTarefas();
}

async function deletarTarefa(id) {
  await fetch(`${API_URL}/${id}`, { method: "DELETE" });
  carregarTarefas();
}

carregarTarefas();
