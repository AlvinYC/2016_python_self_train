import matplotlib.pyplot as plt
import numpy as np
import cv2


plt.figure(0)
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3)
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0))
ax5 = plt.subplot2grid((3,3),(2,1))

#plt.show()

img = cv2.imread('gundam1.jpg')

plt.figure(1)
ax1 = plt.subplot2grid((5,2),(0,0),colspan=2,rowspan=3)
ax1.imshow(img)
ax2 = plt.subplot2grid((5,2),(3,0))
ax3 = plt.subplot2grid((5,2),(3,1))
ax4 = plt.subplot2grid((5,2),(4,0))
ax5 = plt.subplot2grid((5,2),(4,1))
plt.show()

