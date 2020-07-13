def addChampBtns(canvas):
    xpos, ypos = 150, 25
    print('before loop')
    for button_number in range(len(totalChampList)):
        champBtnName = totalChampList[button_number]
        button = tk.Button(canvas, width='5', height='2', text=champBtnName, 
                     command=addChampToList(champBtnName))
        window = canvas.create_window(xpos, ypos, window=button)
        ypos += 50
    print('after loop')
    buyList.clear()
    
addChampBtns(canvas1)
    
# def startGame():
    # if inGame:
        # break
    # else
        # imagePath = 'C:\\Users\\lemic\\Desktop\\Python\\TFT\\images\\'

# def findMatch():
    # findMatchBtn = 'C:\\Users\\lemic\\Desktop\\Python\\TFT\\images\\findMatch.png'
    # playAgainBtn = 'C:\\Users\\lemic\\Desktop\\Python\\TFT\\images\\playAgain.png'
    # lobby = 'C:\\Users\\lemic\\Desktop\\Python\\TFT\\images\\tftLobby.png'
    # inQueue = False
    
    # if inQueue = False:
        # findBtnX, findBtnY = pyag.center(pyag.locateOnScreen(imageLoc, confidence=0.7))
        