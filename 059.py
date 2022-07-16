import itertools
import requests
import pandas as pd
from bs4 import BeautifulSoup

letters = 'abcdefghijklmnopqrstuvwxyz'
cipherText = requests.get('https://projecteuler.net/project/resources/p059_cipher.txt').text
cipherText = cipherText.split(',')
cipherText = [int(i) for i in cipherText]
size = len(cipherText)

keys = [''.join(i) for i in itertools.product(letters, repeat=3)]
keys = [[ord(i) for i in j] for j in keys]
keysCycle = [itertools.cycle(i) for i in keys]
keys = [[next(i) for j in range(size)] for i in keysCycle]

decryption = [''.join([chr(cipherText[i] ^ j[i]) for i in range(size)]) for j in keys]

wikiUrl = 'https://en.wikipedia.org/wiki/Most_common_words_in_English'
wikiHtml = requests.get(wikiUrl)
wikiSoup = BeautifulSoup(wikiHtml.text, 'html.parser')
wikiTable = wikiSoup.find('table', {'class': 'wikitable'})
df = pd.read_html(str(wikiTable))
df = pd.DataFrame(df[0])
commonWords = df['Word'].tolist()

index = 0

while len(decryption) > 1:
    decryption = [i for i in decryption if commonWords[index] in i]
    index += 1

print(sum([ord(i) for i in decryption[0]]))
