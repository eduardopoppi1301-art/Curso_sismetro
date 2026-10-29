import os

os.system("cls" if os.name == "nt" else "clear")

nome = input("Digite seu nome: \n").strip()
print(f"Olá, {nome}\n")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade <= 0:
            print("Idade inválida! Você não pode ter 0 ou menos que 0 anos.\n")
        elif idade > 110:
            print("Idade inválida! Você não pode ter mais de 110 anos.\n")
        else:
            print(f"Idade informada: {idade}\n")
            break 
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.\n")

while True:
    try:
        quantidade_notas = int(input("Quantas provas você fez? "))
        if quantidade_notas <= 0:
            print("Você tem que ter feito ao menos uma prova. Digite novamente.\n")
        else:
            print(f"Você fez o total de {quantidade_notas} provas.\n")
            break
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.\n")

soma_notas = 0
contador = 1

while contador <= quantidade_notas:
    try:
        nota = float(input(f"Digite a nota da prova {contador} (0 a 100): "))

        if nota < 0 or nota > 100:
            print("Nota inválida! Digite um valor entre 0 e 100.\n")
        else:
            soma_notas += nota
            contador += 1  
    except ValueError:
        print("Entrada inválida! Por favor, digite um número (ex: 75.5).\n")

media = soma_notas / quantidade_notas

print("\n--- Resultado Final ---")
print(f"{nome}, sua média final foi: {media:.2f}")

if media >= 70.0:
    print("Parabéns, você foi aprovado!")
else:
    print("Sinto muito, você ficou de recuperação.")
