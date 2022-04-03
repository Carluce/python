# escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considerando 

salario = int(input("digite o salario: "))
print(salario)
imposto = True

if salario > 1900 and salario < 2800:
    valor1 = salario * (7/100)
    print(f"você pegara imposto? {imposto} e no valor de R$ {valor1}")
elif salario > 2800 and salario < 3700:
    valor2 = salario * (15/100)
    print(f"você pegara imposto? {imposto} e no valor de R$ {valor2}")
elif salario > 3700 and salario < 4600:
    valor3 = salario * (22.5/100)
    print(f"você pegara imposto? {imposto} e no valor de R$ {valor3}")

