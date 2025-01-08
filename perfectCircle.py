# ----- PERFECT CIRCLE DRAWER ON CIRCLE GAME -----
# ----- By Blake Almon -----


# -- Website : https://neal.fun/perfect-circle/ --
# -- Make sure website is full screen (Mac : on the very top of your mac click view while on the tab and turn off always show toolbars in fullscreen) --
# -- then click go but don't start drawing the circle --

# -- Run code then swap to website by doing alt + tab  (Mac : command + tab) --

# --- Enjoy ---


# --- imports ---
import pyautogui
import time
import math


#Time to swap tabs [2 seconds]
time.sleep(2)

# Radius 
R = 400

# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = pyautogui.position(x/2,y/2)

#make sure it starts if user did not click go
pyautogui.moveTo(X, Y)
pyautogui.click

# offsetting by radius 
pyautogui.moveTo(X+R,Y)
#mouse down
pyautogui.mouseDown()

#For loop for circle
for i in range(500):
    
    # setting pace with a modulus 
    if i%6==0:
       
       #moving to each pixel of the circle
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
      
