

def parent(num):
    print('Impreso desde el padre')
    def child():
        print('impreso del hijo 1')
    def child2():
        print('impreso del hijo 2')

    try:
        assert num == 10
        return child
    except AssertionError:
        return child2

foo = parent(10)
bar = parent(12)

print(foo())
print(bar())
