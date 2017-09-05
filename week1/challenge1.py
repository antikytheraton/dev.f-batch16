lista = [1,2,3,4,5,6,7,8,9,0]
i = 3
y = (lista.index(i)) if i in lista else 'no esta'
print('I find the %i in the position %X' % (i, y))
