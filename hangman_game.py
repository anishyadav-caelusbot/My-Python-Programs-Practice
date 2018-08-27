from random import randint

words=['Elephant','Banglore','Umbrella','Random','Investigation']
word=words[randint(0,len(words)-1)].lower()
original=word
life=0
vw=['a','e','i','o','u']
for ch in original:
    if ch not in vw:
        word=word.replace(ch,'_')
        life+=1
print word

for x in word:
    if x=='_':
        life+=1

while True:
    inp=str(raw_input("Guess: ").lower())[0]
    if inp in original:
        vw.append(inp)
        word=original
        for ch in original:
            if ch not in vw:
                word=word.replace(ch,'_')
        print word
    else:
        life-=1
    if life==0 and word!=original:
        print "You Loose"
    elif life>0 and word==original:
        print "you win"
        break
    elif life==0 and word==original:
        print "you win"
        break
     
