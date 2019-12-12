import re
from collections import Counter

words = sorted(Counter(re.findall(r'[a-z]+\'?[a-z]*', open('Book.txt').read().lower())).items())
with open('result.txt', 'w') as f:
    for k, v in words: f.write(f'{k} {v} times\n')
