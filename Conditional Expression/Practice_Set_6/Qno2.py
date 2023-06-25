a = int(input("Enter your marks: "))
b = int(input("Enter your marks: "))
c = int(input("Enter your marks: "))

total = a+b+c
per = (total/300)*100

if(per>40):
    if(a >= 33 and b >= 33 and c >= 33):
        print("You are passed.")
    else:
        print("You are fail.")
else:
    print("You are fail.")