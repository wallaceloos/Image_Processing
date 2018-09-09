import numpy as np
import cv2
import matplotlib.pyplot as plt


def morphological_extraction(bin_img, seed, labels, label_id):
		iterations = 0
		x0 = np.zeros(bin_img.shape)
		kernel = np.ones((3,3),np.uint8)

		x0[seed[0],seed[1]] = 255

		x1 = cv2.dilate(x0,kernel,iterations = 1)
		x1 = np.logical_and(x1,bin_img)
		x1 = x1.astype(np.uint8)

		while np.max(x1.flatten()-x0.flatten()) > 0:
				x0 = x1
				x1 = cv2.dilate(x0,kernel,iterations = 1)
				x1 = np.logical_and(x1,bin_img)
				x1 = x1.astype(np.uint8)
				iterations = iterations+1

		labels[np.nonzero(x0)] = label_id
		

def extract_components(bin_img):
		[m,n] = bin_img.shape
		labels = np.zeros(bin_img.shape,dtype=np.uint8)
		label_id = 0

		for i in range(m):
			for j in range(n):
				if(bin_img[i,j] == 255 and labels[i,j] == 0):
					seed = np.array([i,j])
					label_id = label_id+1
					morphological_extraction(bin_img, seed, labels, label_id)

		print ("Number of components:", label_id)
		unique, counts = np.unique(labels, return_counts=True)
		print np.asarray((unique, counts)).T
		return labels, label_id
    

if __name__ == '__main__':

 	#There is a function named "label" from scipy.ndimage that can be used to extract the connected components as well
	bin_img = cv2.imread("extract.png",0)#binary image[0 and 255]

	res,labels = extract_components(bin_img)
	n_components = min(labels,6)# show at most 6 components

	ind = 1
	plt.figure(figsize=(20,10))
	while ind <= n_components:
		plt.subplot(1,n_components,ind)
		plt.title('Label:'+str(ind), fontsize=15)
		plt.axis('off')
		x = np.zeros(bin_img.shape,dtype=np.uint8)
		x[res==ind] = 255
		plt.imshow(x,'gray')
		ind = ind+1
	plt.show()

