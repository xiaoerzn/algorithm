from PIL import Image
import pytesseract
import cv2

if __name__ == "__main__":
    path = "Img/img_1.png"  # 设置图片路径
    img = cv2.imread(path)  # 读取图片
    text = pytesseract.image_to_string(img, lang="chi_sim")  # 将图片中的文字转换成字符串
    # text = pytesseract.image_to_string(Image.open(path),lang="chi_sim")


    print(text) #打印输出