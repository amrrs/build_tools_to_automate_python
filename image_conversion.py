# pip install Pillow
from PIL import Image  # Python Image Library - Image Processing 

import glob

print(glob.glob("*.png"))

# based on SO Answer: https://stackoverflow.com/a/43258974/5086335
for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=95)


'''

import os
for file in glob.glob("*.jpg"):
    os.remove(file)

'''
