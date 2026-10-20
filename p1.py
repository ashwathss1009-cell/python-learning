transactions = [
    {"id": 101, "amount": 500},
    {"id": 102, "amount": 300},
    {"id": 101, "amount": 200},
    {"id": 103, "amount": 700},
    {"id": 102, "amount": 100},
    {"id": 104, "amount": 400}
]
original = set()
duplicate = set()
print(list(enumerate(transactions)))
for i,d in enumerate(transactions):
    if d["id"] not in original:
        original.add(d["id"])
    elif d["id"] in original:
        duplicate.add(d["id"])
        
print(f"duplicate id's are {duplicate}")