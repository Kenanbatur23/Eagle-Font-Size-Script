from pyautogui import write
from pyautogui import press
from pyautogui import hotkey
from time import sleep
print("welcome to the eagle script code for font setting")
print("IMPORTANT: you must write '>' on command line of eagle ")
size= input("what size should fonts on pcb be : ")
print("click where the eagle window is, script is going to start in 5 seconds...")
sleep(5)#
hotkey("ctrl","a")
hotkey("ctrl","c")

write("group all;")
press("enter")

write("smash (C")
hotkey("ctrl","v")
write("0 0);")
press("enter")

write("display none tname bname tval bval;")
press("enter")

write("group all;")
press("enter")

write("change font vector (C")
hotkey("ctrl","v")
write("0 0);")
press("enter")

write(f"change size {size}mil (C")
hotkey("ctrl","v")
write("0 0);")
press("enter")

write("change ratio 15 (C")
hotkey("ctrl","v")
write("0 0);")
press("enter")

write("display last;")
press("enter")
sleep(0.5)