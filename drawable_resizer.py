from PIL import Image
import os
import sys


# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio

def process():
	if len(sys.argv) <= 1:
		return
	file = sys.argv[1]
	try:
		img = Image.open(file)
	except Exception as e:
		print("Error on opening file")
		return
	
	xxxhdpi = 'drawable-xxxhdpi'
	xxhdpi = 'drawable-xxhdpi'
	xhdpi = 'drawable-xhdpi'
	hdpi = 'drawable-hdpi'
	fileName =  os.path.basename(file)
	print(fileName)
	filePath = '{}/{}'
	createFolder(xxxhdpi)
	resize(1.0,img,filePath.format(xxxhdpi,fileName))
	createFolder(xxhdpi)
	resize(0.75,img,filePath.format(xxhdpi,fileName))
	createFolder(xhdpi)
	resize(0.50,img,filePath.format(xhdpi,fileName))
	createFolder(hdpi)
	resize(0.37,img,filePath.format(hdpi,fileName))


def resize(percent,image,filePath):
	width = int(float(image.size[0])*percent)
	print(width)
	height = int((float(image.size[1])*float(percent)))
	print(height)
	newimage = image.resize((width,height), Image.ANTIALIAS)
	newimage.save(filePath)

def createFolder(folderName):
	try:
		os.stat(folderName)
	except Exception as e:
		os.makedirs(folderName)

process()






