import requests
import itertools

def passcodeCheck(passcode):
    for i in keylogs:
        for j in range(3):
            for k in range(j, 3):
                if passcode.index(i[j]) > passcode.index(i[k]):
                    return False
                
    return True

if __name__ == "__main__":
    keylogs = requests.get('https://projecteuler.net/project/resources/p079_keylog.txt').text
    keylogs = keylogs.split('\n')
    keylogs = keylogs[:-1]
    keylogs = list(set(keylogs))
    digits = ''.join(set(''.join(keylogs)))
    passcodes = [''.join(i) for i in itertools.permutations(digits)]
    print([i for i in passcodes if passcodeCheck(i)])
