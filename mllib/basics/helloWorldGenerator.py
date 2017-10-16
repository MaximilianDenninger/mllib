import Image, ImageFont, ImageDraw
import numpy as np
import os

def getText(input, size):
	result = ""
	font = ImageFont.truetype('arialbd.ttf', size) #load the font
	size = font.getsize(input)  #calc the size of text in pixels
	image = Image.new('1', size, 1)  #create a b/w image
	draw = ImageDraw.Draw(image)
	draw.text((0, 0), input, font=font) #render the text to the bitmap
	for rownum in range(size[1]):
		# scan the bitmap: print ' ' for black pixel and print '#' for white one
		line = []
		for colnum in range(size[0]-1):
			if image.getpixel((colnum, rownum)):
				line.append(' '),
			else:
				line.append('#'),
		currentLine = ''.join(line)
		for ele in currentLine:
			if ele == "#":
				if rownum != size[1] - 1:
					result += currentLine + "\n"
				else:
					result += currentLine
				break
	return result

newX = []
newY = []
text = getText("Hello World!",80)
lineCounter = len(text.split('\n'))
for line in text.split('\n'):
	eleCounter = 0
	for ele in line:
		if ele == "#":
			newX.append(eleCounter)
			newY.append(lineCounter)
		eleCounter += 1
	lineCounter -= 1
data = np.append(np.array(newX), np.array(newY)).reshape(2,len(newX)).transpose()

dir_path = os.path.dirname(os.path.realpath(__file__))
dataAsText = ""
for line in data:
	dataAsText += str(line[0]) + "," + str(line[1]) + ",0\n"
with open(os.path.join(dir_path, "..","..", "data", "testData.txt"),'w') as file:
	file.write(dataAsText)