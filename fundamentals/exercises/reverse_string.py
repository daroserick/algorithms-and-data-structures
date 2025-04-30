# Given a string, return the reversed version of it

def reverse_string(s: str) -> str:
    return s[::-1]

s = input('Write a string: ')
rev = reverse_string(s)
print(rev)