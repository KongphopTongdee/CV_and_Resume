import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Pokemon_Go.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gaussian = cv2.GaussianBlur(img, (5,5), 2.0)
gmask = img - gaussian
unshape = img + 1*gmask
highboost = img + 5*gmask

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(unshape),plt.title('Unsharp_Masking')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(highboost),plt.title('High_boost_Filtering')
plt.xticks([]), plt.yticks([])
plt.show()

