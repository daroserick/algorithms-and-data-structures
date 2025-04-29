# Crie uma função que receba dois números e retorne a multiplicação deles

def multiplicacao(a, b):
    return a * b

numeros = []
for i in range(2): # A quantidade dos números para a multiplicação
    numero = float(input(f'Digite o {i+1}° número: '))
    numeros.append(numero)

# Chama a função passando os dois números a ela e armazena o resultado
resultado = multiplicacao(numeros[0], numeros[1])
print(f'O resultado da multiplicação é: {resultado}')
