n = 5
i = 1
j = 1
while i <= n:
    while j <= n:
        print("*",end ='')
        j += 1
    i += 1
    j = i
    print("")