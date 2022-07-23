import requests

def baseExpCompare(row1, row2):
    if row1[0] > (row2[0]**(row2[1]/row1[1])):
        return row1
    else:
        return row2

if __name__ == "__main__":
    base_exp = requests.get('https://projecteuler.net/project/resources/p099_base_exp.txt').text
    base_exp = base_exp.split('\n')
    base_exp = [[int(j) for j in i.split(',')] for i in base_exp]
    result = base_exp[0]

    for row in base_exp[1:]:
        result = baseExpCompare(result, row)
        
    print(base_exp.index(result)+1)
