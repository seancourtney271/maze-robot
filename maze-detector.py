import cv2 as cv
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    dataDirectory = '..\images'
    list = [f for f in os.listdir(dataDirectory) if f.endswith('.jpg') or f.endswith('png')]
    for file in list:
        string = dataDirectory + '\\'+ file
        image = cv.imread(string)
        cv.circle(image, (169, 12), 3, (255, 0, 0), -1)
        cv.circle(image, (80, 232), 3, (0, 0, 255), -1)
        plt.figure(figsize=(7, 7))
        plt.imshow(image)
        plt.show()
        key = cv.waitKey(0) & 0xFF  # mask safer on windows 64
    if key == 27:
        cv.destroyAllWindows()
    elif key == ord('s'):
        cv.imwrite('maze', image)
        cv.destroyAllWindows()

