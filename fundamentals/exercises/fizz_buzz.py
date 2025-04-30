# Imprima os números de 1 a 50. Para múltiplos de 3, imprima "Fizz", para múltiplos de 5, "Buzz" e para ambos "FizzBuzz"

# Print the numbers from 1 to 50. For multiples of 3, print "Fizz", for multiples of 5, "Buzz" and for both "FizzBuzz"

def fizz_buzz() -> None:
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

print(fizz_buzz())