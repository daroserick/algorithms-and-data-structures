# Crie uma função que recebe um número e retorna se ele é par ou ímpar

def par_ou_impar(a):
    if a % 2 == 0: # Verifica se o resto da divisão por dois é zero
        return 'par'
    else:
        return 'ímpar'
    
a = float(input('Digite um número: ')) # Recebe o número do usuário
resultado = par_ou_impar(a) # Armazena o número na função
print(f'O número digitado é {resultado}')