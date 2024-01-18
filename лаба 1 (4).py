f = open('sequence1.txt')
a =[]
for i in f:
    a.append(float(i))
nech = 0
ch = 0
nech_k = 0
ch_k =0 

# ищем средннее арифметическое
for i in range(len(a)):
    if i == 0 or i%2 == 0:
        nech += a[i]
    else:
        ch += a[i]

sr_nech = abs(nech/(len(a)/2))
sr_ch = abs(ch/(len(a)/2))

# диаграмма
import matplotlib.pyplot as plt

index = [0,1]
values1 = [sr_ch, sr_nech]
plt.bar(index, values1)
plt.xticks(index,['четные позиции','нечетные позиции'])
plt.show()