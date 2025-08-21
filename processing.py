from PIL import Image, ImageFilter

img = Image.open("./Processed/pic02.jpg")
sharpen_img = img.filter(ImageFilter.SHARPEN)
sharpen_img.save("./Processed/pic03.jpg")
