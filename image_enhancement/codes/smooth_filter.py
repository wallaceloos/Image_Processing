import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def mean_filter(img, size_mask):#must be odd
	blurImage = np.empty(img.shape, dtype = img.dtype)
	kernel = float(1.0/(size_mask*size_mask))*np.ones([size_mask, size_mask]).astype(float)
	blur = signal.convolve2d(img, kernel, boundary='symm', mode='same')	
	return blur

def median_filter(img, size_mask):#must be odd
	m,n = img.shape
	blur_size_m = int(m-(size_mask/2)*2)
	blur_size_n = int(n-(size_mask/2)*2)

	blur = np.empty([blur_size_m, blur_size_n], dtype = img.dtype)
	print blur.shape
	for i in range(blur_size_m):
		for j in range(blur_size_n):
			kernel = img[i:i+size_mask, j:j+size_mask]
			blur[i,j] = np.median(kernel)
	return blur

def min_filter(img, size_mask):#must be odd
	m,n = img.shape
	blur_size_m = int(m-(size_mask/2)*2)
	blur_size_n = int(n-(size_mask/2)*2)

	blur = np.empty([blur_size_m, blur_size_n], dtype = img.dtype)
	print blur.shape
	for i in range(blur_size_m):
		for j in range(blur_size_n):
			kernel = img[i:i+size_mask, j:j+size_mask]
			blur[i,j] = np.min(kernel)
	return blur

def max_filter(img, size_mask):#must be odd
	m,n = img.shape
	blur_size_m = int(m-(size_mask/2)*2)
	blur_size_n = int(n-(size_mask/2)*2)

	blur = np.empty([blur_size_m, blur_size_n], dtype = img.dtype)
	print blur.shape
	for i in range(blur_size_m):
		for j in range(blur_size_n):
			kernel = img[i:i+size_mask, j:j+size_mask]
			blur[i,j] = np.max(kernel)
	return blur

def gauss_filter(img, std, size_mask):#must be odd
	
	m,n = img.shape
	blur_size_m = int(m-(size_mask/2)*2)
	blur_size_n = int(n-(size_mask/2)*2)
	blur = np.empty([blur_size_m, blur_size_n], dtype = img.dtype)
	
	x = np.arange(-size_mask, size_mask+1)
	y = np.arange(-size_mask, size_mask+1)

	[X, Y] = np.meshgrid(x,y)
	kernel = (1.0/2*np.pi*std*std)*np.exp( -(X**2+Y**2)/(2.0*std*std) )
	blur = signal.convolve2d(img, kernel, boundary='symm', mode='same')	
	
	return blur

if __name__ == '__main__':

	#opencv already had box, gaussian and median filter implemented. they are much more faster than mine
	#cv2.GaussianBlur
	#cv2.blur
	#cv2.medianBlur

	img = cv2.imread('name of the image',0)

	m,n = img.shape
	noise = 25*np.random.randn(m, n)#adding noise in the image
	img = img+noise
	
	average_f = mean_filter(img, 11)
	median_f = median_filter(img, 11)
	min_f = min_filter(img, 11)
	max_f = max_filter(img, 11)
	gauss_f = gauss_filter(img, 6, 11)
	
	plt.figure(figsize=(30,10))
	plt.subplot(2,3,1)
	plt.title('Original image+noise')
	plt.axis('off')
	plt.imshow(img, 'gray')

	plt.subplot(2,3,2)
	plt.title('Average filter')
	plt.axis('off')
	plt.imshow(average_f, 'gray')

	plt.subplot(2,3,3)
	plt.title('Median filter')
	plt.axis('off')
	plt.imshow(median_f, 'gray')

	plt.subplot(2,3,4)
	plt.title('Gaussian filter')
	plt.axis('off')
	plt.imshow(gauss_f, 'gray')

	plt.subplot(2,3,5)
	plt.title('Max filter')
	plt.axis('off')
	plt.imshow(max_f, 'gray')

	plt.subplot(2,3,6)
	plt.title('Min filter')
	plt.axis('off')
	plt.imshow(min_f, 'gray')

	plt.show()
	
