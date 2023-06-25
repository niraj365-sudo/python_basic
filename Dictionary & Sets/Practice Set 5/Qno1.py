#making a dictionary 

myDict = {
    "Apple":"a fruit",
    "Cat" : "an animal",
    "Parrot" : "a bird",
    "Dog" : "an animal",
    "Spider" : "an insect"

}

d = myDict

keys = input("Enter a keyword: ")
print(keys+ " is "+d.get(keys))