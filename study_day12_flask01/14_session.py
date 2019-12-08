from flask import Flask, session

app = Flask(__name__)

# flask中的session需要配置秘钥，因为flask中的session其实是保存在cookie中浏览器端，所以需要设置秘钥
app.config["SECRET_KEY"] = "fdskljfkdsirwrwrwr"


@app.route("/set_session")
def index():
    session["name"] = "python"
    session["pwd"] = "123"
    return "login success"


@app.route("/get_session")
def index():
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run()
