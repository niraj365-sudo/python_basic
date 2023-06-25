#Program to find the sum of natural number till n

n = int(input("Enter a number: "))
sum = 0
for i in range(n+1):
    sum = sum+i #sum += i
print(sum)

