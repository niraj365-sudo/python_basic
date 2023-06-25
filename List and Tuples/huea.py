with open('file.txt','w') as file:
    file.write('This is a text')
with open('file.txt','r') as file:
    print(file.read())
    
file = open('file.txt','r')
print(file.read())