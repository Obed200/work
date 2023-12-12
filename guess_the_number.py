import random
limit=int(input("Enter a number limit\n"))
def generate_random_number():
    name=input("Enter the player_name\n")
    print(f"The player name is: {name}")
    print("Guess the number\n")
    print("______________________________")
def take_user_guess():
    print(f"The numbers are ranged from {1} to {limit}\n")
def check_user(random_number,user_guess,wins):
    tries=5
    count=1
    random_number=random.randint(1,limit)
    while count<=tries:
        user_guess=int(input("Your guesses:"))
        if random_number<user_guess:
            print("Too high")
        elif random_number>user_guess:
            print("Too low")
        elif random_number==user_guess:
            print(f"congratulations You guessed! with {count} Trials") 
            wins +=1
            print(f"You have won {wins} games")
            return wins
        count +=1     
    else:
        print(f"sorry, You ran out of trials,the number was:{random_number}")    
        
def main():
    generate_random_number()
    wins =0
    random_number=0
    user_guess=0
    again="y"     
    while again.lower()=="y":
       take_user_guess()
       check_user(random_number,user_guess,wins)
       again=input("would you like to play again?(y/n)")
       print()
    print ("Bye!")
if __name__ == "__main__":
    main()                          