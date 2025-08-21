import os
from PIL import Image

input_folder = './Pokedex'
output_folder = 'Processed'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.jpg'):
        jpeg_path = os.path.join(input_folder, filename)
        png_filename = os.path.splitext(filename)[0] + '.png'
        png_path = os.path.join(output_folder, png_filename)

        # Open the image with context manager
        with Image.open(jpeg_path) as img:
            if img.mode == 'RGBA':
                # Create a white background image
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])  # Use alpha as mask
                background.save(png_path, 'PNG')
            else:
                img.convert('RGB').save(png_path, 'PNG')

        print(f'Converted {filename} to {png_filename}')
    # print(os.listdir(input_folder))

#SECOND METHOD
import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os. listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f' {output_folder}{clean_name}.png', 'png')
    print('all done!')





