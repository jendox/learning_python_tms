a=['abc','def','ghi','jkl','mno']
b=[str(f'{i} - {a[i]}') for i in range(len(a))]
print(b)