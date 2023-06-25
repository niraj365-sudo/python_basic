dictionary = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964

}

print(type(dictionary))
print(dictionary.items())                       #It displays the couple of keys and values using tuples.

#display keys and values
for keys, values in dictionary.items():         #Using for loop. It takes keys and values from dictionary. Item keyword is used to display both keys and values
        print(keys , "=",values)

#displaying keys only
for keys in dictionary.keys():                  #keys keyword is used to display keys
    print(keys)

#displaying values only
for values in dictionary.values():              #values keyword is used to display values.
    print(values)

#replace and update dictionary

print(dictionary.update({"update":"I am updated item","year":2022}))
print(dictionary.items())

 #get() 
print(dictionary.get('update'))         #gives output if update keyword is present in dictionary
print(dictionary.get('notpresent'))     #result none if not present in program.    

