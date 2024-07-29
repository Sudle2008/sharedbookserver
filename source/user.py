import sqlite3

user_data=sqlite3.connect('./database/user.db')

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
    cursor.execute("insert into user (name,password) values ("+name+","+password+")")
    cursor.close()
    user_data.commit()
    return 1