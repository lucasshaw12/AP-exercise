#! python3

from PIL import ImageColor

#######################################
# Colours and RGBA values

# print(ImageColor.getcolor('red', 'RGBA'))
# print(ImageColor.getcolor('RED', 'RGBA'))
# print(ImageColor.getcolor('Black', 'RGBA'))
# print(ImageColor.getcolor('chocolate', 'RGBA'))
# print(ImageColor.getcolor('Cornflowerblue', 'RGBA'))

#######################################
# Coordinates and box tuples

from PIL import Image

# catIm = Image.open('zophie.png')
# print(catIm.size)
# width, height = catIm.size
# print(width, height)
# print(catIm.filename)
# print(catIm.format)
# print(catIm.format_description)
# catIm.save('newZophie.jpg')

# Create a simple image with block colour
# im = Image.new('RGBA', (100, 200), 'Purple')
# im.save('purpleImage.png')
# im2 = Image.new('RGBA', (20, 20)) # Transprent black as no background has been specified. 
# im2.save('transparentImage.png')

#######################################
# Cropping Images

# catIm = Image.open('zophie.png')
# croppedIm = catIm.crop((335, 345, 565, 560))
# croppedIm.save('cropped.png')

#######################################
# Copying and pasting images onto other images

# catIm = Image.open('zophie.png')
# # catCopyIm = catIm.copy()
# faceIm = catIm.crop((335, 345, 565, 560))
# # print(faceIm.size)
# # catCopyIm.paste(faceIm, (0, 0))
# # catCopyIm.paste(faceIm, (400, 500))
# # catCopyIm.save('pasted.png')

# # Looping with images
# catImWidth, catImHeight = catIm.size
# faceImWidth, faceImHeight = faceIm.size
# catCopyTwo = catIm.copy()
# for left in range(0, catImWidth, faceImWidth):
# 	for top in range(0, catImHeight, faceImHeight):
# 		print(left, top)
# 		catCopyTwo.paste(faceIm, (left, top))
# catCopyTwo.save('tiled.png')

#######################################
# Resizing an image

# catIm = Image.open('zophie.png')
# width, height = catIm.size
# quartersizedIm = catIm.resize((int(width / 2), int(width / 2)))
# quartersizedIm.save('quartersized.png')
# svelteIm = catIm.resize((width, height + 300))
# svelteIm.save('svelte.png')

#######################################
# Rotating and flipping images

# catIm = Image.open('zophie.png')
# catIm.rotate(90).save('rotated90.png')
# catIm.rotate(180).save('rotated180.png')
# catIm.rotate(270).save('rotated270.png')

# catIm.rotate(6).save('rotated6.png')
# catIm.rotate(6, expand=True).save('rotated6_expanded.png') # expand the image frame to fit

# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

#######################################
# Changing individual pixels

# im = Image.new('RGBA', (100, 100))
# print(im.getpixel((0, 0)))
# for x in range(100):
# 	for y in range(50):
# 		im.putpixel((x, y), (210, 210, 210))

# for x in range(100):
# 	for y in range(50, 100):
# 		im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

# print(im.getpixel((0, 0)))
# print(im.getpixel((0, 50)))
# im.save('putPixel.png')

#######################################
# Drawing shapes

# from PIL import Image, ImageDraw
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
# draw.rectangle((20, 30, 60, 60), fill='blue')
# draw.ellipse((120, 30, 160, 60), fill='red')
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
# for i in range(100, 200, 10):
# 	draw.line([(i, 0), (200, i - 100)], fill='green')
# im.save('drawing.png')

#######################################
# Drawing text

# from PIL import ImageFont, Image, ImageDraw
# import os

# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# draw.text((20, 150), 'Hello', fill='purple')
# fontsFolder = 'System/Library/Fonts' # specify location of the .ttf font file
# arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'Arial Unicode.ttf'), 32)
# draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
# im.save('text.png')




















