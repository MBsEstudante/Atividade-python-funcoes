import random

def jogar_jogo():
    numero_aleatorio = random.randint(1, 10)
    tentativas = 0
    erros = 0

    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 10: "))
            if palpite < 1 or palpite > 10:
                print("Por favor, digite um número válido entre 1 e 10.")
                continue

            tentativas += 1

            if palpite == numero_aleatorio:
                print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
                break
            elif palpite < numero_aleatorio:
                print("Seu palpite está baixo. Tente um número mais alto.")
            else:
                print("Seu palpite está alto. Tente um número mais baixo.")

        except ValueError:
            print("Por favor, digite um número válido.")

        finally:
            erros += 1

    return tentativas, erros

def relatorio(tentativas, erros):
    print("\nRelatório Final:")
    print(f"Total de tentativas: {tentativas}")
    print(f"Total de erros: {erros}")

def main():
    tentativas, erros = jogar_jogo()
    relatorio(tentativas, erros)

if __name__ == "__main__":
    main()
