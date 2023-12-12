print("______________________________________________")
def fanclub(team1,team2):
    print(team1+" APR FC",team2+" Rayon Sport ")
fanclub('ale','3:0')
fanclub('retur','0:0')
print('_____________________________________________')
def math(x,y,res,deff):
    global result ,quot
    x=int(input('enter any number:'))
    y=int(input('enter any number:')) 
    result=x+y
    res=x*y
    quot=x/y
    deff=y-x
    if y==0:
        print("error division by 0 ")
    else:
        pass
    print(f"{y}-{x}=",deff)
    print(' addition of ',x,'+',y,' is',result,'\n',"multiplication of",x,"x",y,"is",res,'\n',f"the quotient of {x}/{y} is ",quot)
math('','','',"")
num=False
if not num:
    print("result from adding local variables in function hold in global variable is ",result)
else:
    print("mistake!")