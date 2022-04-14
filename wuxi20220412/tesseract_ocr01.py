from PIL import Image
import pytesseract
# 命令行参数解析包
import argparse

import cv2
import os

# 构造参数解析并解析参数
ap = argparse.ArgumentParser()
#使用 argparse 的第一步是创建一个 ArgumentParser 对象。
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# 加载示例图像并将其转换为灰度
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)

# 检查是否应该应用阈值来预处理 image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# 做一个检查，看看是否中间模糊应该做删除
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)

# 将灰度图像作为临时文件写入磁盘，这样我们就可以
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# 加载PIL/Pillow图像，应用OCR，然后删除临时文件
text = pytesseract.image_to_string(Image.open(filename),lang="chi_sim")
os.remove(filename)
print(text)

# 显示输出图像
# cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)

# 命令执行
# python tesseract_ocr01.py --image img.png

