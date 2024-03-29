def hello_func(greeting, name ='Niraj'):
    return '{}, {} '.format(greeting,name)

print(hello_func("Hiii"))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math','art',name='niraj',age =20)