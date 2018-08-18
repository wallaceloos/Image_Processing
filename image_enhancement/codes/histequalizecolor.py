import numpy as np
import cv2
import matplotlib.pyplot as plt

def equalizeHistogram(img, L):
	m,n = img.shape
	hist,bins = np.histogram(img.flatten(),L,[0,L])
	cdf = hist.cumsum()
	cdfmin = np.min(cdf[np.nonzero(cdf)])
	cdf_normalized = (cdf-cdfmin).astype(float)/((m*n)-cdfmin).astype(float)
	cdf_normalized[cdf_normalized < 0] = 0
	heq = cdf_normalized*(L-1)
	return heq

if __name__ == '__main__':
	img = cv2.imread('name_image.jpg')
	L = 256

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	v = hsv[:,:,2]

	heq = equalizeHistogram(v, L)
	veq = heq[v] 
	hsv[:,:,2] = veq
	rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

	plt.figure(figsize=(15,15))
	plt.subplot(1,2,1)
	plt.title('Original image')
	plt.imshow(img[...,::-1])
	plt.axis('off')
	plt.subplot(1,2,2)
	plt.axis('off')
	plt.title('Equalized image')
	plt.imshow(rgb)

	plt.figure(figsize=(15,3))
	plt.subplot(1,3,1)
	plt.title('Original Histogram (Red)')
	plt.hist(img[:,:,2].flatten(),L,[0,L], color = 'r')#image, bins, range
	plt.xlim([0,256])

	plt.subplot(1,3,2)
	plt.xlim([0,256])
	plt.title('Original Histogram (Green)')
	plt.hist(img[:,:,1].flatten(),L,[0,L], color = 'g')

	plt.subplot(1,3,3)
	plt.xlim([0,256])
	plt.title('Original Histogram (Blue)')
	plt.hist(img[:,:,0].flatten(),L,[0,L], color = 'b')

	plt.figure(figsize=(15,3))
	plt.subplot(1,3,1)
	plt.title('Histogram Equalized (Red)')
	plt.hist(rgb[:,:,0].flatten(),L,[0,L], color = 'r')#image, bins, range
	plt.xlim([0,256])

	plt.subplot(1,3,2)
	plt.xlim([0,256])
	plt.title('Histogram Equalized (Green)')
	plt.hist(rgb[:,:,1].flatten(),L,[0,L], color = 'g')

	plt.subplot(1,3,3)
	plt.xlim([0,256])
	plt.title('Histogram Equalized (Blue)')
	plt.hist(rgb[:,:,2].flatten(),L,[0,L], color = 'b')

	plt.show()

