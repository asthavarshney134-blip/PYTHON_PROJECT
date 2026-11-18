print("WELCOME !!!")
mess = input("Enter message : ")
words = mess.split(" ")                    # message ka splited version
coding = input("Enter 1 for coding or 2 for decoding : ")
coding = True if (coding == "1") else False

if (coding):
    import random 
    import string
    nwords = []                         # yeh new word ke liye joh code decode honge
    for word in words:
        if len(word)>=3:
            # r1 = "sfg"
            # r2 = "lko"
            r1 =''.join(random.choices(string.ascii_letters , k=3))           # yaha join ke saath lgege quote mei space nhi dena 
            r2 =''.join(random.choices(string.ascii_letters , k=3))           # nhi toh joh 3 letter un mei space ayega
            r = r1 + word[1:] + word[0] + r2
            nwords.append(r)
            
        else:
            # r = word[::-1]           # 3 se kam len valo alg print kr rha h
            # print(r) 
            nwords.append(word[::-1])  # yeh ek sang krega
    print(" ".join(nwords))   
else:
    nwords = []
    for word in words:
        if len(word)>=3:
            r = word[3:-3]
            r = r[-1] + r[:-1]
            nwords.append(r)
            
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))