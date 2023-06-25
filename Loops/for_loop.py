list = ['Apple','Ball','Cat','Dog','Egg','Fish','Gun','Hen','Ink','Jug']
i = 0

for i in range(3, 6):  #It starts from 3 to 5 will not include last index
    print(list[i])

print("\n\n")
for i in range(len(list)):      #range(start,stop,step_size)
    print(list[i])
print("\n\n")

for items in list:          #Prints all items in list
    print(items)
print("\n\n")
