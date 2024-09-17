import numpy as np
import pytesseract
from PIL import Image


def texto(imagen):
    pytesseract.pytesseract.tesseract_cmd = '/bin/tesseract'  # In case using colab after installing above modules
    image = cv2.imread(imagen)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(Image.fromarray(thresholded), config='--psm 11')
    text = text.strip()
    print(text)
    cv2.imshow('PythonGeeks', image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all OpenCV windows
    main()

def main():
    # Ask the user to select the area to capture
    print("Move the crosshair to the top-left corner of the area you want to capture and press Enter.")
    input()
    x1, y1 = pyautogui.position()

    print("Move the crosshair to the bottom-right corner of the area you want to capture and press Enter.")
    input()
    x2, y2 = pyautogui.position()

    # Capture the screenshot of the selected area
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))

    # Convert screenshot to format OpenCV can use (RGB)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # Display and save the screenshot using OpenCV
    cv2.imshow('Screenshot', img)
    cv2.imwrite('screenshot.png', img)
    print("adgh")
    
    
    

    texto('screenshot.png')  # Corrected function call

if _name_ == '_main_':
    main()
