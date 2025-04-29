# Escreva uma função que retorne True se um número for par e False caso contrário

def is_even(n: int) -> bool:
    return n % 2 == 0 # Se o resto da divisão por 2 for 0, é par

numero = int(input('Digite um número: '))
if is_even(numero):
    print('O número é par.')
else:
    print('O número é ímpar.')