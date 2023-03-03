import os
from PIL import Image

path = './'
out = './resize'
resize = int(input('Size: '))


def process_image(image_path, output_path):
    img = Image.open(image_path)
    f, e = os.path.splitext(output_path)
    if img.size[1] > img.size[0]:
        size = resize
        wpercent = (size / float(img.size[1]))
        hsize = int((float(img.size[0]) * float(wpercent)))
        img = img.resize((hsize, size), Image.LANCZOS)
        img.save(f + '.jpg', quality=100)
    else:
        size = resize
        wpercent = (size / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((size, hsize), Image.LANCZOS)
        img.save(f + '.jpg', quality=100)


for root, dirs, files in os.walk(path):
    for file in files:
        fullpath = os.path.join(root, file)
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            outdir = os.path.join(out, os.path.relpath(root, path))
            os.makedirs(outdir, exist_ok=True)
            outfile = os.path.join(outdir, file)
            process_image(fullpath, outfile)
