print('________________________1_____________________')
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
result=num1+num2
print(num1,"+",num2,'=',result)
print(f"the sum of {num1} and {num2} is: {result}")
print('________________________2_____________________')
orig_str=input('enter any text: ')
rev_str=orig_str[::-1]
print(rev_str.rjust(30,' '))
print('________________________3_____________________')
num_str='45'
num_int=int(num_str)
print(type(num_int),num_int)
num_float=3.14
num_str2=str(num_float)
print(type(num_str2),num_str2)
print('________________________4_____________________')
name=input('enter your name: ')
age=int(input('enter your age: '))
txt='Hello,{}! you are {} years old. '
print(txt.format(name,age))
print(f" Hello, sir {name} you are {age} years old! ")
print('________________________5.Bonus_____________________')
original='hello albert '
a=original[0:6]
b=original[6:]
reverse=a[::-1]+b[::-1]
print(reverse)