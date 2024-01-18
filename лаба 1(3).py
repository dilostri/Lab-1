plot = [[0 for i in range(21)] for i in range(11)]
f_res = [abs(i) for i in range(-10, 11)]


step = 1



for i in range(len(f_res)):
    plot[-f_res[i]-1][i] = 1
    

for i in range(len(plot)):
    line = '\t' + str((len(plot) - i - 1) * step) + '\t'
    for j in range(len(plot[0])):
        if plot[i][j] == 0:
            line += '- '  
        else:
            line += '* '
    print(line)
print('\t\t9 -8 -6 -5 -4 -2 -1 0 1 2 3 4 5 6 7 8 9 10')
        