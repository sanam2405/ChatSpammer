import pyautogui
import time

time.sleep(5)

limit = int(input("Enter the number of spams : "))
message = input("Enter the spam message : ")

for i in range(limit):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    # time.sleep(5)
