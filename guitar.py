import pyautogui
import tkinter as tk
from tkinter import *
from time import sleep
from subprocess import Popen, PIPE

#Point(x=482, y=77) URL
#Point(x=856, y=128) Search
#Point(x=590, y=310) Top Option



url = "https://www.ultimate-guitar.com/"

def get_track():
    app = "iTunes"

    trackname = '''
    tell application "%(app)s"
      get name of the current track 
    end tell
    ''' % {'app': app} #Get name of track and assign it to trackname variable in applescript
    proc = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True) #Get value of variable from applescript
    name, error = proc.communicate(trackname)
    name = name.strip('\n') #remove endline
    return name
def get_band():
    app = "iTunes"

    bandname = '''
    tell application "%(app)s"
      get the artist of the current track
    end tell
    ''' % {'app': app} #same but artist name instead of songname
    proc = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    artist, error = proc.communicate(bandname)
    artist = artist.strip('\n')
    return artist

def push_button_bass():
    name = get_track()
    artist = get_band()
    inst = "&page=1&type=400" 
    pyautogui.click(x=482, y=77) #Click on searchbar
    pyautogui.write(url)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(x=856, y=128) #click on searchbar in website
    pyautogui.write(name+" "+artist)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.click(x=1038, y=72) # click end of searchbar
    sleep(0.2)
    pyautogui.click(x=1038, y=72)
    pyautogui.write(inst)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.click(x=590, y=310) #click top result



def push_button_guitar():
    name = get_track()
    artist = get_band()
    artist = artist.rstrip("\n")
    pyautogui.click(x=482, y=77)
    pyautogui.write(url)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(x=856, y=128)
    pyautogui.write(name+" "+artist)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.click(x=590, y=310)

def push_button_uke():
    name = get_track()
    artist = get_band()
    artist = artist.rstrip("\n")
    inst = "&page=1&type=800"
    pyautogui.click(x=482, y=77)
    pyautogui.write(url)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(x=856, y=128)
    pyautogui.write(name+" "+artist)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.click(x=1038, y=72)
    sleep(0.2)
    pyautogui.click(x=1038, y=72)
    pyautogui.write(inst)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.click(x=590, y=310)


root = Tk()

button_bass = Button(root, text="Bass", padx=50, pady=20,command=push_button_bass)
button_guitar = Button(root, text="Guitar", padx=50, pady=20,command=push_button_guitar)
button_uke = Button(root, text="Ukulele", padx=50, pady=20,command=push_button_uke)

button_bass .grid(row=1,column=1)
button_guitar.grid(row=1,column=2)
button_uke.grid(row=1,column=3)

root.mainloop()


