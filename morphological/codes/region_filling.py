import numpy as np
import cv2
import matplotlib.pyplot as plt


def draw_seed(seeds, img, size_rect):
    w = size_rect
    h = size_rect
    for p in seeds:
        img[p[0]:p[0]+h, p[1]:p[1]+w] = 255
    

def region_filling(img, seeds):
    iterations = 0
    x0 = np.zeros(img.shape)
    kernel = np.ones((3,3),np.uint8)
    imgC = cv2.bitwise_not(img)
    draw_seed(seeds, x0, 15)
    
    x1 = cv2.dilate(x0,kernel,iterations = 1)
    x1 = np.logical_and(x1,imgC)
    x1 = x1.astype(np.uint8)
    
    while np.max(x1.flatten()-x0.flatten()) > 0:
        x0 = x1
        x1 = cv2.dilate(x0,kernel,iterations = 1)
        x1 = np.logical_and(x1,imgC)
        x1 = x1.astype(np.uint8)
        iterations = iterations+1

    
    result = np.logical_or(x1,img)
    print ("iter:", iterations)
    return result
    


if __name__ == '__main__':

	bin_img = cv2.imread("filling.png",0)

	seeds = np.array([[213, 221], [178, 671], [523,170], [448, 449], [482, 834]])
	res = region_filling(bin_img, seeds)
	plt.axis('off')
	plt.imshow(res,'gray')
	plt.show()

