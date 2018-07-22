### Histogram Equalization
[[code]](codes/histequalize.py)

<p align="justify"> Histogram equalization can be used for image enhancement. Consider a digital grayscale image with gray levels in the range [0, L-1]. The idea of the histogram equalization is increase the dynamic range of the gray levels in the image improving its contrast. This will make the distribution of the image intensities more uniform. So, you want to make your histogram distribution close to an uniform distribution. Cumulative distribution function (cdf) can be used to do that. The cdf can be used to compute the percentile of the intensity I and then mapping the new intensity based in this percentile.  For example, let's take L = 256 and suppose that our image is in the range [80,120]. So, 80 is 0th percentile and 120 is 100th percentile. Thus the intensity 80 will be map to intenisty 0 and the intensity 120 wil be map to intensity 255, stretching the histogram. 

<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/resulthist.png" width="70%" height="70%">
</p>
