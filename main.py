from PIL import Image

img = Image.open('baby.jpeg')

area = (408, 433, 444, 504)

cropped_img = img.crop(area)

# image.show()
cropped_img.show()
