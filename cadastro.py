import os

ARQUIVO = "clientes.txt"

def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    
    with open(ARQUIVO, "a") as f:
        f.write(f"{nome},{email},{telefone}\n")
    
    print("Cliente cadastrado com sucesso!\n")

def listar_clientes():
    if not os.path.exists(ARQUIVO):
        print("Nenhum cliente cadastrado.\n")
        return
    
    with open(ARQUIVO, "r") as f:
        for linha in f:
            nome, email, telefone = linha.strip().split(",")
            print(f"Nome: {nome} | Email: {email} | Telefone: {telefone}")
    print()

def buscar_cliente():
    termo = input("Digite o nome para buscar: ").lower()
    
    if not os.path.exists(ARQUIVO):
        print("Nenhum cliente cadastrado.\n")
        return
    
    encontrado = False
    with open(ARQUIVO, "r") as f:
        for linha in f:
            nome, email, telefone = linha.strip().split(",")
            if termo in nome.lower():
                print(f"Nome: {nome} | Email: {email} | Telefone: {telefone}")
                encontrado = True
    if not encontrado:
        print("Cliente não encontrado.\n")

def menu():
    while True:
        print("\n1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Buscar Cliente")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

menu()
