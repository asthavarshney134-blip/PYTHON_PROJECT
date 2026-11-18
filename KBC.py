welcome = "swagat haii !!! aap sabka kaun banega crorepati "
print(welcome.title())
questions = [

    ["Q1. Who created python? ", "a.Stephen ","b.Rabindranath Tagore","c.Guido Von Rossum","d.Barry Warsaw" , 3 ],
    ["Q2. The ZEn of python consist of  ? ", "a.13 lines ","b.20 lines","c.40 lines", "d.19 lines" , 2],
    ["Q3. Which of one of the following is not attribute of tuple ? ", "a.len() ","b.type()","c.slicing[]","d.append()" , 4],
    ["Q4. Which of the following can print data in unorderd way ? ", "a.tuple ","b.set","c.list","d.dictionary" , 2],
    ["Q5. Can we alter tuple ? ", "a.Yes, by converting tup to list to tup ","b.No ","c.Yes, by using append()","d.Can't say anything" , 1],
    ["Q6. PEP 8 was created by how many person ? ", "a.1","b.4 ","c.6","d.3" , 4],
    ["Q7. Finally block exceutes when ? ", "a.try exceutes ","b.except exceutes  ","c.It will always exceutes","d.else exceutes" ,3],
    ["Q8. Is comment and doc string same ? ", "a.Yes","b.No","c.Can't say anything ","d.Depends on coding", 2 ],
    ["Q9. In sets, how can we join two sets by using attribute ","a.Intersection","b.Symmetric Differenc","c.Difference", "d.Union", 4],
    ["Q10. Color = ['Red','Yellow','Pink','Blue','Green'], which of the following will not print \"Pink\" ? " , "a.color[-1:-2]","b.color[-3]","c.color[1:3]",
     "d.color[2]",1]
]

levels = ["3000","5000","7000","10000","20000","40000","320000","2500000","5000000","10000000"]
money =0
def mechanism():
    for i in range(0,len(questions)):
        question = questions[i]
        print(f"\n\nQues for Rs. {levels[i]}")
        print(f"\n{question[0]}")
        print(f"\n{question[1]}     \n{question[2]}")
        print(f"\n{question[3]}     \n{question[4]}")
        reply = int(input("Enter answer from 1-4 or Want to quit enter 0 : "  ))
        Answer =[0,1,2,3,4]
        if reply not in Answer :
            raise ValueError("Answer according to instruction")
        if (reply == 0):
            money = levels[i-1]
            break
        elif (reply == question[-1]):
            print(f"Correct Answer.. You win {levels[i]}")
            if i == 3:
                money =7000
            elif i == 6:
                money = 320000   
            elif i == 9:
                money = 10000000
                break
        else:
            print(" Wrong Answer!! \nGame Over...") 
            break
    print(f"Money you taking to your home is {money}")      
mechanism()

re = input("Want to play again ? ")
if (re!="Yes" and re!="No"):
    raise ValueError("Answer in Yes and No")
if re == "Yes":
    f = mechanism()
    print(f)
else:
    print("Bye thanks for playing...")