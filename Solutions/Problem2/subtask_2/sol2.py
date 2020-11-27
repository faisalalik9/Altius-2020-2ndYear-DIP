import cv2
import numpy as np


filename = "Subtask2.png"
image = cv2.imread(filename, cv2.IMREAD_COLOR)

# ALGORITHM
# Note these a, b, c were found out but soling for the equation of line 
# when the circle cuts the diagonal (lets call them P1, P2)
# So we find the line connecting (P1 and P2) -> ax + by + c = 0
# Now see that the red region will give -ve value when plugged in.
# Also the green region will give +ve value when plugged in.
# Lastly make sure that the pixels that you choose are within the red-green rectangle.

def find_distance(x, y, a = 44 , b = 73 , c = -25800):
    # The equation of line is ax + by + c

    return a*y + b*x + c

def make_pixel_red(i, j, image):
    image[i][j][0] = 0
    image[i][j][1] = 14
    image[i][j][2] = 255 

def make_pixel_green(i, j, image):
    image[i][j][0] = 11
    image[i][j][1] = 255
    image[i][j][2] = 0

def make_pixel_black(i, j, image):
    image[i][j][0] = 0
    image[i][j][1] = 0
    image[i][j][2] = 0

def inside_rectangle(i, j, image):
    if(j >= 157 and j <= 498):
        if(i >= 50 and i <= 261):
            return True
    
    return False


def main():
    rows,cols, channels = image.shape
    assert(channels == 3)


    for i in range(rows):
        for j in range(cols):
            if(inside_rectangle(i, j, image) == False):
                continue
            dist = find_distance(i, j)
            if(dist == 0):
                make_pixel_black(i, j, image)
            elif(dist < 0):
                make_pixel_red(i, j, image)
            else:
                make_pixel_green(i, j, image)

    cv2.imwrite("Outpur.jpg", image)

if __name__ == "__main__":
    main()