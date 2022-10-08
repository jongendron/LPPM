# Parameter positioning in a function definition are important
# i.e. keyword arguments mark the end of positional-or-keyword arguments
# More info: https://docs.python.org/3/glossary.html#term-parameter
def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2)) # positional parameters
    print("var-positional (*args):..{}".format(args)) # args tupple of variable arguments
    print("keyword:.................{}".format(k)) # keyword argument k (ends args parameter)
    print("var-keyword:.............{}".format(kwargs)) #


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)