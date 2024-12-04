import numpy as np
import cv2.cv2 as cv2
import random


#产生生长核
def crystal_nucleus(cdd,image,color):
    solid_num = 0
    h,w = image.shape
    solidx = []
    solidy = []
    # 第一遍遍历，确定生长核，并记录在列表soild_xy
    for i in range(h):
        for j in range(w):
            cdd_random = random.random()
            # print(cdd1)
            if cdd_random<cdd:
                image[i,j] = color
                solid_num = solid_num + 1
                # print(solid_num)
                solidx.append(i)
                solidy.append(j)
    return image,solid_num,solidx,solidy


#按四个方向定义的去生长
def crytal_graw(max_solid1,cdd1,prob1):
    img = np.zeros([500, 500], np.uint8)
    img,solid1_num,solid1x,solid1y = crystal_nucleus(cdd1,img,255)
    img = grow(img,max_solid1,solid1x,solid1y,solid1_num,prob1,255)
    return img


#生长函数
def grow(img,max_solid1,solid1x,solid1y,solid1_num,prob1,color):
    h,w = img.shape
    max_solid1 = h*w*max_solid1
    while solid1_num <= max_solid1:
        for index in range(len(solid1x)):
            index_i = solid1x[index]
            index_j = solid1y[index]
            # print(index_i)
            #向右长
            if index_j < w-1:
                i = index_i
                j = index_j + 1  #向右移动一位
                if (img[i,j]==0 and random.random()<prob1[0]):
                    img[i,j] = color
                    solid1x.append(i)
                    solid1y.append(j)
                    solid1_num = solid1_num + 1
            #向右上长
            if index_j < w-1 and index_i > 1 :
                i = index_i - 1
                j = index_j + 1
                if (img[i,j]==0 and random.random()<prob1[1]):
                    img[i,j] = color
                    solid1x.append(i)
                    solid1y.append(j)
                    solid1_num = solid1_num + 1
            #向上长
            if index_i > 1:
                i = index_i - 1
                j = index_j
                if (img[i,j]==0 and random.random()<prob1[2]
