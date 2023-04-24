import pyautogui
import keyboard
import time

input('Move this console Window so that it doesn\'t obstruct the download button. Then press Enter.')

while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('e'):
        break
    
    print('Searching for an image ...')
    buttonloc = pyautogui.locateOnScreen('slow download button.png')
    if buttonloc is None:
        print('Couldn\'t find the image!')
    else:
        center = pyautogui.center(buttonloc)
        oldpos = pyautogui.position()
        print('Found the image, clicking on '+ str(center[0]) + ', ' + str(center[1]) + '.')
        pyautogui.click(x=center[0], y=center[1])
        pyautogui.moveTo(oldpos)
        
    print('Sleeping now. You can end this script by holding CTRL+E.')
    time.sleep(8)