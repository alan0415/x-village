a = 5
b = 3
def f(i, j):
    #print("i = ", i, "j = ",j )
    m = i
    #print("m = ", m)
    i = j
    #print("second i = ", i)
    j = m
    #print("secon j = ",j )
    result = (i, j)
    #print("Inner result =",result[0]," ", result[1])
    return result
result = f(a,b)
print("a = ", result[0], "b = ", result[1])