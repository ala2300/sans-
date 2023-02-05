txt = input("write your sentence : ")
x = len(txt)
y = len(set(w.lower() for w in txt))

if x>y :
    print ("some repetitive words")
else :
        print ("no repetitive words")
