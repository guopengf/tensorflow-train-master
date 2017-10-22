#read and process images
from PIL import Image	

from numpy import *

def RGB2Grey(R,G,B):
	return   (255-((R*30 + G*59 + B*11 + 50) / 100))
#read images and return a value and a label
def GetImage(filename):
	width=28
	height=28
        print(filename)
	#the size of image: 28x28
	value=zeros([1,width,height,1])
	value[0,0,0,0]=-1
        #the number of image
	label=zeros([1,10])
	label[0,0]=-1
	#read images from file
        file_position="test_num"+"/"+filename
	img=array(Image.open(file_position).convert("L"))
	width,height=shape(img);
	index=0
	tmp_value=zeros([1,width,height,1])
	for i in range(width):
		for j in range(height):	
			tmp_value[0,i,j,0]=img[i,j]
			index+=1
		
	if(value[0,0,0,0]==-1):
		value=tmp_value
	else:
		value=concatenate((value,tmp_value))
	#recognize the input number	
	tmp_label=zeros([1,10])
	index=int(filename.split('_')[0])
	print "input:",index
	tmp_label[0,index]=1
	if(label[0,0]==-1):
		label=tmp_label
	else:
		label=concatenate((label,tmp_label))
	#return value and label to pridect a output number
	return array(value),array(label)



