c = float(input(('enter number ')))
print(c)
match(c):
    case 1:
        print('one')
    case 1.0:
        print('one point one')
    case 2.1:
        print('two point one')
    case _:
        print('none')
