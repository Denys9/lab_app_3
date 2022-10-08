try:
    num1 = int(input('Введіть перше число - '))
    num2 = int(input('Введіть друге число - '))
    suma = 0
    for x in range (num1, num2+1):

        suma+=x
    else:
        print(f'{suma}')
except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('Exit')