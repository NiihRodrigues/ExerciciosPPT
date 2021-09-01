nome = input("Insira o nome do aluno: ")

nota1 = float(input("Insira a 1° nota: \n"))
nota2 = float(input("Insira a 2° nota: \n"))
nota3 = float(input("Insira a 3° nota: \n"))
nota4 = float(input("Insira a 4° nota: \n"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\nO aluno {nome} ficou com a média {media}")
