# Escreva uma função que recebe dois números inteiros e retorna a diferença absoluta entre eles
# Diferença absoluta é a diferença entre dois números sem sinal negativo. Ou seja, a distância entre eles

def absolute_diff(a: int, b: int) -> int:
    return abs(a - b)

numeros = []
for i in range(2):
    numero = int(input(f'Digite o {i+1}° número: '))
    numeros.append(numero)

resultado = absolute_diff(numeros[0], numeros[1])
print(f'A diferença absoluta entre os números {numeros[0]} e {numeros[1]} é {resultado}')