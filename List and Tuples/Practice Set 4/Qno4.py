#Program to sum the numbers of a list

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))
n4 = int(input("Enter number: "))
n5 = int(input("Enter number: "))
n6 = int(input("Enter number: "))
 
number = [n1,n2,n3,n4,n5,n6]
sum = number[0]+number[1]+number[2]+number[3]+number[4]+number[5]
print(sum)

#Another option
sum = 0
sum += number[0]
sum += number[1]
sum += number[2]
sum += number[3]
sum += number[4]
sum += number[5]
print(sum)