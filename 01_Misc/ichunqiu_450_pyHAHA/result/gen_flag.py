from PIL import Image

str=open("data.txt","r").read()
length=240
width=30
pic=Image.new("RGB",(length,width))
i=0
for x in range(length):
	for y in range(width):
		if str[i] == '0':
			pic.putpixel([x,y],(0,0,0))
		else:
			pic.putpixel([x,y],(255,255,255))
		i += 1
pic.show()
pic.save("flag.png")