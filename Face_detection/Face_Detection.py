import cv2

img = cv2.imread('people2.jpg')

face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# if convert color to gray scale first the detection will be more perfect precise
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_model.detectMultiScale(gray_scale)

# Detect faces
for (x,y,w,h) in faces:
    # Create rectangle on the picture (use gray_scale for detect and use image for create rectangle after detecting)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

# Create rectangle on the picture
# cv2.rectangle(img, (200,200), (400,400), (0,0,255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ใช้ Face Detection with HAAR Cascade 