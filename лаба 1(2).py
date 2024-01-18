plot = [[0 for i in range(41)] for i in range(11)]
f_res = [round(i**0.711) for i in range(20, 0, -1)] + [round(i**0.711) for i in range(0, 21)]


step = 1

END = '\u001b[0m'
YEL = '\u001b[48;5;220m'
GREEN = '\u001b[48;5;22m'

for i in range(len(f_res)):
    plot[-f_res[i]-1][i] = 1
    

for i in range(len(plot)):
    line = '\t' + str((len(plot) - i - 1) * step) + '\t'
    for j in range(len(plot[0])):
        if plot[i][j] == 0:
            line += '-'  
        else:
            line += f'{YEL}{" " * 1}{END}'
    print(line)
print('\t\t-20.................0.................20')