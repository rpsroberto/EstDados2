# Sistema de Gerenciamento de Tarefas

# Listas para armazenar tarefas e seus estados
tarefas = []
estados = []

# Função para adicionar uma tarefa
def adicionar_tarefa(nome):
    tarefas.append(nome)
    estados.append("pendente")
    print(f"Tarefa '{nome}' adicionada com sucesso!")

# Função para marcar uma tarefa como concluída
def marcar_concluida(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        estados[indice] = "concluída"
        print(f"Tarefa '{nome}' marcada como concluída.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

# Função para remover uma tarefa
def remover_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        tarefas.pop(indice)
        estados.pop(indice)
        print(f"Tarefa '{nome}' removida com sucesso!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f" - {tarefa} ({estados[i]})")

# Função para listar tarefas por estado
def listar_por_estado(estado):
    print(f"Tarefas {estado}s:")
    for i, tarefa in enumerate(tarefas):
        if estados[i] == estado:
            print(f" - {tarefa}")

# Função para pesquisar uma tarefa
def pesquisar_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        print(f"Tarefa '{nome}' encontrada: {estados[indice]}")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

# Menu de interação
def menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Marcar como Concluída")
        print("3. Remover Tarefa")
        print("4. Listar Todas as Tarefas")
        print("5. Listar Tarefas Pendentes")
        print("6. Listar Tarefas Concluídas")
        print("7. Pesquisar Tarefa")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            adicionar_tarefa(nome)
        elif opcao == "2":
            nome = input("Digite o nome da tarefa a ser marcada como concluída: ")
            marcar_concluida(nome)
        elif opcao == "3":
            nome = input("Digite o nome da tarefa a ser removida: ")
            remover_tarefa(nome)
        elif opcao == "4":
            listar_tarefas()
        elif opcao == "5":
            listar_por_estado("pendente")
        elif opcao == "6":
            listar_por_estado("concluída")
        elif opcao == "7":
            nome = input("Digite o nome da tarefa a ser pesquisada: ")
            pesquisar_tarefa(nome)
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    menu()
