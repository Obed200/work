def fan():
    global list
    result=sum(list)
    return result
user_input=input("please enter number in list sparated by space")
number=(int(num) for num in list.split())
result=fan(number)
print(number)