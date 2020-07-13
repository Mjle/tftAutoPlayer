import pyautogui as pyag
import time
import pygetwindow as gw
from directkeys import PressKey, ReleaseKey, FOR_SLASH, ENTER, F
import pywinauto
from datetime import datetime

imagePath = 'C:\\Users\\lemic\\Desktop\\Python\\TFT\\images\\'

# Start program
now = datetime.now()
print("Started date and time: " + now.strftime("%Y-%m-%d %H:%M:%S"))

def printTime(eventStage):
    now = datetime.now()
    print(eventStage + now.strftime("%Y-%m-%d %H:%M:%S"))

def clickFindMatch():
    find_match_btn = imagePath + 'findMatch.png'
    try:
        league = gw.getWindowsWithTitle('League of Legends')[0]
        league.activate()
    except:
        pass
    pyag.click(pyag.locateOnScreen(find_match_btn, confidence=0.8))

def accept():
    accept_btn = imagePath + 'accept.png'
    try:
        league = gw.getWindowsWithTitle('League of Legends')[0]
        league.activate()
    except:
        pass
    pyag.click(pyag.locateOnScreen(accept_btn, confidence=0.8))

def ok():
    ok_btn = imagePath + 'ok.png'
    try:
        league = gw.getWindowsWithTitle('League of Legends')[0]
        league.activate()
    except:
        pass
    pyag.click(pyag.locateOnScreen(ok_btn, confidence=0.8))

def attemptSurrender():
    try:
        league = gw.getWindowsWithTitle('League of Legends (TM) Client')[0]
        league.activate()
    except:
        pass
    if pyag.locateOnScreen(imagePath+'3.1.png', confidence=0.9) is not None:
        printTime('Found 3.1 at')
        ff()
    elif pyag.locateOnScreen(imagePath+'3.2.png', confidence=0.9) is not None:
        printTime('Found 3.2 at')
        ff()
    elif pyag.locateOnScreen(imagePath + '3.3.png', confidence=0.9) is not None:
        printTime('Found 3.3 at')
        ff()
    elif pyag.locateOnScreen(imagePath + '3.5.png', confidence=0.9) is not None:
        printTime('Found 3.5 at')
        ff()
    elif pyag.locateOnScreen(imagePath + '3.6.png', confidence=0.9) is not None:
        printTime('Found 3.6 at')
        ff()
    elif pyag.locateOnScreen(imagePath + '4.3.png', confidence=0.9) is not None:
        printTime('Found 4.3 at')
        ff()
    elif pyag.locateOnScreen(imagePath + '4.5.png', confidence=0.9) is not None:
        printTime('Found 4.5 at' + now.strftime("%Y-%m-%d %H:%M:%S"))
        ff()
    elif pyag.locateOnScreen(imagePath + '4.6.png', confidence=0.9) is not None:
        printTime('Found 4.6 at')
        ff()

def ff():
    printTime('FFing at')
    try:
        league = gw.getWindowsWithTitle('League of Legends (TM) Client')[0]
        league.activate()
    except:
        pass
    PressKey(ENTER)
    time.sleep(0.5)
    ReleaseKey(ENTER)
    time.sleep(0.5)
    PressKey(FOR_SLASH)
    time.sleep(0.5)
    ReleaseKey(FOR_SLASH)
    time.sleep(0.5)
    PressKey(F)
    time.sleep(0.5)
    ReleaseKey(F)
    time.sleep(0.5)
    PressKey(F)
    time.sleep(0.5)
    ReleaseKey(F)
    time.sleep(0.5)
    PressKey(ENTER)
    time.sleep(0.5)
    ReleaseKey(ENTER)
    time.sleep(3)
    try:
        xS,yS,aS,bS = pyag.locateOnScreen(imagePath + 'surrenderIG.png', confidence=0.8)
        time.sleep(2)
        pywinauto.mouse.double_click(button='left', coords=(xS,yS))
        time.sleep(1)
        pywinauto.mouse.double_click(button='left', coords=(xS,yS))
        time.sleep(1)
        pywinauto.mouse.double_click(button='left', coords=(xS,yS))
    except:
        pass


def playAgain():
    try:
        league = gw.getWindowsWithTitle('League of Legends')[0]
        league.activate()
    except:
        pass
    pyag.click(pyag.locateOnScreen(imagePath + 'playAgain.png', confidence=0.7))

'''
Iterate through different screens to carry out functions
'''
while True:
    if pyag.locateOnScreen(imagePath+'tftLobby.png') is not None:
        printTime('In lobby: ')
        clickFindMatch()
        accept()
        time.sleep(2)
    elif pyag.locateOnScreen(imagePath + 'tftLobby.png') is None:
        printTime("In-game or not in lobby: ")
        accept()
        attemptSurrender()
        playAgain()
        time.sleep(10)