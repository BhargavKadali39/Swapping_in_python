
def type1():
    x,y=10,20
    print('Type 1')
    x = x + y
    y = x - y
    x = x - y
    print('x: {0} y: {1}\n'.format(x,y))
    print('------------------')


def type2():
    x,y=10,20
    print('Type 2')
    x = x * y
    y = x / y
    x = x / y
    print('x: {0} y: {1}\n'.format(x,y))
    print('------------------')


def type3():
    x,y=10,20
    print('Type 3')
    x = (x & y) + (x | y)
    y = x + (~y) + 1
    x = x + (~y) + 1
    print('x: {0} y: {1}\n'.format(x,y))
    print('------------------')


def type4():
    x,y=10,20
    print('Type 4')
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print('x: {0} y: {1}\n'.format(x,y))
    print('------------------')


def type5():
    x,y=10,20
    print('Type 5')
    x,y = y,x
    print('x: {0} y: {1}\n'.format(x,y))
    print('------------------')

def type6():
    print('Type6')
    x,y=10,20
    x,y=y,x
    print('x: {0} y: {1}\n'.format(x,y))

type1()
type2()
type3()
type4()
type5()
type6()

