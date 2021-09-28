
def breaky():
    print('------------------')

def type1(x,y):
    print('Type 1')
    print('resetting values')
    print('x: {0} y: {1}\n'.format(x,y))
    x = x + y
    y = x - y
    x = x - y
    print('After swapping')
    print('x: {0} y: {1}\n'.format(x,y))
    breaky()


def type2(x,y):
    print('Type 2')
    print('resetting values')
    print('x: {0} y: {1}\n'.format(x,y))
    x = x * y
    y = x / y
    x = x / y
    print('After swapping')
    print('x: {0} y: {1}\n'.format(x,y))
    breaky()


def type3(x,y):
    print('Type 3')
    print('resetting values')
    print('x: {0} y: {1}\n'.format(x,y))
    x = (x & y) + (x | y)
    y = x + (~y) + 1
    x = x + (~y) + 1
    print('After swapping')
    print('x: {0} y: {1}\n'.format(x,y))
    breaky()


def type4(x,y):
    print('Type 4')
    print('resetting values')
    print('x: {0} y: {1}\n'.format(x,y))
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print('After swapping')
    print('x: {0} y: {1}\n'.format(x,y))
    breaky()


def type5(x,y):
    print('Type 5')
    print('resetting values')
    print('x: {0} y: {1}\n'.format(x,y))
    x,y = y,x
    print('After swapping')
    print('x: {0} y: {1}\n'.format(x,y))
    breaky()


breaky()
type1(10,20)
type2(10,20)
type3(10,20)
type4(10,20)
type5(10,20)
