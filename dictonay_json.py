import json

word=input('enter the word')
letter=word[0]

filepath = 'E:\python works\data\data\D'+letter.upper()+'.json'
dt=open(filepath)
data_dict = json.load(dt)
A=data_dict[word]
#print(A)
meaning=A['MEANINGS']
#print(type(meaning))

Meaning1=list(meaning.values())[0]
#print(type(Meaning1))
m=Meaning1[1]
print(m)

