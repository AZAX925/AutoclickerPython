import pyautogui
import time
flag = 0
time.sleep(2)

pyautogui.moveTo(777,2136)
time.sleep(1)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(328,63)
time.sleep(1)
pyautogui.click()
pyautogui.write("clickspeedtest.com")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.moveTo(1638,1066)
time.sleep(5)


count1 = time.time() + 5
while flag == 0:

    pyautogui.tripleClick()
    count2 = time.time()
    if count2 < count1:
        pass
    else:
        flag = 1

