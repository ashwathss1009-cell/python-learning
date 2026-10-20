def check_balance(transactions):
    balance = {}
    for i,d in enumerate(transactions):
    
        for d["user_id"] in transactions:
            if d["type"]=="credit":
                balance+=d["amount"]
            elif d["type"] =="debit":
                balance -= d["amount"]
                
    return balance
        
        
        
transactions = [
    {"id": 101, "user_id": "U1", "amount": 500,
     "category": "Food", "type": "debit"},

    {"id": 102, "user_id": "U2", "amount": 1200,
     "category": "Shopping", "type": "debit"},

    {"id": 103, "user_id": "U1", "amount": 2000,
     "category": "Salary", "type": "credit"},

    {"id": 104, "user_id": "U2", "amount": 300,
     "category": "Food", "type": "debit"},

    {"id": 101, "user_id": "U1", "amount": 500,
     "category": "Food", "type": "debit"},

    {"id": 105, "user_id": "U3", "amount": 800,
     "category": "Travel", "type": "debit"}
]

print(check_balance(transactions))