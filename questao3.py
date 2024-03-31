def receber_notas():
    notas = []
    while True:
        try:
            nota = float(input("Digite a nota do aluno (ou digite -1 para encerrar): "))
            if nota == -1:
                break
            elif nota < 0 or nota > 10:
                print("Por favor, digite uma nota válida entre 0 e 10.")
            else:
                notas.append(nota)
        except ValueError:
            print("Por favor, digite uma nota válida.")

    return notas

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return round(media, 2)

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Em recuperação"
    else:
        return "Reprovado"

def main():
    notas = receber_notas()
    if not notas:
        print("Nenhuma nota foi inserida.")
        return

    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)

    print(f"\nMédia final: {media}")
    print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()
