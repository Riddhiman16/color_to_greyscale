import cv2
import matplotlib.pyplot as plt

# read the image
image = cv2.imread('mw.jpg')

# convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to a 2D array of pixels and 3 color values (RGB)
p = image.reshape((-1, 3))
w=len(p)

for i in range(0,w-1):
    h=(int(p[i][0])+int(p[i][1])+int(p[i][2]))/3
    p[i][0] = h
    p[i][1] = h
    p[i][2] = h


s = p.reshape(image.shape)

# show the image
plt.imshow(s)
plt.show()
