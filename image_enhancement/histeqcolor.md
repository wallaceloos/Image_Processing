### Histogram Equalization on Color Image
[[code]](codes/histequalizecolor.py)

<p align="justify">
The histogram equalization on a color image is performed by equalizing its brightness rather than the color. To keep the color in balance and only equalize the brightness, we need a color model that separates the color from the brightness. The color model HSV (Hue, Saturation, Value) describes the color, by the color itself (Hue and Saturation), and its brightness (Value). This model is also closer to the way in which human vision perceives color. With this new color model, we can equalize only the value component and keep the color in balance. The Figure below presents the result of the histogram equalization on a color image.
</p>

<p align="center">
<img src="https://github.com/wallaceloos/Image_Processing/blob/master/image_enhancement/images/img_histeqcolor.png" width="70%" height="70%">
</p>
