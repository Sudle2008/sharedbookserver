import sqlite3

def check_user(name,password):
    user_data=sqlite3.connect('./database/user.db')
    cursor=user_data.cursor()
    pwd=cursor.execute("select password from user where name='"+name+"'").fetchone()
    print(pwd)
    if (password,)==pwd:
        return 1
    return 0

def add_user(name,password):
    user_data=sqlite3.connect('./database/user.db')
    cursor=user_data.cursor()
    user=cursor.execute("select name from user where name='"+name+"'").fetchone()
    print(user)
    if user:
        return 2
    print("insert into user (name,password) values ('"+name+"','"+password+"')")
    cursor.execute("insert into user (name,password) values ('"+name+"','"+password+"')")
    cursor.close()
    print(111)
    user_data.commit()
    print(222)
    return 1
