print("___________________________________________")
from tkinter import *

def game():
    ws.destroy()
    import app

def instr():
    ws.destroy()
    import instruction

def change_setting():
    ws.destroy()
    import chng_setting


ws = Tk()
ws.title('PythonGuides')
ws.geometry('600x500')
ws.config(bg='green')

start_game = Button(
    ws,
    width=20,
    text='Start Game',
    font=('sans-serif', 14),
    bg='#8C3232',
    fg='grey',
    command= game
)
start_game.place(x=160, y=120)

instructions = Button(
    ws,
    width=20,
    text='Instructions',
    font=('arial', 14),
    bg='#8C3232',
    fg='white',
    command=instr
)
instructions.place(x=160, y=170)


setting = Button(
    ws,
    width=20,
    text='Settings',
    font=('sans-serif', 14),
    bg='#8C3232',
    fg='white',
    command=change_setting
)
setting.place(x=160, y=220)


exit = Button(
    ws,
    width=20,
    text='Quit Game',
    font=('sans-serif', 14),
    bg='#8C3232',
    fg='white',
    command=exit
)
exit.place(x=160, y=270)


ws.mainloop()

 
from tkinter import *
import random

ws = Tk()
ws.title('PythonGuides')
ws.geometry('600x400')
ws.config(bg='#5671A6')

ranNum = random.randint(0, 10)
chance = 5
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'You won! {ranNum} is the right answer.'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is greater. You have {chance} attempt left.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {chance} attempt left.'

    disp.set(msg)


Label(
    ws,
    text='Number Guessing Game',
    font=('sans-serif', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#F27D16'
).pack(pady=(10, 0))

Entry(
    ws,
    textvariable=var,
    font=('sans-serif', 18)
).pack(pady=(50, 10))

Button(
    ws,
    text='Submit Guess',
    font=('sans-serif', 18),
    command=check_guess
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#5671A6',
    font=('sans-serif', 14)
).pack(pady=(20,0))

ws.mainloop()
 