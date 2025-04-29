# Escreva uma função que receba dois números inteiros e retorne a soma deles

def soma_dois_inteiros(a: int, b: int):
    return a + b

numeros =  []
for i in range(2):
    numero = int(input(f'Digite o {i+1}° número: '))
    numeros.append(numero)

resultado = soma_dois_inteiros(numeros[0], numeros[1])
print(f'A soma dos números é igual a {resultado}')