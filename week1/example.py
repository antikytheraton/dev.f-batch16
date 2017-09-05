'''
lista = list(range(0,7))

var = 6
print(var in lista)

lista.insert(1,7)
# print(lista[0::2])
print(lista)
print(lista[::-1])
print(lista.reverse())
print(lista)
'''

'''
tuplas
'''

tuplas = (
    ['lunes',1],
    ('martes',2),
    ('miercoles',3)
)
# tuplas[0][1] = 2

# print(tuplas)

'''
dicionarios
'''
# dic = dict(tuplas)
# print(dic['lunes'])
#
#
dict2 = {
    'nombre':'Aaron',
    'edad':27,
    'gustos':['programar','leer','caminar']
}
# print(dict2)
dict2.update({'aficiones':[1,2,3,4,5]})
# print(dict2)


for key,value in dict2.items():
    string = 'La llave %s tiene el valor %s' % (key,value)
    print(string)
