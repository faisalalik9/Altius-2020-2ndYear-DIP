import cv2
import numpy as np
from pprint import pprint
'''
Algo : Since we have to get rid of white circle in the red background.
I will be using the Flood-Fill Algorithm

Wrong Approach :
Because we also have a white circle in the green region. This method will fail.
if image[i][j] == 255:
    image[i][j = red
'''
def is_red(i, j, image):
    if(image[i][j][0] == 0 and image[i][j][1] == 14 and image[i][j][2] == 255):
        return True
    else:
        return False

def all_white(i, j, image):
    if(image[i][j][0] == 255 and image[i][j][1] == 255 and image[i][j][2] == 255):
        return True
    else:
        return False

def possible(i, j, rows, cols):
    # print(type(i), type(j), type(rows), type(cols))
    if(i >= 0 and i < rows and j >= 0 and j < cols):
        return True
    else:
        return False

filename = "Subtask1.png"
image = cv2.imread(filename, cv2.IMREAD_COLOR)
visited = np.zeros(shape=(image.shape[0], image.shape[1]))

# pprint(image[:300, :300, 3])


def dfs(x, y, image, rows, cols):
    if(visited[x][y]):
        return 
    if(possible(x, y, rows, cols) and is_red(x, y, image)):
        visited[x][y] = 1
        if(possible(x - 1, y, rows, cols) and all_white(x - 1, y, image)):
            image[x - 1][y][0] = 0
            image[x - 1][y][1] = 14
            image[x - 1][y][2] = 255
            dfs(x - 1, y, image, rows,  cols)


def main():

    rows, cols, channels = image.shape
    print(rows, cols)

    for i in range(rows):
        for j in range(cols):
            if(is_red(i, j, image)):
                dfs(i, j, image, rows, cols)

    cv2.imwrite("Output.jpg", image)


if __name__ == "__main__":
    main()