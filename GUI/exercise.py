#! python3
# Failsafe - move mouse cursor to any corner of the screen
# Some functions have been left out - don't all work on macOs (pyautogui's window functions)
import pyautogui

#######################################################
# Controlling mouse movement

# wh = pyautogui.size() # obtain screen resolution
# print(wh)
# print(wh[0])
# print(wh.width)

# moving the mouse
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# # Move mouse from current relative position
# for i in range(10):
#     pyautogui.move(100, 0, duration=0.25)  # right
#     pyautogui.move(0, 100, duration=0.25)  # down
#     pyautogui.move(-100, 0, duration=0.25)  # left
#     pyautogui.move(0, -100, duration=0.25)  # up

# Getting mouse position
# print(pyautogui.position())
# p = pyautogui.position()
# print(p[0])
# print(p.x)

#######################################################
# Mouse interaction

import time
# Clicking the mouse
# pyautogui.click(10, 5)
# pyautogui.click(500, 500, button='right')  # 'button' keyword to specify which mouse button

# Dragging the mouse to create a spiral (using https://sumo.app/)
# time.sleep(5)
# pyautogui.click() # Click to make the window active
# distance = 300
# change = 20
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2, button='left')
#     distance = distance - change
#     pyautogui.drag(0, distance, duration=0.2, button='left')
#     pyautogui.drag(-distance, 0, duration=0.25, button='left')
#     distance = distance - change
#     pyautogui.drag(0, -distance, duration=0.25, button='left')

#######################################################
# Scrolling the mouse

# time.sleep(2)
# pyautogui.scroll(20)

#######################################################
# Planning mouse movements

# import sys
# sys.platform='_'
# pyautogui.mouseInfo() # Opens mouseInfo window for mouse current position and RGB value

#######################################################
# Screenshots

# im = pyautogui.screenshot()
#
# print(pyautogui.pixel(0, 0))
# print(pyautogui.pixel(50, 200))
# print(pyautogui.pixelMatchesColor(50, 200, (59, 63, 66)))
# print(pyautogui.pixelMatchesColor(50, 200, (255, 135, 144)))

#######################################################
# Image recognition
# Ensure the image is in the foreground when the program is run.

b = pyautogui.locateOnScreen('image.png')
print(b)
print(b[0])
print(b.left)
# print(list(pyautogui.locateAllOnScreen('image.png')))

# Then click
pyautogui.click('image.png')