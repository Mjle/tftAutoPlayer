import pyautogui as pyag
import datetime
import tkinter as tk
import glob, os
import time, msvcrt
import keyboard 
import sys
import threading as th
import ctypes

# Global variables
imagePath = 'C:\\Users\\lemic\\Desktop\\Python\\TFT\\buyImages\\'
inGame = False
auto = True
sellButton = 'h'
buyList = []
totalChampList = []
        
def populateChampList():
    os.chdir(r"C:\Users\lemic\Desktop\Python\TFT\buyImages")
    for champ in glob.glob("*.png"):
        champName = champ.split('.')[0]
        totalChampList.append(champName)

def cybersList():
    global buyList
    buyList = ['Fiora','Irelia','Lucian','Graves','Vi','Leona',
            'Ekko', 'Kayle', 'MissFortune','Darius']

# Function to buy champs given X,Y
def buyChamp(champName):
    imageLoc = imagePath + champName + '.png'
    try:
        champLocX, champLocY = pyag.center(pyag.locateOnScreen(imageLoc, confidence=0.7))
    except:
        return False
    pyag.moveTo(200,200)
    pyag.click()
    pyag.moveTo(champLocX,champLocY)
    pyag.mouseDown()
    pyag.moveTo(950,650)
    pyag.mouseUp()
    time.sleep(0.5)
    pyag.click(button='left', clicks=2, interval=0.5)

def addChampToList(champName):
    if champName not in buyList:
        buyList.append(champName)
        print(buyList)
        return True
    
def removeChampFromList(champName):
    try:
        buyList.remove(champName)
    except: 
        print('Champ not on list')

# Function to buy champs given X, Y
def sellChamp(x,y):
    pyag.moveTo(x,y, duration=1, tween=pyag.easeInOutQuad)
    pyag.click()
    pyag.press(sellButton)
    
# Create GUI
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
entry1 = tk.Entry (root) 
canvas1.create_window(100, 140, window=entry1)

# Temporary to buy champs via user input
def getUserBuyInput():
    champ = entry1.get()
    canvas1.itemconfig(lbl1, text='Bought')
    
button1 = tk.Button(text='Buy champ', command = getUserBuyInput)
canvas1.create_window(100,180, window=button1)

def getUserAddListInput():
    champ = entry1.get()
    if champ in totalChampList:
        addChampToList(champ)
        canvas1.itemconfig(lbl1, text="Added")
        updateList()
    
button2 = tk.Button(text='Add champ', command = getUserAddListInput)
canvas1.create_window(100,230, window=button2)

def getUserRemoveListInput():
    champ = entry1.get()
    removeChampFromList(champ)
    canvas1.itemconfig(lbl1, text="Removed")
    updateList()
    
def updateList():
    buyListToStr = ','.join(buyList)
    canvas1.itemconfig(champTxtLbl, text=buyListToStr)
    return buyListToStr

def key_capture_thread():
    global auto
    a = keyboard.read_key()
    if a== "s":
        auto = False

def autoBuy():
    global auto
    auto = True
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    pyag.moveTo(500,500)
    pyag.click()
    while auto:
        for champ in buyList:
            buyChamp(champ)
        print('entering sleep')
        time.sleep(1)
    print('Exit')
            
            
button3 = tk.Button(text='Remove champ', command = getUserRemoveListInput)
canvas1.create_window(100,280, window=button3)

autoBuyBtn = tk.Button(text='AutoBuy', command = autoBuy)
canvas1.create_window(230,230, window=autoBuyBtn)

lbl1 = canvas1.create_text(50,100, text="Welcome", anchor="nw")
champLbl = canvas1.create_text(200,100, text="Champ List", anchor="nw")
champTxtLbl = canvas1.create_text(200,130, text="[]", width=150, anchor="nw")
cybersList()
populateChampList()

canvas1.pack()
root.mainloop()












































