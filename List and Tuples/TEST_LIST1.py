import pyttsx3
import time
myList = []
a=0
i = len(myList)
engine = pyttsx3.init() # object creation


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
y = int(input("Speed of speaking(100-200):"))
engine.setProperty('rate', y)     # setting up new voice rate


"""VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level
volume = float(input("volume: "))
sys_volume = (volume/100)
engine.setProperty('volume',sys_volume)    # setting up volume level  between 0 and 1
print(f"Your volume is {volume}")


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
a = input("Male \n Female \n")
if(a == str.startswith('m','M')):
    engine.setProperty('voice', voices[0].id)  
else:
    engine.setProperty('voice', voices[1].id)   
#st = input("Enter a text: ")

"""Program"""
flag = True
while(flag):
    b = int(input("Enter a number: "))
    if(myList.count(b) == 1):
        engine.say("Included")
        time.sleep(2)
    
    elif(myList.count(b) == 0):
        myList.append(b)
        engine.say("Added")
        time.sleep(2)
    
    else:
        myList.remove(b)
    con = input("Do you want to continue: ")
    if(con == 'n'):
        flag = False

print(myList)
engine.runAndWait()
engine.stop()