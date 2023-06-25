mySet = {1,2,3,4,5,6,7}

s = mySet       #assigning s for my set(For easy use)


#len
print(len(s))   #print the lenght of set

#remove
s.remove(7)     #removes 7 from set if it is present in a set
print(s)

#pop
a=s.pop()         #Remove items from set randomly and returns. It doesnot takes any arguments
print("Removed item: ",a)
print("After removing:",s)

#clear
s.clear()       #It clears all the elements from the set.
print(s)

#union
s.union({5,6,7,8,9})        #{5,6,7,8,9} are the items of another set. Unions add item to the existing set from new set. Add those items which are not present
print("After union: ") 

