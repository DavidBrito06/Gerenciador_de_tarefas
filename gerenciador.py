def adicionar_tarefa(tarefas,nome_tarefa):
  #tarefa: nome da tarefa a ser adicionada
  # completa: se a tarefa está completa ou não
  tarefa = {
    "tarefa": nome_tarefa,
    "completa": False
  }
  tarefas.append(tarefa) # adiciona a tarefa à lista de tarefas
  print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
  return

def ver_tarefas(tarefas):
  print("Lista de tarefas:")
  for indice, tarefa in enumerate(tarefas):
    status = "Completa" if tarefa["completa"] else "Incompleta"
    nome_tarefa = tarefa["tarefa"]
    # imprime o índice, nome da tarefa e status (completa ou incompleta)
    print(f"{indice + 1}. {nome_tarefa} - {status}")
  return

def atualizar_nome_tarefa(tarefas,indice_tarefa,novo_nome_tarefa):
  indice_ajustado = int(indice_tarefa) - 1
  if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
   tarefas[indice_ajustado]["tarefa"] = novo_nome_tarefa # atualiza o nome da tarefa
   print(f"Tarefa '{novo_nome_tarefa}' atualizada com sucesso!")
  else:
    print("Índice inválido. Tarefa não encontrada.")
  return

def completar_tarefa(tarefas,indice_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  tarefas[indice_tarefa_ajustado]["completa"] = True # marca a tarefa como completa
  print(f"Tarefa {indice_tarefa} completada com sucesso!")
  return

def remover_tarefas_completadas(tarefas):
  print("Tarefas completadas removidas com sucesso!")
  for tarefa in tarefas:
    if tarefa["completa"]:
      tarefas.remove(tarefa)
  return

tarefas = []

while True:
  print("\n Menu o gerenciador de lista de tarefas")
  print("1 - Adicionar tarefa")
  print("2 - Ver tarefas")
  print("3 - Atualizar tarefa")
  print("4 - Completar tarefa")
  print("5 - Remover tarefas completadas")
  print("6 - Sair")

  escolha = input("Digite a sua escolha: ")
  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)

  elif escolha == "2":
    ver_tarefas(tarefas)

  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
    novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)

  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
    completar_tarefa(tarefas, indice_tarefa)
    

  elif escolha == "5":
    remover_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)
    
  elif escolha == "6":
    break

print("Fim do programa")