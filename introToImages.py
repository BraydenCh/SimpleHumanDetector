import cv2 

img = cv2.imread('assets/img1.jpeg', 1)
"""img = cv2.resize(img, (400, 400)) """
"""how to resize manually"""

"""how to resize by variable"""
img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)


"""rotate image"""
"img = cv2.rotate(img, cv2.ROTATE_180)"

"""write an image"""
cv2.imwrite('new_img.jpg', img)

cv2.imshow('WindowLabel',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"cv2.IMREAD_COLOR : color image (also -1)"
"cv2.IMREAD_GRAYSCALE : loads in grayscale mode 0 "
"cv.IMREAD_unchanged: includes alpha channel 1"