import pyautogui
import tkinter as tk
import datetime

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 150)
canvas1.pack()


# Start program
now = datetime.datetime.now()
print("Start program date and time: " + now.strftime("%Y-%m-%d %H:%M:%S"))


def takeScreenshot ():
    
    myScreenshot = pyautogui.screenshot(region=(480,930,185,140)) # 931, 1070 is consistent
    myScreenshot.save(r'C:\Users\lemic\Desktop\Python\TFT\images\image1.png')

def takeScreenshot1 ():
    
    myScreenshot = pyautogui.screenshot(region=(680,930,185,140))
    myScreenshot.save(r'C:\Users\lemic\Desktop\Python\TFT\images\image2.png')

def takeScreenshot2 ():
    
    myScreenshot = pyautogui.screenshot(region=(885,930,185,140))
    myScreenshot.save(r'C:\Users\lemic\Desktop\Python\TFT\images\image3.png')
    
def takeScreenshot3 ():
    
    myScreenshot = pyautogui.screenshot(region=(1085,930,185,140))
    myScreenshot.save(r'C:\Users\lemic\Desktop\Python\TFT\images\image4.png')
    
def takeScreenshot4 ():
    
    myScreenshot = pyautogui.screenshot(region=(1285,930,185,140))
    myScreenshot.save(r'C:\Users\lemic\Desktop\Python\TFT\images\image5.png')
    
def mouseCoords ():
    
    currentMouseX, currentMouseY = pyautogui.position()
    mousePosition = ("Current mouse position: " + str(currentMouseX) + " " + str(currentMouseY))
    canvas1.itemconfig(lbl1, text=mousePosition)
    root.after(1000, mouseCoords)
    
lbl1 = canvas1.create_text(50, 100, text="hi", anchor="nw")
    
myButton = tk.Button(text='1', command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(50, 50, window=myButton)

myButton1 = tk.Button(text='2', command=takeScreenshot1, bg='green',fg='white',font= 10)
canvas1.create_window(100, 50, window=myButton1)

myButton2 = tk.Button(text='3', command=takeScreenshot2, bg='green',fg='white',font= 10)
canvas1.create_window(150, 50, window=myButton2)

myButton3 = tk.Button(text='4', command=takeScreenshot3, bg='green',fg='white',font= 10)
canvas1.create_window(200, 50, window=myButton3)

myButton4 = tk.Button(text='5', command=takeScreenshot4, bg='green',fg='white',font= 10)
canvas1.create_window(250, 50, window=myButton4)

mouseCoords()
root.mainloop()

