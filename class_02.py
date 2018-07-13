class Life:
    weight = '0'
    year = '0'
    money = '0'

a = Life()
print('a_weight: ',a.weight)
print('a_year: ',a.year)
print('a_money: ',a.money)
print('First_a_address: ',a)

after_a = Life()
after_a.weight = '60'
after_a.year = '20'
after_a.money = '20k'

print('After_a weight: ',after_a.weight)
print('After_a year: ',after_a.year)
print('After_a money: ',after_a.money)
print('Second_a_address: ',after_a)