from PIL import Image
import pytesseract
import cv2
import os


if __name__ == "__main__":
    for root, dirs, files in os.walk("D:/project/code/AlgorithmProject/wuxi20220412/Img/", topdown=False):
        for image in files:
            image_path = "D:/project/code/AlgorithmProject/wuxi20220412/Img/"+image
            image_name = image.split('.')[0]
            img = cv2.imread(image_path)  # 读取图片 读进BGR格式
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #颜色空间转换灰度图像
            proImgFile = 'D:/project/code/AlgorithmProject/wuxi20220412/proImg03/'
            if not os.path.exists(proImgFile):
                os.makedirs(proImgFile)
            cv2.imwrite(proImgFile+'pro'+image, gray)  # 将图片保存
            text = pytesseract.image_to_string(gray, lang="chi_sim")  # 将图片中的文字转换成字符串
            ocrResultFile = 'D:/project/code/AlgorithmProject/wuxi20220412/result03/'
            if not os.path.exists(ocrResultFile):
                os.makedirs(ocrResultFile)
            f = open(ocrResultFile+image_name+'_result', 'w', encoding='utf-8')
            f.write(text)
            f.close()
            print(text) #打印输出