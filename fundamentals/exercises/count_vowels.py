# Write a function that counts how many vowels there are in a string (a, e, i, o, u)

def count_vowels(text: str) -> int:
    vowels = 'aeiou'
    text = text.lower()
    return sum(text.count(v) for v in vowels)

user_input = input('Write a string: ')
res = count_vowels(user_input)
print(res)