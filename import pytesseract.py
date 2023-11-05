import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\bildefinner\tesseract.exe'
img_path = r"C:\Users\johan\OneDrive\Dokumenter\dismoney\debug_screenshot.png"

text = pytesseract.image_to_string(img_path)
print(text)

