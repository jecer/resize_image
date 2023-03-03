from pathlib import Path
from PIL import Image

path = Path('./')
resize = int(input('Enter resize size: '))
out_dir = path / 'resized'
out_dir.mkdir(exist_ok=True, parents=True)

ignore = ['.py', '.exe']
for item in path.iterdir():
    if item.is_dir():
        images_found = False
        for subitem in item.iterdir():
            if subitem.is_file() and subitem.suffix not in ignore and subitem.suffix.lower() in ['.jpg', '.png']:
                images_found = True
                image = Image.open(subitem)
                max_dimension = max(image.size)
                scale = resize / max_dimension
                new_size = (int(image.size[0] * scale), int(image.size[1] * scale))
                image = image.resize(new_size, Image.LANCZOS)
                if subitem.suffix == '.jpg':
                    image.save(out_dir / item.name / (subitem.stem + '.jpg'), quality=100)
                elif subitem.suffix == '.png':
                    image.save(out_dir / item.name / (subitem.stem + '.png'), quality=100)
        if not images_found:
            (out_dir / item.name).mkdir(exist_ok=True)
    elif item.is_file() and item.suffix not in ignore and item.suffix.lower() in ['.jpg', '.png']:
        image = Image.open(item)
        max_dimension = max(image.size)
        scale = resize / max_dimension
        new_size = (int(image.size[0] * scale), int(image.size[1] * scale))
        image = image.resize(new_size, Image.LANCZOS)
        if item.suffix == '.jpg':
            image.save(out_dir / (item.stem + '.jpg'), quality=100)
        elif item.suffix == '.png':
            image.save(out_dir / (item.stem + '.png'), quality=100)
