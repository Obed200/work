print('________________________11______________________')
def temperature():
    global s
    s=int(input('enter the temperature in celcious degree:'))
    if s>=100:
        print('very hot it\'s gases.')
    elif s<=0:
        print('so cold it\'s solid.')
    else:
        print('liquid!')
temperature()
print('________________________12______________________')
def my_fun(lists):
    #li=input('enter any text: ')
    li: list='hello','bro','where','have','been','in','weekend'
    print(lists,len(li),' elements')
my_fun(' It has ')
print('________________________13______________________') 
def my(text):
    without_vowels=''
    vowels='aeoiuAEOIU'
    for char in text:
        if char in vowels:
            without_vowels += '*'
        else:
            without_vowels += char
    return without_vowels
user_input=input('enter a word text :')
result=my(user_input)
print(f'the word {user_input} replace vowels by "*" it will look like {result}')       
print('________________________14______________________') 
def my():
    x=input('enter text:')
    vowels='aeoiuAEOIU'
    y=x
    for s in vowels:
        y=y.replace(s,"*") 
    print(y)
my()
print('__________________')
def my():
    x = input('Enter text: ')
    vowels = 'aeoiuAEOIU'
    y = x
    for char in vowels:
        y = y.replace(char, '*')
    print(f'The text {x} with vowels replaced by "*" looks like {y}')

my()
