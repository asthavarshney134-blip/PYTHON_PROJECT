print("=============================================================")
entry ="WELCOME GUYS IN KAUN BANEGA CROREPATI BY ASTHA"
print(entry.center(60))
print("=============================================================")
print("----Hosted by Astha----")
guest = input("Enter guest name : ")
print("Our guest name is ",guest)
print("---Time to begin game----")
total = 0

def ask_question(ques,correct,prize):
    for i in ques:
        print(i)
    ans = input("Answer : ") 
    if ans==correct: 
        print ("Shii Javab")
        print("Aap jeet hai",prize)
        print("............")
        return True ,prize
    else:
        print("Glt javab")
        print("............")
        return False, 0

# QUESTION 1
status, amount = ask_question(ques = ["1. Favourite colour of Astha ? ","A. Black","B. Pink","C. Blue","D. White"],
                      correct = "A",prize = 100000)
if status ==True:
    total += amount
 
# QUESTION 2
    status ,amount= ask_question(ques = ["2. Most loved hobby of Astha ? ","A. Reading book","B. Gaming","C. Drawing","D. Dancing"] ,
                      correct = "C",prize = 200000)
    if status == True:
        total += amount

# QUESTION 3
        status , amount= ask_question(ques = ["3. In class 11th which stream she opt ? ","A. PCB","B. PCM","C. Commerce","D. PCMB"],
                      correct = "B",prize = 300000)
        if status == True:
            total += amount
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")            
print( "Winning Prize :",total)
print("=====================================")
gratitude="Thanks for coming "
print(gratitude.center(40))  
print("=====================================")