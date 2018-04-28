#loading image processing package
close all
clc

pkg load image

#loading image

im_rgb = imread("/home/wallace/computer_vision/images/lion.jpg");
im_gray = rgb2gray(im_rgb);

filter_size = 21;
ind = 1;
for sigma = 1:3:10
sigma
  subplot(2,4,ind)
  h = fspecial('gaussian', filter_size, sigma);
  imagesc(h);
  
  subplot(2,4,ind+4)
  im = imfilter(im_gray, h);
  imshow(im);
  
  ind = ind + 1;
end
