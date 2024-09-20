import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageGrab
import pyautogui
##import matplotlib.pyplot as plt

def texto(imagen):
    pytesseract.pytesseract.tesseract_cmd = '/bin/tesseract'  # Update this path as needed
    image = cv2.imread(imagen)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(Image.fromarray(thresholded), config='--psm 11')
    text = text.strip()
    print(text)

    # Display the original image using Matplotlib
    

def main():
    print("Move the crosshair to the top-left corner of the area you want to capture and press Enter.")
    input()
    x1, y1 = pyautogui.position()
    
    print("Move the crosshair to the bottom-right corner of the area you want to capture and press Enter.")
    input()
    x2, y2 = pyautogui.position()

    # Capture the screenshot of the selected area
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img.save("screenshot.png")

    # Display the screenshot using Matplotlib
    img_np = np.array(img)  # Convert to numpy array
    #plt.imshow(img_np)  # Display the image
   # plt.title("Screenshot")
    #plt.axis('off')  # Hide axis
    #plt.show()

    texto('screenshot.png')  # Corrected function call

if __name__ == "__main__":
    main()
