### section 1 ###
num = 10
def func1():
    num = 20
    print(num) 

func1() 
print(num)
'''
output:
20
10
'''



### section 2 ###
num = 10
def func2():
    global num
    print(num)

func2()
print(num)
'''
output:
10
10
'''



### section 3 ###
num = 10
def func3():
    global num
    num = 20
    print(num)

func3()
print(num)
'''
output:
20
20
'''
print(num)
