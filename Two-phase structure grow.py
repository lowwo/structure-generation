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
                if (img[i,j]==0 and random.random()<prob1[2]):
                    img[i,j] = color
                    solid1x.append(i)
                    solid1y.append(j)
                    solid1_num = solid1_num + 1
            #向左上长
            if index_j > 1 and index_i > 1 :
                i = index_i - 1
                j = index_j - 1
                if (img[i,j]==0 and random.random()<prob1[3]):
                    img[i,j] = color
                    solid1x.append(i)
                    solid1y.append(j)
                    solid1_num = solid1_num + 1
            #向左长
            if index_j > 1:
                i = index_i
                j = index_j - 1
                if (img[i,j]==0 and random.random()<prob1[4]):
                    img[i, j] = color
                    solid1x.append(i)
                    solid1y.append(j)
                    solid1_num = solid1_num + 1
            #向左下长
            if index_j >1 and index_i < h-1 :
                i = index_i + 1
                j = index_j - 1
                if (img[i,j]==0 and random.random()<prob1[5]):
                    img[i,j] = color
                    solid1x.append(i)
                    solid1y.append(j)
                    solid1_num = solid1_num + 1
            #向下长
            if index_i < h - 1:
                i = index_i +1
                j = index_j
                if (img[i,j]==0 and random.random()<prob1[6]):
                    img[i,j] = color
                    solid1x.append(i)
                    solid1y.append(j)
                    solid1_num = solid1_num + 1
            #向右下长
            if index_i < h-1 and index_j <w-1 :
                i = index_i +1
                j = index_j +1
                if (img[i,j]==0 and random.random()<prob1[7]):
                    img[i,j] = color
                    solid1x.append(i)
                    solid1y.append(j)
                    solid1_num = solid1_num + 1
    return img



from PIL import Image
import numpy as np
import os

# 设定参数
cdd1 = 0.0001  # 成核概率
max_solid1 = 0.1  # 该相所占整体比例
prob1 = [0.5, 0.5, 0.5, 0.5, 0.0001, 0.0001, 0.0001, 0.0001]  # 四个方向生长概率，按逆时针转

path = r"E:\daore"

# 确保路径存在
os.makedirs(path, exist_ok=True)



# 生成并保存10张图片
for i in range(10,20):
    image_array = crytal_graw(max_solid1, cdd1, prob1)  # 调用函数生成图像数据
    image = Image.fromarray(image_array)  # 将 NumPy 数组转换为 PIL 图像
    file_name = os.path.join(path, f"crystal_image_{i+1}.png")  # 生成不同的文件名
    image.save(file_name)  # 保存图片
    print(f"Saved {file_name}")
