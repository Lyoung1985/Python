# coding=gbk
'''
Created on 2017��1��7��
@author:
'''
from PIL import Image,ImageDraw,ImageFont

#�ļ�������·�����ļ����·������Ӧ�ļ���
inputSrc="./../../inputImg/"
outputSrc="./../../outputImg/"
fontSrc="./../../fonts/STXINGKA.TTF"
inputFile="qztmp.jpg"
outputFile="output.jpg"

 #��������
im=Image.open(inputSrc+inputFile)

draw = ImageDraw.Draw(im)

#��ͼƬ��Сȷ�������С
fontsize=50

#��������
fontobj=ImageFont.truetype(font=fontSrc, size=fontsize, index=0, encoding="")
draw.text((im.size[0]-fontsize,0),text="9", fill=(255,0,0), font=fontobj)

im.save(outputSrc+outputFile)

im.show()
