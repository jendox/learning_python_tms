st = input('Input string: ')

if len(st)%2:
    n = int(len(st)/2)
    print(st[n])
    if st[n] == st[0]:
        n_st = st[1:len(st)-1]
        print(n_st)
