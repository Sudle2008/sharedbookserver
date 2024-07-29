#-*- coding : utf-8-*-

from flask import Flask,render_template,make_response,request,redirect
import source.user as database_user

app = Flask(__name__)

@app.route("/")
def mainpage():
    acc="1"
    try:
        username=request.cookies.get('username')
        password=request.cookies.get('password')
        status=database_user.check_user(username,password)
        if status==1:
            pass
        elif status==0:
            raise Exception("Wrong User")
        else:
            raise Exception("UNKNOWN WRONG")
    except:
        acc="0"
        username="EMPTY"
        password="EMPTY"
    res=make_response(render_template('mainpage.html',username=username,password=password,acc=acc))
    res.set_cookie("acc",str(acc),max_age=3600)
    return res

@app.route("/login/",methods=["GET","POST"])
def login():
    acc=request.cookies.get('acc')
    warning=""
    if request.method=="POST":
        try:
            username=request.form['name']
            password=request.form['password']
            status=database_user.check_user(username,password)
            if status==1:
                res=make_response('''登录成功，<a href="/">点我返回主页</a>。''')
                res.set_cookie("username",username,max_age=3600)
                res.set_cookie("password",password,max_age=3600)
                res.set_cookie("acc","1",max_age=3600)
                return res
            elif status==0:
                warning="用户名或密码错误"
            else:
                raise Exception("UNKNOWN WRONG")
        except:
            warning="未知错误，请稍后重试或联系管理员"
    return render_template('login.html',warning=warning,acc=acc)

@app.route("/register/",methods=["GET","POST"])
def register():
    acc=request.cookies.get('acc')
    warning=""
    if request.method=="POST":
        try:
            username=request.form['name']
            password=request.form['password']
            status=database_user.add_user(username,password)
            if status==1:
                return '''注册成功，请<a href="/login/">跳转登录</a>。'''
            elif status==2:
                warning="该用户名已被注册"
            else:
                raise Exception("UNKNOWN WRONG")
        except:
            warning="未知错误，请稍后重试或联系管理员"
    return render_template('register.html',warning=warning,acc=acc)

@app.route("/logout/")
def logout():
    res=make_response('''退出登录成功，<a href="/">点我返回主页</a>''')
    res.set_cookie("acc","0",max_age=3600)
    res.delete_cookie("username")
    res.delete_cookie("password")
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0")#添加参数以共享至局域网内
    #app.run(debug=True,use_reloader=False)
