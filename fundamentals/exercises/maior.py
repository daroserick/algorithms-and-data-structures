# Crie uma função que receba uma lista de números e retorna o maior número da lista

def maior(lista):
    maior_num = lista[0] # Assume que o primeiro número é maior
    for n in lista:
        if n > maior_num:
            maior_num = n
    return maior_num

numeros = []
num_digitados = int(input('Quantos números você quer digitar? '))

for i in range(num_digitados):
    numero = float(input(f'Digite o {i+1}° número: '))
    numeros.append(numero)

resultado = maior(numeros)
print(f'O maior número digitado é: {resultado}')

