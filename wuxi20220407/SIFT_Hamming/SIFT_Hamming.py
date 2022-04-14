import cv2
import numpy as np
from sklearn.cluster import KMeans


def kmeans_detect(file_list, cluster_nums, randomState=None): # KNN 线性分类器
    features = []
    files = file_list #特征检测
    sift = cv2.SIFT_create()#调用SIFT特征提取方法
    for file in files:
        img = cv2.imread(file)#读入文件
        img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_CUBIC)
        # 重新设计图片大小，cv2.resize(img,(2*width,2*height)），这个当中是使用的宽高，这里一定要注意。
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #灰度化处理
        # print(gray.dtype) #打印类型
        kp,des = sift.detectAndCompute(gray, None) #调用SIFT算法
        # 检测并计算描述符
        # Kp,des=sift.detectAndCompute(gray,None)#检测并计算描述符
        # des =sift.detect(gray, None)# sift.detectAndCompute(gray, None)
        # 找到后可以计算关键点的描述符
        # Kp, des = sift.compute(gray, des)

        if des is None:
            file_list.remove(file)
            continue
        reshape_feature = des.reshape(-1, 1)
        features.append(reshape_feature[0].tolist())

    input_x = np.array(features) #计算关键点
    kmeans = KMeans(n_clusters=cluster_nums, random_state=randomState).fit(input_x) #关键点聚类
    return kmeans.labels_, kmeans.cluster_centers_