from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # all 函数接收一个列表，如果都有值，才算为真
    if not all([username, password]):
        resp = {
            "code": 1,
            "message": "invalid params"
        }
        return jsonify(resp)

    if username == "admin" and password == "admin":
        resp = {
            "code": 0,
            "message": "login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "login error"
        }
        return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True)
