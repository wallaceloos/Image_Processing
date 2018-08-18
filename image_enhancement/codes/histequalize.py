#support material
#https://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html

import numpy as np
import cv2
import matplotlib.pyplot as plt

def equalizeHistogram(img, L):
	hist,bins = np.histogram(img.flatten(),L,[0,L])
	cdf = hist.cumsum()
	cdfmin = np.min(cdf[np.nonzero(cdf)])
	cdf_normalized = (cdf-cdfmin).astype(float)/((m*n)-cdfmin).astype(float)
	cdf_normalized[cdf_normalized < 0] = 0
	heq = cdf_normalized*(L-1)
	return heq

img = cv2.imread('name of the image',0)
m,n = img.shape
L = 256

heq = equalizeHistogram(img, L)
imgEq = heq[img]	

plt.figure(figsize=(15,15))
plt.subplot(2,2,1)
plt.title('Original image')
plt.imshow(img, 'gray')
plt.axis('off')
plt.subplot(2,2,2)
plt.axis('off')
plt.title('Equalized image')
plt.imshow(imgEq, 'gray')

plt.subplot(2,2,3)
plt.title('Histogram')
plt.hist(img.flatten(),L,[0,L], color = 'r')#image, bins, range
plt.xlim([0,256])
plt.subplot(2,2,4)
plt.xlim([0,256])
plt.title('Histogram equalized')
plt.hist(imgEq.flatten(),L,[0,L], color = 'r')
plt.show()
