import numpy as np
import cv2
import matplotlib.pyplot as plt


def sharpening_laplacian_gray_image(img):

	kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]], dtype = float)#laplacian operator (composite mask)

	laplace = cv2.filter2D(img,-1,kernel)

	laplace = laplace-np.min(laplace)
	laplace = laplace/np.max(laplace)*255
		 	
	return laplace

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

def sharpening_laplacian_color_image(img):

	b = img[:,:,0]
	g = img[:,:,1]
	r = img[:,:,2]

	b = sharpening_laplacian_gray_image(b)
	g = sharpening_laplacian_gray_image(g)
	r = sharpening_laplacian_gray_image(r)

	#applying histogram matching to ajust the intensity
	b = histogramMatching(b, img[:,:,0], 256)
	g = histogramMatching(g, img[:,:,1], 256)
	r = histogramMatching(r, img[:,:,2], 256)

	dst = np.empty([b.shape[0], b.shape[1], 3], dtype = img.dtype)

	dst[:,:,0] = b
	dst[:,:,1] = g
	dst[:,:,2] = r

	return dst


if __name__ == '__main__':

	img = cv2.imread('name_image.jpg') # this image is unsigned int 8 (uint8[0,255])
	img = img.astype(float) #converting to float

	laplace = sharpening_laplacian_color_image(img)

	img = img.astype(np.uint8)
	laplace = laplace.astype(np.uint8)

	plt.figure(figsize=(50,50))
	plt.subplot(1,2,1)
	plt.axis('off')
	plt.title('Original image',fontsize=15)
	plt.imshow(img[...,::-1])
	plt.subplot(1,2,2)
	plt.axis('off')
	plt.title('Sharp image (Laplacian operator)', fontsize=15)
	plt.imshow(laplace[...,::-1])
	plt.show()
