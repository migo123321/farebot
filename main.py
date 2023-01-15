# farebot
#mousbot
import time
import pyautogui as pag 
import random

while True:
    x=random.randint(600,700)
    y=random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(3)
    
