'''import random
score=0
ques1=("what is 1+1",["a)2","b)5","c)6","d)7"],"a")
ques2=('what is 1+5',["a)2","b)5","c)6","d)7"],"c")
ques3=('what is 1+3',["a)2","b)5","c)6","d)4"],"d")
ques4=('what is 1+0',["a)1","b)5","c)6","d)7"],"a")
ques5=('what is 1+9',["a)2","b)5","c)10","d)7"],"c")
ques6=('what is 1+1',["a)2","b)5","c)6","d)7"],"a")
ques7=('what is 1+8',["a)2","b)5","c)6","d)9"],"d")
ques8=('what is 1+7',["a)2","b)8","c)6","d)7"],"b")
item=[ques1,ques2,ques3,ques4,ques5,ques6,ques7,ques8]
total_question=len(item)
print(total_question)
count=0
#question=random.choice(item)
#print(question[:2])
#print(question[2])
previous_ques=[]
while count<8:
    question=random.choice(item)
    

    print(question[:2])
    answer=input("enter the answer")
        #answer=item[2]
    if answer==question[2]:
        print("answer is correct,Go to next question")
        score+=1
        print(score)
    else:
        print("answer is incorrect")


print("Total score:",score,"out of",total_question)

'''


from pytimedinput import timedInput

def timedInput(prompt="", timeout=60, resetOnInput=True, maxLength=0, allowCharacters="", endCharacters="\x1b\n\r"):
    print("time out")
    

score=0
ques1=("what is 1+1",["a)2","b)5","c)6","d)7"],"a")
ques2=('what is 1+5',["a)2","b)5","c)6","d)7"],"c")
ques3=('what is 1+3',["a)2","b)5","c)6","d)4"],"d")
ques4=('what is 1+0',["a)1","b)5","c)6","d)7"],"a")
ques5=('what is 1+9',["a)2","b)5","c)10","d)7"],"c")
ques6=('what is 1+1',["a)2","b)5","c)6","d)7"],"a")
ques7=('what is 1+8',["a)2","b)5","c)6","d)9"],"d")
ques8=('what is 1+7',["a)2","b)8","c)6","d)7"],"b")
ques9=('what is 11+2',["a)2","b)8","c)13","d)7"],"c")
ques10=('what is 3+5',["a)2","b)8","c)8","d)7"],"c")
item=[ques1,ques2,ques3,ques4,ques5,ques6,ques7,ques8,ques9,ques10]
total_question=len(item)
print(total_question)

count=1
#question=random.choice(item)
#print(question[:2])
#print(question[2])
previous_ques=[]
#for question in item:
while count<=8:
    #print("count= ",count)
    question=random.choice(item)
    if question not in previous_ques:
        print("Question No: ",count)
        print(question[:2])
        
        #answer=input("enter the answer")
        answer, timedOut = timedInput("Enter the answer: ")
        if(timedOut):
            print("Timed out when waiting for input.")
            print("User-input so far:",answer)
        else:
            print("User-input:",answer)
                #answer=item[2]
        if answer==question[2]:
            print("answer is correct,Go to next question")
            score+=1
            print(score)
            break
        else:
            print("answer is incorrect")
    previous_ques.append(question)
    count=count+1

print("Total score:",score,"out of",count-1)
percentage=(score/(count-1))*100
if percentage>=75:
    print("won")
else:
    print("Failed")




