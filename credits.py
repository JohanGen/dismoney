import pyautogui
import pytesseract

def extract_credits_from_screenshot(region=None):
    # Capture screenshot of the specified region
    screenshot = pyautogui.screenshot(region=region)
    
    # Extract text using pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'D:\bildefinner\tesseract.exe'
    text = pytesseract.image_to_string(screenshot)
    screenshot.save("debug_screenshot.png")

    
    # Split the text by lines and search for the line with 'Credits'
    for line in text.split('\n'):
        if "Credits" in line:
            credits = ''.join(filter(str.isdigit, line))
            return int(credits)
    return None

region = (380, 590, 500, 350)
result = extract_credits_from_screenshot(region)  # Store the result in the variable 'result'

print(result)  # Print the result


