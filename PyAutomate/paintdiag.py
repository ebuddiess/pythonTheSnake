
import pyautogui as py
i=0
x=500
y=400
counter=10
py.moveTo(x, y)

while i<20:
 py.dragTo(x+counter,y) #l50
 py.dragTo(x,y+counter) #r50
 py.dragTo(x-counter,y) #l-50
 py.dragTo(x,y-counter) #r-50
 counter=counter+15
 i=i+1
