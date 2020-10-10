test = ''
while test != 'quit':
    test = str(input('select add, subtract, multiply, divide, quit'))
    while test not in ['add','subtract','multiply','divide','quit']:
        test = str(input('select add, subtract, multiply, divide, quit'))
    if test == 'add':
        i=1
        result = 0
        while (i < 4):
            s = float(input('Enter number ' + str(i) + ':'))
            result = result + s
            i+= 1
            
        print ('Your answer is ' + str(result))
    elif test == 'subtract':
        i=1
        result = 0
        while i < 4 :
            s = float(input('Enter number ' + str(i) + ':'))
            if i == 1:
                result = result + s
            else: result = result - s
            i += 1
        print('Your answer is ' + str(result))
    elif test == 'multiply':
        i = 1
        result = 1
        while i < 4:
            s = float(input('Enter number ' + str(i) + ' :'))
            result = result * s
            i += 1
        print('Your answer is ' + str(result))
    elif test == 'divide':
        i = 1
        result = 0
        while i < 3:
            s = float(input('Enter number ' + str(i) + ' :'))
            if i == 1:
                result = result + s
            else: result = result / s
            i += 1
        print ('Your answer is ' + str(result))
    elif test == 'quit':
        print ('Thanks for using this calculator')
