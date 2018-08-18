import numpy as np
import cv2
import matplotlib.pyplot as plt

def computeInverse(cdf, cdf_ref, L):

	refInv = np.zeros([L], dtype = cdf.dtype)
	for i in range(L):
		index = np.argmin(abs(cdf[i]-cdf_ref))
		refInv[i] = index

	return refInv

def histogramMatching(img, ref, L):#image and the reference image, L: total number of gray level

	m,n = img.shape
	hist,bins = np.histogram(img.flatten(),L,[0,L])
	cdf = hist.cumsum()/float(m*n)

	m_ref,n_ref = ref.shape
	hist_ref,bins_ref = np.histogram(ref.flatten(),L,[0,L])
	cdf_ref = hist_ref.cumsum()/float(m_ref*n_ref)
	
	hm = computeInverse(cdf, cdf_ref, L)
	dst = np.empty(img.shape, dtype = img.dtype)
	dst = hm[img.astype(int)]

	return dst

if __name__ == '__main__':

	img = cv2.imread('name_image.jpg',0) # this image is unsigned int 8 (uint8[0,255])
	img_ref = cv2.imread('name_reference_image.jpg',0)
	img = img.astype(float) #converting to float
	img_ref = img_ref.astype(float) #converting to float
	L = 256
	img_match = histogramMatching(img, img_ref, L)

	plt.figure(figsize=(50,50))
	plt.subplot(2,3,1)
	plt.axis('off')
	plt.title('Original Image',fontsize=15)
	plt.imshow(img,'gray')
	plt.subplot(2,3,2)
	plt.axis('off')
	plt.title('Reference Image',fontsize=15)
	plt.imshow(img_ref,'gray')
	plt.subplot(2,3,3)
	plt.axis('off')
	plt.title('Image Matching', fontsize=15)
	plt.imshow(img_match,'gray')


	plt.subplot(2,3,4)
	plt.title('Original Histogram',fontsize=15)
	plt.hist(img.flatten(),L,[0,L], color = 'r')
	plt.subplot(2,3,5)
	plt.title('Reference Histogram',fontsize=15)
	plt.hist(img_ref.flatten(),L,[0,L], color = 'r')
	plt.subplot(2,3,6)
	plt.title('Histogram Matching',fontsize=15)
	plt.hist(img_match.flatten(),L,[0,L], color = 'r')


	plt.show()


