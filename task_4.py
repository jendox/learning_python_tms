def inch_in_sm(x):
    return x * 2.54

def sm_in_inch(x):
    return x * 0.39

def mile_in_km(x):
    return x * 1.61

def km_in_mile(x):
    return x * 0.62

def lb_in_kg(x):
    return x * 0.45

def kg_in_lb(x):
    return x * 2.2

def ounce_in_gr(x):
    return x * 28.35

def gr_in_ounce(x):
    return x * 0.035

def gallons_in_litres(x):
    return x * 3.79

def litres_in_gallons(x):
    return x * 0.26

def pint_in_litres(x):
    return x * 0.47

def litres_in_pint(x):
    return x * 2.11

print('Выберите вариант перевода:')
print('1  - Дюймы в сантиметры')
print('2  - Сантиметры в дюймы')
print('3  - Мили в километры')
print('4  - Километры в мили')
print('5  - Фунты в килограммы')
print('6  - Килограммы в фунты')
print('7  - Унции в граммы')
print('8  - Граммы в унции')
print('9  - Галлоны в литры')
print('10 - Литры в галлоны')
print('11 - Пинты в литры')
print('12 - Литры в пинты')

while True:
    var = int(input())
    if var == 0:
        break
    x = float(input('Введите данные для перевода: '))
    if var == 1:
        print(inch_in_sm(x))
    elif var == 2:
        print(sm_in_inch(x))
    elif var == 3:
        print(mile_in_km(x))
    elif var == 4:
        print(km_in_mile(x))
    elif var == 5:
        print(lb_in_kg(x))
    elif var == 6:
        print(kg_in_lb(x))
    elif var == 7:
        print(ounce_in_gr(x))
    elif var == 8:
        print(gr_in_ounce(x))
    elif var == 9:
        print(gallons_in_litres(x))
    elif var == 10:
        print(litres_in_gallons(x))
    elif var == 11:
        print(pint_in_litres(x))
    elif var == 12:
        print(litres_in_pint(x))
    else:
        print('Неверный ввод')
