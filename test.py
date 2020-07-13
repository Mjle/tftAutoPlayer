import pyautogui as pyag
import time

pyag.moveTo(200,200)
pyag.click()
pyag.moveTo(948,1002)
pyag.mouseDown()
pyag.moveTo(950,650)
pyag.mouseUp()
time.sleep(0.5)
pyag.click(button='left', clicks=2, interval=0.5)