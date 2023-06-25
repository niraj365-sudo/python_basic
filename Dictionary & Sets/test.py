myList = {}         #An empty list
l = myList

for keys , value in l.items():
    print(keys," : ",value)


print("-------------MENU-------------")
print("Enter your choice")
a=input("\n1. Insert  \n 2. Remove  \n 3. Display  \n 4. Exit")

if(a == 1):
    key=input("Enter key:")
    value=input("Enter value: ")
l.update({key:value})
for key, value in l.items():
    print(key," : ",value)