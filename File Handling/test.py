# import time
# file = open("file.txt", "w")
# print (file.write("This is a text"))
# file.close()
# current = time.ctime()
# print(current)

with open('file.txt','r') as file:
   print(file.read())
