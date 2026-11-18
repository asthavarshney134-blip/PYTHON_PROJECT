print("=================================================")
entry = "Number Guessing"
print(entry.center(50))
print("=================================================")
n = input("Enter your name: ")
def game():
    import random 
    number = random.randint(1,100)
    # number = 67
    g = int(input("Enter number : "))
    print(f"{n},So let's see your guess will be right or wrong")
    attempt = 0
    while attempt<6:                        # agar attempt = 0 rkhna h toh while 6 rkhna pdega nhi toh 
        if g>(number):                      # attempt = 1 h toh while 7 rkhna hoga  nhi toh max 7 attempt nhi honge
            print("Too High!")
            g = int(input("Enter number : "))
        elif g<(number):
            print("Too Low!")
            g = int(input("Enter number : ")) 
        else:
            print("You got it") 
            break
        attempt +=1        
game()