import pyautogui
import time
sikkerhet = 0
icon_location = pyautogui.locateCenterOnScreen('C:/Users/johan/OneDrive/Dokumenter/dismoney/lyd_spam.png')
# icon_location1 = pyautogui.locateCenterOnScreen('C:/Users/johan/OneDrive/Dokumenter/dismoney/lyd_spam.png')

def open_discord_channel():
    pyautogui.moveTo(icon_location)
    pyautogui.click()


# def open_discord_channel1():
#     pyautogui.moveTo(icon_location1)
#     pyautogui.click()

time.sleep(5)
while True:
    open_discord_channel()
    time.sleep(1)
    # open_discord_channel1()
    sikkerhet += 1
    if sikkerhet == 200:
        break