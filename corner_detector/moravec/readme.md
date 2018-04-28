
# Moravec corner detection algorithm

### Usage

Octave script

```ocatve
%reading the image
g = uint8(imread('predio.jpg'));%name of the image

%converting to grayscale
if (size(g,3) > 1)
  img = rgb2gray(g);
else
	img = g;
end

%setting parameters
threshold = 850;
lenW = 3;

%name of the output file
filename = 'output.png';

%moravec corner detector
%input: image, threshold and the size of the window
%output: corners detected and image with the corners detected over the input image
[corner_map] = corner_detection_moravec(img, threshold, lenW, filename);
```

<p align="center">
  <img width="256" height="256" src="https://github.com/wallaceloos/Image_Processing/blob/master/corner_detector/moravec/images/blox.png">
  <img width="256" height="256" src="https://github.com/wallaceloos/Image_Processing/blob/master/corner_detector/moravec/images/img7x7_t12000.png">
</p>

<p align="center">
  <img width="256" height="256" src="https://github.com/wallaceloos/Image_Processing/blob/master/corner_detector/moravec/images/predio.jpg">
  <img width="256" height="256" src="https://github.com/wallaceloos/Image_Processing/blob/master/corner_detector/moravec/images/img3x3_t850.png">
</p>

