# Dado um número inteiro n, retorne o número com os dígitos invertidos

def rev_number(n: int) -> int:
    return int(str(n)[::-1])

numero = int(input('Digite um número: '))
rev = rev_number(numero)
print(rev)