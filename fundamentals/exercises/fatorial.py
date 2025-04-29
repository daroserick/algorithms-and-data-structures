# Crie uma função que recebe um número e retorna o fatorial deste número

def fatorial(a):
    resultado = 1
    for i in range(1, a + 1):
        resultado *=i # Multiplica pelo valor atual de i
    return resultado

a = int(input('Digite um número: ')) # Recebe o número do usuário
resultado = fatorial(a) # Armazena o número na função
print(f'O fatorial de {a} é {resultado}')