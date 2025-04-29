# Escreva uma função que recebe um número inteiro e retorna True se ele for primo, e False caso contrário

def is_prime(n: int) -> bool:
    if n <=1:
        return False # Números menores ou iguais a 1 não são primos
    
    for i in range(2, n):
        if n % i == 0:
            return False # Se for divisível por algum número entre 2 e n-1, não é primo
    return True # Se passou pelo loop sem divisores, é primo

numero = int(input('Digite um número: '))
if is_prime(numero):
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')