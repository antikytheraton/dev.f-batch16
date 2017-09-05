def my_decorator(some_function):
    def wrapper():
        print("Algo esta pasando antes de 'some_function'")
        some_function()
        print("Algo esta pasando despues de 'some_function'")
    return wrapper
