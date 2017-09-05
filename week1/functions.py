

def suma_de_n(*args,**kwargs):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

print(suma_de_n(*[1,2,3,4,5,5,7,7]))

def suma_de_p(*args, **kwargs):
    resultado = 0
    for k,v in kwargs.items():
        resultado += v
    if kwargs.get('uno', ''):
        return resultado

print(suma_de_p(uno=1, dos=2, tres=3))
