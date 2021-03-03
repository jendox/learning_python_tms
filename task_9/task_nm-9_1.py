from datetime import datetime

def my_dec(func):
    def my_wrap(*x):
        print('Function arguments:',end=' ')
        for i in x:
            print(i,end=' ')
        time = datetime.now()
        func(*x)
        time = datetime.now() - time
        print(f'Function running: {time}')
    return my_wrap

@my_dec
def func(*x):
    for j in range(100000000):
        j = j
    return

func(1,3,5,8,9,2,1,5,7,4)