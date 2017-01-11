#coding:gbk
'''
Created on 2017��1��11��

@author: coldJune
'''

from PIL import Image
import os
#�����ļ�·��
inputPath='./../../beforeImage/'
#����ļ�·��
outputPath='./../../afterImage/'

'''
    inputPath������Ŀ¼
    outputPath�����Ŀ¼
    file_name���ļ���
    imgtype���ļ�����
'''

def processImage(inputresource,outputresource,file_name,imgtype):
    imgtype='jpeg' if imgtype=='jpg' else 'png'
    #��ͼƬ
    im=Image.open("r"+inputresource+file_name)
    
    #���ű���
    rate=max(im.size[0]/640.0 if im.size[0]>640 else 0,im.size[1]/1136.0 if im.size[1]>1136 else 0)
    
    if rate:
        im.thumbnail((im.size[0]/rate,im.size[1]/rate))
    im.save("r"+outputresource+file_name,imgtype)


def run():
    #�л���ԴĿ¼������ԴĿ¼������ͼƬ
    os.chdir(inputPath)
    for i  in os.listdir(os.getcwd()):
        #����׺
        postfix=os.path.splitext(i)[1]
        if postfix == '.jpg' or postfix == '.png':
            processImage(inputPath, outputPath,i, postfix)
            

if __name__=='__main__':
    run()