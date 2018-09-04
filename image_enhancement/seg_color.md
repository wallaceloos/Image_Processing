### Color Segmentation
[[code]](codes/segcolor_filter.py)

<p align="justify">
Segmentation is the process of partitioning an image into different segments.  Here, we are interested in segments that have colors in a specific range. A straightforward approach to do this is based on the RGB color system. We define a bounding box around the region of interest and then compute the average (mR, mG, mB) and the standard deviation (stdR, stdG, stdB) for each channel from the samples that belong to the bounding box. After that, for each color from the image, we check whether it is inside or outside of the ranges:  [mR-stdR, mR+stdR], [mG-stdG, mG+stdG], and [mB-stdB, mB+stdB]. The Figure below presents the result of the segmentation in a color image.
</p>

<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/segcolor_1.png" width="90%" height="90%">
</p>
