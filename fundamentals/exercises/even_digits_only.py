# Dado um número inteiro positivo n, determine se todos os dígitos de n são pares

def even_digits_only(n: int) -> bool:
    for digit in str(n):
        if int(digit) % 2 != 0:
            return False
    return True
    
numero = int(input('Digite um número: '))
resultado = even_digits_only(numero)
print(resultado)