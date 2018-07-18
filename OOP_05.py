def div(a, b):
    if b == 0:
        raise ValueError("divisor cannot be zero!")
    else: return a/b

num = div(1, 0)
print(num)