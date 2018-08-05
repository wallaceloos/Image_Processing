### Sharpening Spatial Filter
[[code]](codes/sharpening_filter.py)
<p align="justify">
The spatial filtering is performed on the pixels of the image. Sharpening spatial filters are used to reduce the effect of blurring and highlight fine details. For this we compute the derivative in order to find the sharp transitions. The sharp transition has high derivatives whereas the region with slow variation has low derivatives. For this reason the sharp transitions are highlighted and the regions with slow variations are attenuated. The discrete version of the derivative can be expressed by finite difference and need to follow some requirements: (1) the derivative of the flat region must be zero and; (2) the ramp region must be constant and different of zero for first-order derivatives, and zero for second-order derivatives. The first-order derivative can be approximated by df/dx = f(x+1)-f(x) and the second-order derivative by d2f/dx2 = f(x+1) + f(x-1) - 2f(x). The graphics below present the plot of a stripe from an image.
</p>
<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/stripe_.png" width="55%" height="45%">
</p>

<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/signalfd.png" width="49%" height="49%">
  <img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/signalsd.png" width="49%" height="49%">
</p>

<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/derivadas4.png" width="65%" height="65%">
</p>

<p align="center">
  <img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/img1_resposta1.png" width="65%" height="65%"/>
  <img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/img1_resposta2.png" width="65%" height="65%" /> 
</p>

<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/sharp_img.png" width="90%" height="90%">
</p>
