def calculate(operation, x, y):
    '''
    operation  - takes de string [add,sub,mul,div]
    x & y  - floats
    '''
    if operation == 'Addition':
        return x + y
    elif operation == 'Subtraction':
        return abs(x - y)
    elif operation == 'Multiplication':
        return x * y
    elif operation == 'Division':
        return x / y

