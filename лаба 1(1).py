RED = '\u001b[48;5;1m'
END = '\u001b[0m'
YEL = '\u001b[48;5;220m'
GREEN = '\u001b[48;5;22m'

line = ''

for i in range(6): 
    if i == 0 or i == 1:
        print(f'{YEL}{"  " * 18}{END}')
    elif i == 2 or i == 3:
        print(f'{GREEN}{"  " * 18}{END}')
    else: 
        print(f'{RED}{"  " * 18}{END}')