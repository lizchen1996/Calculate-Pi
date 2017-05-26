# Calculating Pi
## Method of the polygons

This is my favourite method, because is very easy to understand and can give you a range where the real value of Pi is.

This method is based on the fact that a circle is a regular polygon with infinite sides. So, to get an aproximate value of Pi we only have to calculate Pi with a polygon with a lot of sides.

<!--![Polygon inside a circle. A circle is a regular polygon with infinite sides](https://github.com/xoancosmed/Calculate-Pi/blob/readme/Polygons/images/polygon_circle.png)-->
<div><center><img src="https://github.com/xoancosmed/Calculate-Pi/blob/readme/Polygons/images/polygon_circle.png" alt="Polygon inside a circle. A circle is a regular polygon with infinite sides" width="250" style="display: block; margin: auto;"/></center></div>

But how we get the value of Pi of a regular Polygon? This is very easy. We know that the perimeter of the circle is `2·r·pi`. So, to calculate Pi we only have to know the radius of the circle (whitch we will fix) and the permiter of the polygon (which is the `L·N`, where _N_ is the number of sides and _L_ is the length of each side).

<!--![Example of how to calculate Pi from a polygon](https://github.com/xoancosmed/Calculate-Pi/blob/readme/Polygons/images/circulo_cuadrado_calcular_pi.png)-->
<div><center><img src="https://github.com/xoancosmed/Calculate-Pi/blob/readme/Polygons/images/circulo_cuadrado_calcular_pi.png" alt="Example of how to calculate Pi from a polygon" height="250" style="display: block; margin: auto;"/></center></div>

And how can we calculate the length of the sides of a regular polygon? To do so we have to go one by one duplicating the number of sides. That is because we have to use the theorem of Pitagoras to get the value of each side. To understand better this, please see the following example, where we start with a square, the basic polygon in this problem, and then we follow with a polygon with 8 sides. And which circle are we going to use? The simplest way is to use one circle with D=1, so the perimiter of the circle is equals to Pi ('P = 2·r·pi => P = D·pi' so if D=1, 'P = pi').

// Continue ...
