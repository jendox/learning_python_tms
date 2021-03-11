def my_file_generator(filename):
    with open(filename,) as f:
        while True:
            l = f.readline()
            if not l:
                break
            yield l

gen_iter = my_file_generator('test.txt')
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
