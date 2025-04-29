# Escreva uma função que recebe 2 números e retorna a soma deles

def soma(a, b):
    return a + b

numeros = []
for i in range(2):
    numero = float(input(f'Digite o {i+1}° número: '))
    numeros.append(numero)

resultado = soma(numeros[0], numeros[1])
print(f'O resultado da soma dos números é: {resultado}')