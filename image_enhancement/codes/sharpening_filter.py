import numpy as np
import cv2
import matplotlib.pyplot as plt

def first_derivative(signal):
	fd = signal[1:]-signal[:-1]
	return fd

def second_derivative(signal):
	sd =  signal[2:]+signal[:-2]-2*signal[1:-1]
	return sd

def sharpening_laplacian_gray_image(img):

	kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])#laplacian operator (composite mask)
	laplace = cv2.filter2D(img,-1,kernel)

	laplace = laplace-np.min(laplace)
	laplace = laplace/np.max(laplace)*255
		 
	return laplace

if __name__ == '__main__':

	img = cv2.imread('name of the image',0) # this image is unsigned int 8 (uint8[0,255])
	img = img.astype(float) #converting to float

	laplace = sharpening_laplacian_gray_image(img)

	plt.subplot(1,2,1)
	plt.axis('off')
	plt.title('Original image')
	plt.imshow(img, 'gray')
	plt.subplot(1,2,2)
	plt.axis('off')
	plt.title('Sharp image (Laplacian operator)')
	plt.imshow(laplace, 'gray', vmin = 10, vmax = 250)#ajusting the intensities[vmin, vmax] (you can make a fine tuning)

	plt.show()

