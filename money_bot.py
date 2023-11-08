import pyautogui
import time
import pytesseract

icon_location = pyautogui.locateCenterOnScreen('C:/Users/johan/OneDrive/Dokumenter/dismoney/target_chat.png')
message = "t!wallet"
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/johan/OneDrive/Dokumenter/dismoney/bildefinner/tesseract.exe'

gammel_verdi = 3294

def open_discord_channel():
    pyautogui.moveTo(icon_location)
    pyautogui.click()
    pyautogui.typewrite(message)
    pyautogui.press('enter')

def extract_values_from_screenshot(region=None):
    # Capture screenshot of the specified region
    screenshot = pyautogui.screenshot(region=region)
    
    # Extract text using pytesseract
    text = pytesseract.image_to_string(screenshot)
    
    def extract_value(text, keyword):
        for line in text.split('\n'):
            if keyword in line.lower():
                return ''.join(filter(str.isdigit, line))
        return None

    credits = extract_value(text, "credits")
    tokens = extract_value(text, "tokens")
    server_points = extract_value(text, "server points")

    return {
        "Credits": credits,
        "Tokens": tokens,
        "Server Points": server_points
    }

ny_verdi = 0
sikkerhet = 0
while True:
    open_discord_channel()
    sikkerhet += 1
    endring = sikkerhet

    # venter på at tatsu oppdaterer credits
    time.sleep(5)

    # området botten tar screenshot av tatsu info
    region = (380, 590, 500, 350)
    values = extract_values_from_screenshot(region)

    # transformerer credits til int
    try:
        current_credits = int(values['Credits'])
    except TypeError:
        continue
    ny_verdi = current_credits - gammel_verdi

    if ny_verdi < 0:
        ny_verdi = 0

    if sikkerhet == 300:
        break
    if gammel_verdi < current_credits:
        if ny_verdi <= 10:
            pyautogui.typewrite('t!slots') #+ str(ny_verdi))
            pyautogui.press('enter')
        if ny_verdi > 10:
            pyautogui.typewrite('t!slots')
            pyautogui.press('enter')
            ny_verdi = 1
    else:
        # pyautogui.typewrite('t!slots')
        # pyautogui.press('enter')
        ny_verdi = 1
        sikkerhet += 1
    


    # Update the old value with the current credits for the next iteration
    gammel_verdi = current_credits - 1

    # current_credits_actual = current_credits - ny_verdi
    
    ny_verdi = 0

    print(gammel_verdi)

    if endring < sikkerhet:
        print('Sikkerhet: ', sikkerhet)

    # venter 2 min på neste kjøring (115 + 5)
    time.sleep(115)

