#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:02:45 2018

@author: twj
"""
import cv2
import glob
import argparse
def crop(image,path):
    imgName = image.split('/')[3]
    imgName = imgName.split('.')[0]
    print imgName
    img = cv2.imread(image, 1)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    #1296*966  左上角（324,241）中上（324,483）右上（324,724）
    #          左中（648,241）中心点（648,483）右中（648,724）
    #          左下（972,241）中下（972,483）右下（972,724）
    #对原图进行裁剪
    #cv2.imshow('src', img)  
    crop1 = img[0:height/2,0:width/2]
    cv2.imwrite(path+imgName+'_'+str(1)+'.png', crop1)
    #cv2.imshow('左上', crop1)
    crop2 = img[0:height/2,width/4:width*3/4]
    cv2.imwrite(path+imgName+'_'+str(2)+'.png', crop2)
    #cv2.imshow('中上', crop2)
    crop3 = img[0:height/2,width/2:width]
    cv2.imwrite(path+imgName+'_'+str(3)+'.png', crop3)
    #cv2.imshow('右上', crop3)
    crop4 = img[height/4:height*3/4,0:width/2]
    cv2.imwrite(path+imgName+'_'+str(4)+'.png', crop4)
    #cv2.imshow('左中', crop4)
    crop5 = img[height/4:height*3/4,width/4:width*3/4]
    cv2.imwrite(path+imgName+'_'+str(5)+'.png', crop5)
   # cv2.imshow('中心', crop5)
    crop6 = img[height/4:height*3/4,width/2:width]
    cv2.imwrite(path+imgName+'_'+str(6)+'.png', crop6)
    #cv2.imshow('中右', crop6)
    crop7 = img[height/2:height,0:width/2]
    cv2.imwrite(path+imgName+'_'+str(7)+'.png', crop7)
    #cv2.imshow('左下', crop7)
    crop8 = img[height/2:height,width/4:width*3/4]
    cv2.imwrite(path+imgName+'_'+str(8)+'.png', crop8)
    #cv2.imshow('中下', crop8)
    crop9 = img[height/2:height,width/2:width]
    cv2.imwrite(path+imgName+'_'+str(9)+'.png', crop9)
    #cv2.imshow('右下', crop9)
    #对标签进行裁剪
if __name__ == '__main__':
  parser = argparse.ArgumentParser("./crop.py")
  parser.add_argument(
      '--data', '-d',
      type=str,
      required=True,
      help='orignal dataset',
  )
  parser.add_argument(
      '--out', '-o',
      type=str,
      required=True,
      help='augment dataset',
  )
  FLAGS, unparsed = parser.parse_known_args()
for _image in glob.glob(FLAGS.data+"/img/*"):
    print _image
    imgPath = _image
    crop(imgPath,FLAGS.out+'/img/')
for _image in glob.glob(FLAGS.data+"/lbl/*"):
    print _image
    imgPath = _image
    crop(imgPath,FLAGS.out+'/lbl/')
