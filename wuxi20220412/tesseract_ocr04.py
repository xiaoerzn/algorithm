from PIL import Image
import pytesseract
import cv2
import os





if __name__ == "__main__":
    for root, dirs, files in os.walk("D:/project/code/AlgorithmProject/wuxi20220412/Img/", topdown=False):
        for image in files:
            image_path = "D:/project/code/AlgorithmProject/wuxi20220412/Img/" + image
            image_name = image.split('.')[0]
            img = cv2.imread(image_path)  # 读取图片 读进BGR格式
            x, y = img.shape[0:2]
            img = cv2.resize(img, (int(y * 2), int(x * 2)), interpolation=cv2.INTER_CUBIC)  # 放大
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 颜色空间转换灰度图像
            # 模糊化
            # img = cv2.bilateralFilter(img, 9, 75, 75)
            img = cv2.medianBlur(img, 3)
            # 自适应阈值
            img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            proImgFile = 'D:/project/code/AlgorithmProject/wuxi20220412/proImg04/'
            if not os.path.exists(proImgFile):
                os.mkdir(proImgFile)
            cv2.imwrite(proImgFile + 'pro' + image, img)  # 将图片保存
            text = pytesseract.image_to_string(img, lang="chi_sim")  # 将图片中的文字转换成字符串
            resultFile = 'D:/project/code/AlgorithmProject/wuxi20220412/result04/'
            if not os.path.exists(resultFile):
                os.makedirs(resultFile)
            f = open(resultFile + image_name + '_result', 'w', encoding='utf-8')
            f.write(text)
            f.close()
            # print(text) # 打印输出
