#loading image processing package
close all
clc

pkg load image

#loading image

im_rgb = imread("../images/shopping.jpg");
im_gray = rgb2gray(im_rgb);
template = im_gray(396:435, 420:440);

im_corr = normxcorr2(template, im_gray);
[y, x] = find(im_corr == max(im_corr(:)))

imshow(im_corr)

figure 
y = y - size(template,1) + 1;
x = x - size(template,2) + 1;

w = x + size(template,2) - 1;
h = y + size(template,1) - 1;

imshow(im_rgb)
hold on
h = rectangle ("Position", [x, y, 20, 40], "Curvature", [0.5, 0.5]);
set (h, "EdgeColor", [1, 0, 0]);
set (h, "linewidth", 2)