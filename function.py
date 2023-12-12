# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:56:13 2023

@author: USER
"""
print('______________________________________________________')
# other program

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print('______________________________________________________')
# other program
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print(x)
myfunc()

print("Python is " + x)
print('______________________________________________________')
# other program
x = frozenset({"apple", "banana", "cherry"})
print(x)
y=range(5)
print(y)
z=dict(name='fred',ange=20)
print(z)
print('______________________________________________________')
# other program
