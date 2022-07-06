import PIL
from PIL import Image
import os.path

path = './img'
dirs = os.listdir(path)
out = './img/resize'
resize = int(input('Width: '))


def crop():
    for item in dirs:
        fullpath = os.path.join(path, item)
        outhome = os.path.join(out, item)
        if os.path.isfile(fullpath):
            img = Image.open(fullpath)
            f, e = os.path.splitext(outhome)
            size = resize
            wpercent = (size / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((size, hsize), PIL.Image.ANTIALIAS)
            img.save(f + '_Cropped.jpg', quality=100)


crop()
