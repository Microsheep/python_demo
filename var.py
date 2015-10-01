num1 = 1
def func1():
    print num1

def func2():
    global num1
    #num1 = 10
    print num1

def func3():
    num1 = 10
    print num1

def func4():
    global num2
    num2 = 10
    print num2

def func5():
    print num2

def func6():
    num2 = 20
    print num2

def func7():
    for i in range(5):
        for j in range(i):
            print 'inside', j
        print 'outide', i

def func8():
    for i in range(5):
        for i in range(i):
            print 'inside', i
        print 'outside', i

