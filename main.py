try:
    num1 = int(input('Введіть перше число - '))
    num2 = int(input('Введіть друге число - '))
    suma = 0
    counter = num2-num1+1
    for x in range (num1, num2+1):
        suma+=x
        avg = suma/counter

    else:
        print(f'{suma}\n{avg}')

except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('Exit')