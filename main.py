from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def white():
    return "hello world"
    #return render_template('xxx.html')
    #html���������ͬ����templates�ļ�����


if __name__ == "__main__":
    app.run(host="0.0.0.0")#��Ӳ����Թ�������������
    #app.run(debug=True,use_reloader=False)
