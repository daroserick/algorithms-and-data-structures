# Write a function that takes an integer and returns 'Even' if it is even and 'Odd' if it is odd

def even_or_odd(n: int) -> str:
    return 'Even' if n % 2 == 0 else 'Odd' # use of ternary if

number = int(input('Write a number: '))
result = even_or_odd(number)
print(result)