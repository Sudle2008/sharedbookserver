from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def white():
    return "hello world"
    #return render_template('xxx.html')
    #html在与服务器同级的templates文件夹下


if __name__ == "__main__":
    app.run(host="0.0.0.0")#添加参数以共享至局域网内
    #app.run(debug=True,use_reloader=False)
