import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
import time
# ImageGrab will take a screenshot of your current screen/window
# pyautogui will help us perform a function(pressing of a key using pyautogui),
# if at a particular coordinate of the picture grabed by PIL there is dark pixel.(Obstacle)
# from numpy import asarray


# Function which will help us to hit any key when needed.
def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds/ Detects Birds
    for i in range(500, 575):
        for j in range(400, 553):
            if data[i, j] > 155:
                hit("down")
                return

    # Detects Cactus
    for i in range(500, 600):
        for j in range(590, 690):
            if data[i, j] >155:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(5)
    hit('space') #to start the game
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert('L') #.convert('L') returns a grayscale image
        data = image.load() #loads the image in array form. Allocates storage for the image and loads the pixel data.
        isCollide(data) #Checks if collition happens on every screenshot

    # # Draw the rectangle for birds
    # for i in range(375, 475):
    #     for j in range(400, 553):
    #         data[i, j] = 171
    #
     # Draw the rectangle for cactus
    # for i in range(375, 525):
    #     for j in range(590, 690):
    #          data[i, j] = 0
    # image.show()
    # break
        # print(asarray(image)) to show the image as an numpy array

''' 
use chrome://dino to run this program. Run this program and go to this url
so that your pyautogui can work on your screen and make the game auto.
'''

       
