
print("__________________6_______________")
x=float(input('enter base: '))
def number():
    y=int(input('enter an exponent: '))
    print(f'{x} to the power of {y} is',x**y)
number()
print("__________________7_______________")
def reversing():
    OgStr=input('enter original word: ')
    RevStr=OgStr[::-1]
    print(RevStr.rjust(30,' '))
reversing()
print("__________________8______________")
def marks():
    mark=int(input('enter your marks:'))
    if mark>100 or mark<0:
        print('you entered invalid marks your marks should be between 0 and 100 so reenter your marks!')
    elif mark>=50:
        print('Congratulations you have Passed.')
    else:
        print('Failed you are required to repeat!')
marks()
print("__________________9______________")
def vowel():
    x=input('enter the word you want: ')
    if 'a' in x:
        print(x.count('a'))
vowel()
print("__________________10______________")
def primefactor():
    x=int(input('enter 1st number:'))
    y=int(input('enter 2nd number:'))
    if (x%y==0):
        print(f'{y} is a factor of {x} and {x}/{y}=',x/y)
    elif x%y!=0:
       print(f'{y} isnot a factor of {x} and {x}/{y}=',x/y) 
    else:
       print('python can not divide by zero')     
primefactor()