let usuarios = [];

function renderizar() {
  const lista = document.getElementById("lista");
  lista.innerHTML = "";
  usuarios.forEach((usuario, i) => {
    const li = document.createElement("li");
    li.textContent = `${usuario.nome} (${usuario.email})`;
    li.innerHTML += ` <button onclick="removerUsuario(${i})">Remover</button>`;
    lista.appendChild(li);
  });
}

function adicionarUsuario() {
  const nome = document.getElementById("nome").value.trim();
  const email = document.getElementById("email").value.trim();
  if (nome && email) {
    usuarios.push({ nome, email });
    document.getElementById("nome").value = "";
    document.getElementById("email").value = "";
    renderizar();
  }
}

function removerUsuario(i) {
  usuarios.splice(i, 1);
  renderizar();
}
