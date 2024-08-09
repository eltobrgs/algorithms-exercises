def myfunc(*args, **kwargs):
    print("argumentos posicinais: ", args)
    print("argumentos nomeados", kwargs)


myfunc(1, 2, 3, nome="jose", idade=30)