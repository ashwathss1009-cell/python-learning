name1 = list(input("Enter the name of first person :").lower())
name2 = list(input("Enter the name of second person :").lower())

for i in name1.copy():
    if i in name2:
        name1.remove(i) 
        name2.remove(i)
count = len(name1) +len(name2)


flames = ["friends","lovers","affection","marriage","enemy",'siblings']
index = 0

while len(flames)>1:
    index = (index + count-1)%len(flames)
    flames.pop(index)
    
print("your flames is",flames[0])