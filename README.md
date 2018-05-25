# devops
This file contains devops 
drawable_resizer.py helps you to create multiple drawables from XXXHDPI. This create images for xxhdpi, xhdpi, hdpi

Example:
Consider we have image for xxxhdpi ic_logo.png with dimension 272x272.
Run >>python drawable_resizer.py ic_logo.png
This create drawable-xxxhdpi,drawable-xxhdpi,drawable-xhdpi,drawable-hdpi images and add it to respective folders

Note:Required to install Python Image Library

pip install pillow

