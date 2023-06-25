myList = []
a=0
flag = True
i = len(myList)
while(flag):
    b = int(input("Enter a number: "))
    if(myList.count(b) == 1):
        print("Included")
    
    elif(myList.count(b) == 0):
        myList.append(b)
        print("Added")
        print(myList)

    else:
        myList.remove(b)
    z = input("Do you want to continue: ")
    if(z == 'n'):
        flag = False



