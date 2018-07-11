#Fibonacci number in recursive method
#for exercise2:recursive_2
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)
print('answer: ', f(20))