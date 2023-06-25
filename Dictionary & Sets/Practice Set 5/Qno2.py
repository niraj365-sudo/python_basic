#Program to input eight number from user and display all the unique number once.
mySet = set()
s = mySet

for i in range(8):
    s.add(input("Enter a number: "))

print(s)
