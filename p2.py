students = [
    {"name": "Rahul", "marks": 85, "age": 20},
    {"name": "Asha", "marks": 92, "age": 19},
    {"name": "Kiran", "marks": 85, "age": 18},
    {"name": "Priya", "marks": 92, "age": 21},
    {"name": "Arun", "marks": 85, "age": 19}
]

sorted_students = sorted(
    students,
    key = lambda student:(-student["marks"],student["age"]))
# Here key is to tell for which value we need to sort
# - indicates we need to sort lowest to highest (-92 and -85 so -92 is lesser than -85) generally it sort from lowest t highest 

print("name", "marks", "age")   
for i,dict in enumerate(sorted_students):
    
    print(dict["name"],dict["marks"],dict["age"])
    
    print("Thank you")