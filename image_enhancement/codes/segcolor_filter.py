import numpy as np
import cv2
import matplotlib.pyplot as plt


def segColor(img, bounding_box, factor):

    mask = np.zeros([img.shape[0], img.shape[1]])
   
    b = bounding_box[:,:,0]
    g = bounding_box[:,:,1]
    r = bounding_box[:,:,2]
    
    mean_r = np.mean(r)
    std_r = np.std(r)
    
    mean_g = np.mean(g)
    std_g = np.std(g)
    
    mean_b = np.mean(b)
    std_b = np.std(b)
    
    index1 = np.logical_and(img[:,:,2] >= (mean_r-factor*std_r), img[:,:,2] <= (mean_r+factor*std_r))
    index2 = np.logical_and(img[:,:,1] >= (mean_g-factor*std_g), img[:,:,1] <= (mean_g+factor*std_g))
    index3 = np.logical_and(img[:,:,0] >= (mean_b-factor*std_b), img[:,:,0] <= (mean_b+factor*std_b))
    
    mask = np.logical_and(np.logical_and(index1, index2), index3)
    
    return mask.astype(np.uint8)

if __name__ == '__main__':

	img = cv2.imread("name of the image")
	img_cpy = np.copy(img)

	#w =  width bounding box
	#h =  #height bounding box
	#(px,py) = #left corner coordinates

	#examples from the images
	w = 30
	h = 10
	px = 663
	py = 582

	w = 130
	h = 80
	px = 990
	py = 13


	cv2.rectangle(img_cpy,(px,py),(px+w,py+h),(0,0,0),5)#[(x,y), (x+w,y+h)]
	bounding_box = img[py:py+h,px:px+w]#[row,cols]

	mask_ = segColor(img, bounding_box, 3.2)
	res = cv2.bitwise_and(img,img,mask = mask_)

	plt.figure(figsize=(20,10))
	plt.subplot(1,3,1)
	plt.axis('off')
	plt.title("Original Image", fontsize=15)
	plt.imshow(img_cpy[...,::-1])
	plt.subplot(1,3,2)
	plt.axis('off')
	plt.title("Mask", fontsize=15)
	plt.imshow(mask_,"gray")
	plt.subplot(1,3,3)
	plt.axis('off')
	plt.title("Image AND Mask",fontsize=15)
	plt.imshow(res[...,::-1])
	plt.show()

