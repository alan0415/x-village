def f(a,b):
    if a > 90:
        return 8000 + b * 200
    elif a < 90 and a > 70:
        return 6000 + b * 200
    elif a < 70:
        return 4000 + b * 200
A_pay = f(55, 14)
B_pay = f(96, 13)
C_pay = f(85, 22)
print("A_pay = ",A_pay)
print("B_pay = ",B_pay)
print("C_pay = ",C_pay)