myListOfNumbers  = [1,6,7,3,5,3]

#Sorting
print("Sorting")     
print("Before")
print(myListOfNumbers)  #Before ascending
myListOfNumbers.sort()  #It ascends the numbers of list. It doesnot return anything it only modifies. Can't be used inside print
print("After")
print(myListOfNumbers)  #After ascending

#Reverse
print("\nReverse")
print("Before")
print(myListOfNumbers)      #Before reversing
myListOfNumbers.reverse()   #It reverse the numbers of list. It doesnot return anything it only modifies. Can't be used inside print
print("After")
print(myListOfNumbers)      #After reversing

#Append
print("\nAppend")
print("Before")
print(myListOfNumbers)      #Before appending
myListOfNumbers.append(9)   #It insert 9 on the end of original list which is at line 1.
print("After")
print(myListOfNumbers)      #After appending

#Insert
print("\nInsert")
print("Before")
print(myListOfNumbers)      #Before appending
myListOfNumbers.insert(3,8)   #It inserts 8 on index 3 of the original list.
print("After")
print(myListOfNumbers)      #After appending

#pop
print("\nPop")
print("Before")
print(myListOfNumbers)      #Before poping
myListOfNumbers.pop()   #It delete the element from end of the index of original list if nothing is specified inside pop()
print("After")
print(myListOfNumbers)      #After poping
myListOfNumbers.pop(2)  #It delete the element from given index of original list
print(myListOfNumbers)

#remove
'''
Pop deletes the data through index but remove delete the given data from list
'''
print("\nRemove")
print("Before")
print(myListOfNumbers)      #Before removing
myListOfNumbers.remove(3)   #It removes the first occurance of given data from original list
print("After")
print(myListOfNumbers)      #After removing