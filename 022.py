import requests

data = requests.get('https://projecteuler.net/project/resources/p022_names.txt').text
names = data.split('","')
names[0] = names[0].replace('"', '')
names[-1] = names[-1].replace('"', '')
names.sort()
count = 0
temp = 0

for i in range(0, len(names)):
    temp = 0
    for j in range(0, len(names[i])):
        temp = temp + ord(names[i][j]) - ord('A') + 1
    count += (i + 1) * temp

print(count)
