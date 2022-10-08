try:
    num1 = int(input('Введіть перше число - '))
    num2 = int(input('Введіть друге число - '))
    suma = num1
    for x in range (num1, num2):
        num1+=1
        suma+=num1
    else:
        print(f'{suma}')
except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('Exit')