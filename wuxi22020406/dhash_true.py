# !/usr/bin/env Python
# -*- coding: utf-8 -*-
import PIL
from PIL import Image
import os
import numpy as np
import time
import shutil



# 差异哈希算法
def dHash(image):
    image_new = image
    # 计算均值
    avreage = np.mean(image_new)
    hash = []
    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if image[i, j] > image[i, j + 1]:
                hash.append(1)
            else:
                hash.append(0)
    return hash


# 计算汉明距离
def Hamming_distance(hash1, hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num


if __name__ == "__main__":
    start = time.time()
    # 中间写上代码块
    dic = {}
    # 输入图片文件夹位置
    for root, dirs, files in os.walk("D:/project/code/AlgorithmProject/wuxi22020406/result/"):
        for dir in dirs:
            image_dir = "D:/project/code/AlgorithmProject/wuxi22020406/result/" + dir + '/screenshot/main.png'
            if not os.path.exists(image_dir):
                continue
            # 开始读取并处理图片   缩小尺寸并灰度化
            image1 = Image.open(image_dir)
            image1 = np.array(image1.resize((9, 8), Image.ANTIALIAS).convert('L'), 'f')
            hash1 = dHash(image1)
            dic[image_dir] = hash1

        # for image in files:
        #     if image == ".DS_Store":
        #         continue
        #     # 输入图片文件夹位置
        #     image_dir = "D:/project/code/AlgorithmProject/wuxi22020406/Img/" + image
        #
        #     # 开始读取并处理图片   缩小尺寸并灰度化
        #     image1 = Image.open(image_dir)
        #     image1 = np.array(image1.resize((9, 8), Image.ANTIALIAS).convert('L'), 'f')
        #     hash1 = dHash(image1)
        #     dic[image_dir] = hash1
    # print(dic)

    count = 1

    dic_done = {}
    for k, v in dic.items():
        # for image in files:
        if k in dic_done:
            continue

        image_dir = k
        if not image_dir:
            continue
        hash1 = v

        # 保存图片文件夹位置，按照计数命名，聚了几类就就计数几次
        tmp = "D:\project\code\AlgorithmProject\wuxi22020406\outImg\outImg" + str(count)
        if not os.path.exists(tmp):
            os.makedirs(tmp)
        shutil.copy(image_dir,os.path.join(tmp,k.split('/')[-3]+'.png'))
        # print(image_dir+"zzzzzzzzzzzzzzzz" + tmp)
        dic_done[k] = 1

        count += 1

        for key, value in dic.items():
            if not key:
                continue
            if key in dic_done:
                continue

            hash2 = value
            dist = Hamming_distance(hash1, hash2)

            # 将距离转化为相似度
            similarity = 1 - dist * 1.0 / 64

            print('dist is ' + '%d' % dist)
            print('{} and {} similarity is {}'.format(image_dir.split('/')[-3],key.split('/')[-3],str(similarity)))

            if similarity >= 0.9:
                shutil.copy(key,os.path.join(tmp,key.split('/')[-3]+'.png'))
                # print(key+"????????????????"+tmp)
                dic_done[key] = 1
    end = time.time()
    print('Running time: %s Seconds' % (end - start))




