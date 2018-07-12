import config
import calc

for i in range(config.range1[0], config.range1[1] + 1):
    for j in range(config.range2[0], config.range2[1] + 1):
        for k in calc.calc(i,j):
            print(str(i) + str(k['sign']) + str(j) + '=' + str(k['result']), end = " ")
    print()