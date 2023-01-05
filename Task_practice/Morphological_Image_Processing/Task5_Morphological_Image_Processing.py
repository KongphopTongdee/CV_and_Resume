# import cv2
# import numpy as np
# import matplotlib.pylab as plt
# from pytesseract import pytesseract

# # Load in Grayscale
# img = cv2.imread('text_frombook.png')

# kernel = cv2.getStructuringElement(cv2.MO)

# # find the letter O
# se = cv2.getStructuringElement(cv2.MORPH_RECT,(1,51))
# img1 = cv2.erode(img, se)

# # reconstrction

# plt.figure(figsize=([20,20]))
# plt.subplot(311),plt.imshow(img, cmap = 'gray')
# plt.title('original'),plt.xticks([]),plt.yticks([])
# plt.subplot(312),plt.imshow(img1, cmap = 'gray')
# plt.title('the letter O'),plt.xticks([]),plt.yticks([])
# # plt.subplot(313),plt.imshow(img2, cmap = 'gray')
# # plt.title('final result'),plt.xticks([]),plt.yticks([])
# plt.show()

## this is for testing
# pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# img = cv2.imread("text_frombook.png")
# height, width, c = img.shape

# letter_boxes = pytesseract.image_to_boxes(img)

# # print(letter_boxes)

# for box in letter_boxes.splitlines():   
#     box = box.split()
#     # print(box)
#     if box[0] == 'o':
#         x,y,w,h = int(box[1]),int(box[2]),int(box[3]),int(box[4])
#         # cv2.rectangle(img, (x,y), (w,h), (0,0,255), 3)
#         cv2.rectangle(img, (x,height-y), (w,height-h), (0,0,255), 3)
#         cv2.putText(img, box[0],(x,height-h+32),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

# cv2.imshow("window", img)
# cv2.waitKey(0)

import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("text_frombook.png")
height, width, c = img.shape

letter_boxes = pytesseract.image_to_boxes(img)

for box in letter_boxes.splitlines():   
    box = box.split()
    if box[0] == 'o':
        x,y,w,h = int(box[1]),int(box[2]),int(box[3]),int(box[4])
        cv2.rectangle(img, (x,height-y), (w,height-h), (0,0,255), 3)
        cv2.putText(img, box[0],(x,height-h+32),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imshow("window", img)
cv2.waitKey(0)