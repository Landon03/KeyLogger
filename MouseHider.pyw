import time as t
import pyautogui as pya
import random
randomcordinate1 = (random.randint(100, 2000))
randomcordinate2 = (random.randint(100, 2000))
cordinate1 = (randomcordinate1, randomcordinate2)

while True:
	
	t.sleep(0.5)
	pya.moveTo(cordinate1, duration=0.20)