"""
图片识别为，将图片中的文字转换为字符串，一般用来处理规范的文字

"""
from PIL import Image
import pytesseract

file_path = "./baidu.png"

img = Image.open(file_path)

str = pytesseract.image_to_string(img)
print(str)