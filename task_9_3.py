def my_decorator(func):
    def my_wrapper(lst):
        m_ls = [i for i in lst if i%2]
        func(m_ls)
        return m_ls
    return my_wrapper

@my_decorator
def func(lst):
    for i in lst:
        print(i,end=' ')
    return

func(range(-10,83))