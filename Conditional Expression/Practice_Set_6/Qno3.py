a = 'make a lot of money'
b = 'buy now'
c = 'subscribe this'
d = 'click this'

email  = input("Enter a mail: ").lower()
spam = False

if a in email:
    spam = True

if b in email:
    spam = True

if c in email:
    spam = True

if d in email:
    spam = True

print("Spam is",spam)