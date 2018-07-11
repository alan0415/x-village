#compare number a and b
a = 3
b = 2
def f(i, j):
    if i > j:
        result = ('a > b')
        return result
    elif i == j:
        result = ('a = b')
        return result
    else:
        result = ('a < b')
        return result
print(f(a,b))