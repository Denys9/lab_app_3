try:
    num = int(input('Введіть перше число - '))
    print(f'!{num}=', end='')
    temp = 1
    for item in range (1, num+1):
        if item == num:
            print(item,end = '')
        else:
            print(f'{item}*',end = '')
        temp*=item
    print(f' = {temp}')
except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('Exit')