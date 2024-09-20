import numpy as np
import pytesseract
from PIL import Image, ImageGrab
import cv2
import pyautogui
import time
from pyvirtualdisplay import Display
import os

os.environ['QT_QPA_PLATFORM'] = 'wayland'

display = Display(visible=0, size=(1024, 768))
display.start()
#display = Display(visible=0, size=(1024, 768))
#display.start()

def texto(imagen):
    pytesseract.pytesseract.tesseract_cmd = '/bin/tesseract'  
    image = cv2.imread(imagen)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(Image.fromarray(thresholded), config='--psm 11')
    text = text.strip()
    print(text)
    cv2.imshow('PythonGeeks', image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
    main()

def main():
    print("Move the crosshair to the top-left corner of the area you want to capture and press Enter.")
    input()
    x1, y1 = pyautogui.position()
    print(f"Top-left corner: ({x1}, {y1})")

    print("Move the crosshair to the bottom-right corner of the area you want to capture and press Enter.")
    input()
    x2, y2 = pyautogui.position()
    print(f"Bottom-right corner: ({x2}, {y2})")

    # Add a delay to ensure the screenshot is taken correctly
    time.sleep(1)

    # Capture the screenshot of the selected area
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))

    # Check if the image is not empty
    if img:
        # Convert screenshot to format OpenCV can use (RGB)
        #img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        
        # Display and save the screenshot using OpenCV
        cv2.imshow('Screenshot', img)
        cv2.imwrite('screenshot.png', img)
        
        texto('screenshot.png')  
    else:
        print("Failed to capture screenshot.")

if __name__ == '__main__':
    main()
