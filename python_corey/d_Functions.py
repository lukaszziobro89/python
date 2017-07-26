def hello_function():
    print("Hello World!")


def hello_again():
    return 'Hello World, again!'


hello_function()
hello_again()
print(hello_again().upper())


def hello_name(name='you'):
    return 'Hello {}!'.format(name)


print(hello_name())
print(hello_name('Lukasz'))


def get_all_info(*args, **kwargs):
    print(args)
    print(kwargs)


get_all_info('Math', 'Art', name='Lukasz', age=28)


courses = ['Math','Art']
info = {'name': 'Lukasz', 'age': 28}


get_all_info(*courses, **info)