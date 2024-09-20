import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageGrab
import pyautogui
import time
import os

def texto(imagen):
    pytesseract.pytesseract.tesseract_cmd = '/bin/tesseract'  # In case using colab after installing above modules
    image = cv2.imread(imagen)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(Image.fromarray(thresholded), config='--psm 11')
    text = text.strip()
    print(text)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all OpenCV windows
    
def main():
    print("Move the crosshair to the top-left corner of the area you want to capture and press Enter.>")
    input()
    x1, y1 = pyautogui.position()
    #print(f"Top-left corner: ({x1}, {y1})")
    print("Move the crosshair to the bottom-right corner of the area you want to capture and press Enter>")
    input()
    x2, y2 = pyautogui.position()
    #print(f"Bottom-right corner: ({x2}, {y2})")
    # Capture the screenshot of the selected area
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img.save("screenshot.png")
    img = cv2.imread("screenshot.png")
    img_np = np.array(img)  # Convert to numpy array
    cv2.imshow("Screenshot", img_np)  # Display the image
    # Espera hasta que se presione una tecla para cerrar la ventana
    cv2.waitKey(0)
        
    texto('screenshot.png')  # Corrected function call

if __name__ == "__main__":
    main()
