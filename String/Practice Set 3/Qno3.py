#Find and replace double spaces.

myStr = "My  name  is  Niraj  Paudel."
print(myStr.find("  ")) #It finds double space.
print(myStr.replace("  "," "))  #It finds and replaces all double spaces with single space.
b=myStr[myStr.find('Niraj'):19]

