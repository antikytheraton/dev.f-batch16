import os
import datetime
import math

# NOTE: datetime, math and os
path = os.getcwd()
print(os.path.join(path,'statuc'))

print(datetime.datetime.now())

fecha = datetime.datetime(1999,4,16)
print(fecha)
fecha1 = datetime.datetime.strptime('1990-08-12','%Y-%m-%d')
print(fecha1)


# var_a = input('num1: ')
# var_b = input('num2: ')
#
# print(int(var_a) + int(var_b))

# NOTE: split() y join()

lista_letras = "nsbdf sdf sd fsd a fdffsg".split()
print(lista_letras)
lista_letras.append("holi")
print(lista_letras)
nombre = " ".join(lista_letras)
print(nombre)


# NOTE: zip()

tupla1=('a','b','c','d')
tupla2=('e','f','g','h')
nueva_tupla = zip(tupla1,tupla2)
print(list(nueva_tupla))
