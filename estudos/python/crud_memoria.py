tarefas = []
proximo_id = 1

def criar_tarefa(titulo, descricao):
  global proximo_id
  tarefa = {
    'id': proximo_id,
    'titulo': titulo,
    'descricao': descricao,
    'concluida': False
  }
  tarefas.append(tarefa)
  proximo_id += 1
  return tarefa

def listar_tarefas():
  return tarefas

def atualizar_tarefa(id, titulo=None, descricao=None, concluida=None):
  for tarefa in tarefas:
    if tarefa['id'] == id:
      if titulo is not None:
        tarefa['titulo'] = titulo
      if descricao is not None:
        tarefa['descricao'] = descricao
      if concluida is not None:
        tarefa['concluida'] = concluida
      return tarefa
  return None

def deletar_tarefa(id_tarefa):
  global tarefas
  tarefas = [t for t in tarefas if t['id'] != id_tarefa]
  return True

#Testando as funções
if __name__ == "__main__":
  print("Criando tarefas...")
  criar_tarefa("Estudar Python", "Focar no CRUD")
  criar_tarefa("Ler artigo", "Ler artigo sobre APIs")

  print("\nTarefas:")
  print(listar_tarefas())

  print("\nAtualizando a primeira tarefa...")
  atualizar_tarefa(1, concluida=True)

  print("\nTarefas atualizadas:")
  print(listar_tarefas())

  print("\nDeletando a segunda tarefa...")
  deletar_tarefa(2)

  print("\nTarefas finais:")
  print(listar_tarefas())