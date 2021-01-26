import re
lit = []
def encode():
    password = input('Enter what you would like to encode: ')
    key = int(input('Enter your key: '))
    for p in password:
        code = ord(p) + key
        lit.append(code)
    print('\nYour password has been encoded')
    for i in lit:
        print(i, end=':')

def decode():
    hashh = input('Enter your hash: ')
    key = int(input('Enter your key: '))
    find = re.findall('[0-9]{1,3}', hashh)
    for p in find:
        code = chr(int(p) - key)
        print(code, end='')
    print('\nYour password has been decoded')

inp = input('Hello, what would you like to do \n1. Encrypt \n2. Decrypt \n')

if inp == '1':
    encode()
elif inp == '2':
    decode()
else:
    print('invalid input, please enter 1 to encrypt or 2 to decrypt')