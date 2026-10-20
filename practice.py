l  = [1,2,3,4,2,1,2,2]

freq = {}

for i in l:
    if i in freq.values():
        freq[i]+=1
        
    else:
        freq[i] =1

highest = max(freq.values())  

for key,value in freq.items():
    if freq[value] == highest:
        print(f"the highest frequency of {freq[key]} is {freq[value]}")