import numpy as np
import cv2
import matplotlib.pyplot as plt


def boundary_extraction(bin_img, thickness):
    kernel = np.ones((thickness,thickness),np.uint8)
    erosion = cv2.erode(bin_img,kernel,iterations = 1)
    diff = bin_img - erosion
    return diff

if __name__ == '__main__':

	img = cv2.imread("binary image",0)
	bin_img = np.copy(img)

	boundary1 = boundary_extraction(bin_img, 7)
	boundary2 = boundary_extraction(bin_img, 13)
	boundary3 = boundary_extraction(bin_img, 17)

	plt.figure(figsize=(20,10))
	plt.subplot(1,3,1)
	plt.axis('off')
	plt.title("7x7", fontsize=15)
	plt.imshow(boundary1,'gray')
	plt.subplot(1,3,2)
	plt.axis('off')
	plt.title("13x13", fontsize=15)
	plt.imshow(boundary2,'gray')
	plt.subplot(1,3,3)
	plt.axis('off')
	plt.title("17x17", fontsize=15)
	plt.imshow(boundary3,'gray')
	plt.show()

