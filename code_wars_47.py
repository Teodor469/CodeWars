import re

def reverse_words(text):
    words = re.split(r'(\s+)', text)
    reversed_words = [word[::-1] for word in words]
    reversed_text = ''.join(reversed_words)
    return reversed_text
    
a = input()
print(reverse_words(a))