import numpy as np
import cv2
import matplotlib.pyplot as plt

def box_filter(img, sz): #must be odd
	kernel = np.ones((sz,sz),np.float32)/(sz*sz)
	b = cv2.filter2D(img[:,:,0],-1,kernel)
	g = cv2.filter2D(img[:,:,1],-1,kernel)
	r = cv2.filter2D(img[:,:,2],-1,kernel)

	dst = np.empty([b.shape[0], b.shape[1], 3], dtype = img.dtype)

	dst[:,:,0] = b
	dst[:,:,1] = g
	dst[:,:,2] = r
	return dst


def median_filter(img,sz): #must be odd
	b = cv2.medianBlur(img[:,:,0], sz)
	g = cv2.medianBlur(img[:,:,1], sz)
	r = cv2.medianBlur(img[:,:,2], sz)

	dst = np.empty([b.shape[0], b.shape[1], 3], dtype = img.dtype)

	dst[:,:,0] = b
	dst[:,:,1] = g
	dst[:,:,2] = r
	return dst



def gaussian_filter(img, stdX, stdY):
	b = cv2.GaussianBlur(img[:,:,0],(stdX, stdY),0)#mean zero
	g = cv2.GaussianBlur(img[:,:,1],(stdX, stdY),0)
	r = cv2.GaussianBlur(img[:,:,2],(stdX, stdY),0)

	dst = np.empty([b.shape[0], b.shape[1], 3], dtype = img.dtype)

	dst[:,:,0] = b
	dst[:,:,1] = g
	dst[:,:,2] = r
	return dst

def bilateral_filter(img, d, stdC, stdS):#d: pixel neighborhood , stdC: sigmaColor, stdS: sigmaSpace
	b = cv2.bilateralFilter(img[:,:,0], d, stdC, stdS)#mean zero
	g = cv2.bilateralFilter(img[:,:,1], d, stdC, stdS)
	r = cv2.bilateralFilter(img[:,:,2], d, stdC, stdS)

	dst = np.empty([b.shape[0], b.shape[1], 3], dtype = img.dtype)

	dst[:,:,0] = b
	dst[:,:,1] = g
	dst[:,:,2] = r
	return dst

if __name__ == '__main__':

	img_original = cv2.imread('name_image.jpg')
	box_smooth = box_filter(img_original, 13)
	median_smooth = median_filter(img_original, 13)
	gaussian_smooth = gaussian_filter(img_original, 13, 13)
	bilateral = bilateral_filter(img_original,9,60,60)
	#you can use the opencv function directly

	plt.figure(figsize=(50,50))
	plt.subplot(2,2,1)
	plt.axis('off')
	plt.title("Average Filter", fontsize=11)
	plt.imshow(box_smooth[...,::-1])
	plt.subplot(2,2,2)
	plt.axis('off')
	plt.title("Mediam Filter", fontsize=11)
	plt.imshow(median_smooth[...,::-1])
	plt.subplot(2,2,3)
	plt.axis('off')
	plt.title("Gaussian Filter", fontsize=11)
	plt.imshow(gaussian_smooth[...,::-1])
	plt.subplot(2,2,4)
	plt.axis('off')
	plt.title("Bilateral Filter", fontsize=11)
	plt.imshow(bilateral[...,::-1])
	plt.show()


