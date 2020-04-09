#REMEBER TO INSTALL pynput via pip 'pip install pynput'
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(15)

while 1 == 1:
    keyboard.press('l')
    keyboard.release('l')
    keyboard.press('o')
    keyboard.release('o')
    keyboard.press('l')
    keyboard.release('l')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print('Done!')
    c=180
    while c != 0:
        print(c)
        c-=1
        time.sleep(1)
