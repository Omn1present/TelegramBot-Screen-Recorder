import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = tuple(pyautogui.size())
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 12.0, (SCREEN_SIZE))
while True:    
    img = pyautogui.screenshot()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out.write(img)