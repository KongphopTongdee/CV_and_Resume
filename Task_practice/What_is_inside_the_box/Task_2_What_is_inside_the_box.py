import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('inside-the-box.jpg',1)            # open file picture name inside-the-box

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)          # change the image color mode to cv2.COLOR_BGR2GRAY that is grey color

R, G, B = cv2.split(img)            # split the color to type Red,Green and Blue

output1_R = cv2.equalizeHist(R)         # change indensity histogram of Red type
output1_G = cv2.equalizeHist(G)         # change indensity histogram of Green type 
output1_B = cv2.equalizeHist(B)         # change indensity histogram of Blue type

output1 = cv2.merge((output1_R, output1_G, output1_B))          # sumation all type of histogram
output = [img, output1]         # create array stored image output 

fig, ax = plt.subplots(1,2)     # create fig screen, ax is select the graph to show
fig.set_figheight(15)           # create the screen height
fig.set_figwidth(15)            # create the screen width
for i in range(2):          # loop 2 times
    #plt.figure(figsize=(10,10))
    ax[i].imshow(output[i])         # select the picture in output value and show on screen
    #plt.xticks([])
    #plt.yticks([])
plt.show()          # plot show in fig

cv2.waitKey(0)
cv2.destroyAllWindows()