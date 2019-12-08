"""
文件上传

"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    file_obj = request.files.get("pic")
    if file_obj is None:
        return "未上传文件"

    # 读取文件的方式保存文件
    # with open("./demo.png", "wb") as f:
    #     f.write(file_obj.read())

    # 可以直接通过save()方法保存文件
    file_obj.save("./demo1.png")

    return "上传成功"


if __name__ == '__main__':
    app.run(debug=True)








