#用for loop 解 practice_4.py 的象限判斷
A = [-1, -10]
B = [5, -5]
C = [1,1]
D = [-2, 3]
dots = [
    ['A', A],
    ['B', B],
    ['C', C],
    ['D', D]
]#把A,B,B,D四個list塞進dots這個list裡面
for i in dots:
    print(i[0], "is in", end =' ')
    if i[1][0] > 0 and i[1][1] > 0:
        print("I")
    elif i[1][0] < 0 and i[1][1] > 0:
        print("II")
    elif i[1][0] < 0 and i[1][1] < 0:
        print("III")
    elif i[1][0] > 0 and i[1][1] < 0:
        print("IV")