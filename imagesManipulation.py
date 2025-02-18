import cv2
import random
img = cv2.imread('assets/img1.jpeg')

"""tells (height, width, # channels)"""
print(img.shape)

"""
    how to look at the x row, n-m pixels of the image
    print(img[x][n:m])
"""

"""
images looks like:

this is the image layout, where this is a 2x2 image, 
this is row,column, pixel format

color is bgr format (blue, green, red)
[
[[0,0,0],[255,255,255]],
[[0,0,0],[255,255,255]]
]

"""


"""how to randomize colors of certain pixels in the image"""
for i in range(100):   
    """for each rows, you want # of columbs"""
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]


"""
    copy part of the image
    copies the square captured this range
 """

tag = img[1000:1400,600:1000]
"paste into row 100-500 col 100-500"
img[100:500,100:500] = tag

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()