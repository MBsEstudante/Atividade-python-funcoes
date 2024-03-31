def receber_dados(nome, telefone):
    return nome, telefone

def menu():
    print("Bem-vindo ao sistema de registro de contatos!")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    return receber_dados(nome, telefone)

def main():
    nome, telefone = menu()
    print(f"Nome: {nome}\nTelefone: {telefone}")

if __name__ == "__main__":
    main()
