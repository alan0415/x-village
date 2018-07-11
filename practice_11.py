def maker(n):
    def action(x):
        return n ** x
    return action
a = input("Enter a: ")#a為底數
a = int(a)
b = input("Enter b: ")#b為次方數
b = int(b)

f = maker(a)
print(f(b))
