print("=================================================")
entry = "Snake Water Gun"
print(entry.center(50))
print("=================================================")
n = input("Enter your name: ")
print(f"{n},So let's see some rules first about game")
print(" This is game between two player....")
r = ["Rules:","1. Snake beats Water","2. Water beats Gun","3. Gun beats Snake","4. Snake - S","5. Water - W","6. Gun - G"]
for i in r:
    print(i)
print("Time Start Game!!!") 
def game():   
    p1 = input("Enter S & W & G : ")
    print(f"Selected by player1 : {p1}")
    import random
    p2 = ["S","W","G"]
    choices = random.choice(p2) 
    # choices = input("Enter :")
    print(f"Selected by player2 : {choices}")
# if p1 == "S" and choices == "W":                        # method1
#     print("p1 wins") 
    winning = [("S","W"),("W","G"),("G","S")]
    draw = [("S","S"),("W","W"),("G","G")]
    if (p1,choices) in winning:
        print("p1 wins")
    elif (p1,choices) in draw:
        print("Game will start Again...")
        return game()    
    else:
        print("p2 wins")    

game()
print("Want to play again ? ")
e = input("Enter : ")
if e == "yes":
    g = game()
    print(g)
else:
    print("Bye...See You Again")