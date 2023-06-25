#Can we have a set with 18(int) and "18"(str) as a value in it?

mySet = set()
s = mySet

s.add(int(input("Enter a number: ")))           #Takes input as an int
s.add(input("Enter the same number: "))         #Takes input as an string

print(s)