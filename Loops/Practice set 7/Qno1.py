#Multiplication table using loop

num = int(input("Enter a number: "))
for i in range(10):
    i += 1
    print(f"{num}*{i}={num*(i)}")   #by using f string we can insert variables inside {}

print('\n\nUsing while loop')
i=1
while(i<=10):
    print(f"{num}*{i}={num*(i)}")   #by using f string we can insert variables inside {}
    i += 1