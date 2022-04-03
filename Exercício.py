# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado a média do aluno deve ser maior ou igual a 7.
# Estabelecer notas
# média = nota1 + nota2 + nota3 / 3 

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
média = (nota1 + nota2 + nota3) / 3 
print("Somando {:.1f}. e {:.1f} e {:.1f}, a média do aluno é {:.1f}". format(nota1, nota2, nota3, média))
if 7 > média >= 5:
    print("O aluno está em RECUPERAÇÃO.")
elif média < 5:
    print("O aluno esta REPROVADO.")
elif média >= 7:
    print("O aluno está APROVADO.")
