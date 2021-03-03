n = int(input('Number of invited guests: '))
if n < 20:
    print('Home')
elif n >=20 and n <= 50:
    print('Caffe')
else:
    print('Restaurant')
