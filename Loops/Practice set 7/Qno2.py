#Program to greet all the person names stored in a list l1 and which starts with s

l1 = ['Sam','Sita','Rahul','Rohan','Ravi']
for items in l1:
    if items.startswith('S'):
        print(f"Good morning {items}")