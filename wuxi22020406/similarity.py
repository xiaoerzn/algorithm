# !/usr/bin/env Python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: utf8 -*-

import json
import sys

#python3写法：
import importlib,sys
importlib.reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, paired_distances


def text_embedding():
    dic = {}
    for line in open("/home/bpfsrw_8/huanghan02/cutframe_0126_fsp1_out/text_out", "r"):
        data = json.loads(line.rstrip("\n"))
        text = data[0]
        embedding = data[1]
        dic[text] = embedding

    return dic


def sim(img_embedding, text_set):
    """
    calculate_similarity
    """

    candidate_simi_list = []
    # img_embedding = np.array([img_embedding])

    for key, value in list(text_set.items()):
        # candi_embedding = candidate_embedding_map[uri]
        cos_sim = 0.0

        text_embedding = np.array(value)
        # print text_embedding
        cos_q_e = cosine_similarity([img_embedding], [text_embedding])
        # print cos_q_e
        cos_sim = cos_q_e[0][0]
        candidate_simi_list.append([key, cos_sim])

    return candidate_simi_list


def image(text):
    dic_img = {"img": "", "embedding": "", "count": 0}
    for line in open("/home/bpfsrw_8/huanghan02/cutframe_0126_fsp1_out/part_out", "r"):
        data = json.loads(line.rstrip("\n"))
        image = data[0]
        # image = '/home/bpfsrw_7/yangfan53/tag/cutframe_0126_fsp1/cutvideo_0114_5w_part1-pl/mda-jc5rdf7kajrhxwz3_0/00004.jpg'
        img = image[:-10]
        embedding = np.array(data[1])

        if dic_img["img"] == img:
            tmp = np.sum([dic_img["embedding"], embedding], axis=0)
            dic_img["embedding"] = tmp
            dic_img["count"] += 1
            # print 111

        elif dic_img["img"] == "":
            dic_img = {"img": img, "embedding": embedding, "count": 1}
            # print 222

        else:
            # print dic_img["count"]
            # print dic_img["embedding"] / dic_img["count"]
            sim_list = sim(dic_img["embedding"] / dic_img["count"], text)
            sim_list = sorted(sim_list, key=(lambda x: x[1]), reverse=True)
            # print sim_list[0][1]
            # print sim_list[0][0]

            if sim_list[0][1] <= 0.3:
                sim_list[0][0] = "鍏朵粬"
            print(image[:-10] + "\t" + sim_list[0][0] + "\t" + str(sim_list[0][1]))

            dic_img = {"img": img, "embedding": embedding, "count": 1}

    sim_list = sim(dic_img["embedding"] / dic_img["count"], text)
    sim_list = sorted(sim_list, key=(lambda x: x[1]), reverse=True)

    if sim_list[0][1] <= 0.3:
        sim_list[0][0] = "鍏朵粬"
    print(image[:-10] + "\t" + sim_list[0][0] + "\t" + str(sim_list[0][1]))


if __name__ == "__main__":
    text = text_embedding()
    image(text)
