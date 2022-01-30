def fun(a,b):
    return a+b

def square(num):
    print('will use this as docorated function')
    return num*num

@square
def fn(ar):
    def inner(*args,**kwargs):
        return(fn(*args,**args))
    
x=fn(3)
    