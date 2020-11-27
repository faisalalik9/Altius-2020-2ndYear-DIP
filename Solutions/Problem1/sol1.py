import cv2
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# Returns the image object
def read_image(filename):
    img = cv2.imread(filename)
    return img

def part_1(rgb_image):
    grayscale_img = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    return grayscale_img

def part_2(gray_image):

    rows, cols = gray_image.shape
    print("Grayscale Image Shape : ", gray_image.shape, "\n")
    #assert(channels == 1)

    a = [0]*256
    for i in range(rows):
        for j in range(cols):
            a[gray_image[i][j]] += 1

    assert(sum(a) == rows*cols)
    return a

def part_3(hist_vector):
    # Have to normalise the hist_vector to denote the pdf
    pdf_vector = np.array(hist_vector, copy = True, dtype = np.float64)
    total_pixels = sum(pdf_vector)

    for i in range(len(pdf_vector)):
        pdf_vector[i] /= total_pixels

    assert(abs(sum(pdf_vector) - 1) < 0.01)
    return list(pdf_vector)

def part_4(img, hist_vector):
    # Now calculating the expected_value of pixel values
    mean = 0
    for i in range(0, 256):
        mean += i*hist_vector[i]
    
    # Now calculating the varinace of pixel values
    variance = 0
    for i in range(0, 256):
        variance += i**2*hist_vector[i]
    variance -= mean**2

    # Some checks 
    #print(mean, np.mean(img))
    print(variance, np.var(img))
    assert(abs(mean - np.mean(img)) < 0.01)
    assert(abs(variance - np.var(img)) < 0.01)

    return (mean, variance)

def part_5(a):
    idxs = []
    for i in range(1, 255):
        if(a[i] > a[i + 1] and a[i] > a[i - 1]):
            idxs.append(i)
    print(len(idxs))
    s = ",".join(str(x) for x in idxs)
    return s

def do_everything(filename):

    dog_image = read_image(filename)
    # Part 1 
    grayscale_dog = part_1(dog_image)

    # Part 2 
    histogram = part_2(grayscale_dog)
    # # Part 3
    pdf = part_3(histogram)

    # # Part 4
    mean, variance = part_4(grayscale_dog, pdf)
    print(f"MEAN IS {mean}", "\n")
    print(f"VARIANCE IS {variance}", "\n")

    # # PART 5
    idxs = part_5(histogram)
    print("Comma Separted Indexes : ", idxs, "\n")


if __name__ == "__main__":

    filename = "dog.jpg"
    do_everything(filename)


