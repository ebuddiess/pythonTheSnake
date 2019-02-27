import time
import pyautogui as py

def save(command):
    py.moveTo(200,200)
    py.click(200,200)
    py.typewrite('clear')
    py.press('enter')
    py.typewrite(command)
    py.press('enter')
    time.sleep(5)
    py.press('printscreen')
    py.moveTo(200,500)
    py.click(200,500)
    py.hotkey('ctrl','v')
    py.hotkey('ctrl','s')
    py.typewrite(command+'.png')
    py.press('enter')
    py.hotkey('ctrl','n')

data = ['help -d cd' , 'apropos init ' , 'whatis ls' , 'date', 'cal','cal -3','who','whoami','whoami --version']
for command in data:
    save(command)