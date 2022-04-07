# !/usr/bin/env Python
# -*- coding: utf-8 -*-
import PIL
from PIL import Image
import os
import numpy as np
import time
from sklearn.metrics.pairwise import cosine_similarity, paired_distances


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


def cos_sim(img1, img2):
    """
    calculate_similarity
    """
    #
    candidate_simi_list = []
    # img_embedding = np.array([img_embedding])

    # for key, value in text_set.items():
        # candi_embedding = candidate_embedding_map[uri]
        # cos_sim = 0.0

    # img1_emb = np.array(img1)
    # img2_emb = np.array(img2)
        # print text_embedding
    cos_q_e = cosine_similarity(img1, img2)
        # print cos_q_e
    cos_sim = cos_q_e[0][0]
        # candidate_simi_list.append([key, cos_sim])

    return cos_sim


if __name__ == "__main__":
    dic = {}
    # 输入图片文件夹位置
    for root, dirs, files in os.walk("/Users/huanghan02/Desktop/image/", topdown=False):
        for image in files:
            if image == ".DS_Store":
                continue
            # 输入图片文件夹位置
            image_dir = "/Users/huanghan02/Desktop/image/" + image

            # 开始读取并处理图片   缩小尺寸并灰度化
            image1 = Image.open(image_dir)
            image1 = np.array(image1.resize((9, 8), Image.ANTIALIAS).convert('L'), 'f')
            hash1 = dHash(image1)
            dic[image_dir] = image1
    # print(dic)

    count = 10

    dic_done = {}
    for k, v in dic.items():
        # for image in files:
        if k in dic_done:
            continue

        image_dir = k
        hash1 = v

        # 保存图片文件夹位置，按照计数命名，聚了几类就就计数几次
        tmp = "/Users/huanghan02/Desktop/" + str(count)
        if not os.path.exists(tmp):
            os.makedirs(tmp)
        os.system("cp " + image_dir + " " + tmp)
        dic_done[k] = 1

        count += 1

        for key, value in dic.items():
            if key in dic_done:
                continue

            hash2 = value
            dist = cos_sim(hash1, hash2)

            # 将距离转化为相似度
            similarity = 1 - dist * 1.0 / 64
            print('dist is ' + '%d' % dist)
            print('similarity is ' + str(similarity))

            if similarity >= 0.7:
                os.system("cp " + key + " " + tmp)
                dic_done[key] = 1




