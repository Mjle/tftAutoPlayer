import glob, os
os.chdir(r"C:\Users\lemic\Desktop\Python\TFT\buyImages")
champList = []
for champ in glob.glob("*.png"):
    champName = champ.split('.')[0]
    champList.append(champName)
    print(champName)