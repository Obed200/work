
print("__________________1_______________")
def func(a):
    global x
    x=input('enter text: ')
    print('Welcome to PSWAfrica '+x)
func(' ')
print(f'{x} Welcome to PWSAfrica ')
print("__________________2_______________")
y=float(input('enter any number: '))
def num():
    print(f'the square of {y} is: ',y**2)
num()
print("__________________3_______________")
def tel():
    vb=input('enter any text: ')
    print(vb+' '+vb,'\n')
    print(vb*2)
tel()
print("__________________4_______________")
def fan():
    global m
    m=input('enter a text: ')
    for i in range(10):
        print(i,m)
fan()
print("__________________5_______________")
def bd(day):
    q=input('enter your name: ')
    print(day+q)
bd('happy birth day to you ')