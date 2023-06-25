a="Niraj"

print(a[0]) #Print string of index 0
print(a[1]) #Print string of index 1
print(a[2]) #Print string of index 2
print(a[3])
print(a[4])
print(a)

#String from to
#example: print(a[0:3])     It prints from index 0 to index 2 not of last index

print(a[0:1])
print(a[0:2])
print(a[0:3])
print(a[0:4])
print(a[0:5])

#String Skipping
#example: print(word[3:8:2])  It will print from index 3 to index 7 by skipping a character

word = "AMAZING"
print(word[2:7:1])  #1 will not skip a character
print(word[2:7:2])  #2 will  skip 1 character

#Advance String Skipping 

print(word[:7]) #Here we skipped first starting index. It will start to print from starting to index 6
print(word[0:]) #Here we skipped last index. It will start from 0(can be any starting value) and goes up to end
print(word[::2])    #This will goes from index 0 to last index of word by skipping 1 index

#Reverse String Skipping

print(word[::-1])   #It reverses the string. If the starting index and ending index is positive, But skipping argument is in negative it revert the string
print(word[::-2])   #It reverses the string and skips 1 character.