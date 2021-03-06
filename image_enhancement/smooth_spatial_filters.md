### Smoothing Spatial Filters  
[[code]](codes/smooth_filter.py)
<p align="justify">The spatial filtering is performed on the pixels of the image. Smoothing spatial filters are used to blur the image in order to: remove small details, make the object of interest more detectable, and for reduction of noise. The objects smaller than the size of the mask are usually blended with the background. As smooth filters reduce the sharp transition, they will also blur the edges. Examples of smoothing spatial filters are:</p>  

* average filters  
* median filter  
* gaussian filter  
* min and max filter

<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/smoothoriginal.png" width="35%" height="35%">
</p>

<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/smoothresult.png" width="100%" height="100%">
</p>
