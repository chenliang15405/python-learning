"""


"""
"复制小文件"
# 1. 打开
file_read = open("README")
file_write = open("README_COPY", "w")

# 读 写
text = file_read.read()
file_write.write(text)

# 关闭
file_read.close()
file_write.close()


"复制大文件"

# 1. 打开
file_read = open("README")
file_write = open("README_COPY", "w")

# 读 写
while True:
    text = file_read.readline()

    if not text:
        break

    file_write.writelines(text)

# 关闭
file_read.close()
file_write.close()







