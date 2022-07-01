import requests

data = requests.get('https://projecteuler.net/project/resources/p042_words.txt').text
words = data.split('","')
words[0] = words[0].replace('"', '')
words[-1] = words[-1].replace('"', '')
maxLen = len(max(words, key=len))
tri = [int(i*(i+1)/2) for i in range(1, 28)]
triWords = []

for word in words:
    wordValue = 0
    
    for letter in word:
        wordValue += ord(letter) - 64
        
    if wordValue in tri:
        triWords.append(word)
        
print(len(triWords))
