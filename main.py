#-*- coding : utf-8-*-

from flask import Flask,render_template,make_response,request,redirect
import source.user as database_user
import source.book as database_book

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

@app.route("/book/")
def book():
    acc=request.cookies.get('acc')
    book_list=database_book.list_all()
    return render_template('book.html',book_list=book_list,acc=acc)
    
@app.route("/book/add/")
def book_add():
    acc=request.cookies.get('acc')
    if acc=="1":
        username=request.cookies.get('username')
        bookname=request.values.get("bookname")
        place=request.values.get("place")
        if (not bookname) or (not place):
            return render_template('book_add.html')
        if database_book.add_book(bookname,place,username):
            return '''添加成功， <a href="/book/add/">点我继续添加</a>,  <a href="/book/">点我返回书籍页面</a>。'''
        else:
            return '''未知错误， <a href="javascript:location.reload()">点我重试</a>,  <a href="/book/">点我返回书籍页面</a>。'''
    else:
        return '''请先<a href="/login/">登录</a>。'''
    
@app.route("/book/delete/")
def book_delete():
    acc="1"
    book_id=request.values.get("id")
    if not book_id:
        return '''未选择删除书籍，<a href="/">返回首页</a>。'''
    try:
        username=request.cookies.get('username')
        password=request.cookies.get('password')
        status=database_user.check_user(username,password)
        print(status)
        if status==1:
            if database_book.delete_book(book_id,username):
                return '''删除成功，请关闭此标签页'''
            else:
                return '''删除失败，可能原因：<br/>1、您尝试删除他人书籍<br/>2、书籍已经删除<br/>3、未知原因，请联系管理员'''
        elif status==0:
            raise Exception("Wrong User")
        else:
            raise Exception("UNKNOWN WRONG")
    except:
        return '''请重新<a href="/login/">登录</a>。'''
    
@app.route("/book/clean/")
def book_clean():
    acc="1"
    book_id=request.values.get("id")
    clean=request.values.get("to")
    if not book_id:
        return '''未选择书籍，<a href="/">返回首页</a>。'''
    if not clean:
        return '''未选择更改状态，<a href="/">返回首页</a>。'''
    try:
        username=request.cookies.get('username')
        password=request.cookies.get('password')
        status=database_user.check_user(username,password)
        print(status)
        if status==1:
            if database_book.clean_change(book_id,clean,username):
                return '''消毒状态更改成功，请关闭此标签页'''
            else:
                return '''状态更改失败，未知原因，请联系管理员'''
        elif status==0:
            raise Exception("Wrong User")
        else:
            raise Exception("UNKNOWN WRONG")
    except:
        return '''请重新<a href="/login/">登录</a>。'''

@app.route("/person/")
def person():
    acc=request.cookies.get('acc')
    if acc=="1":
        username=request.cookies.get('username')
        book_list=database_book.list_all(user=username)
        return render_template('person.html',username=username,book_list=book_list)
    else:
        return '''请先<a href="/login/">登录</a>。'''

if __name__ == "__main__":
    app.run(host="0.0.0.0")#添加参数以共享至局域网内
    #app.run(debug=True,use_reloader=False)
