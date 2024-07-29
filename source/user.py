import sqlite3

user_data=sqlite3.connect('./database/user.db')

def check_user(name,password):
    user_data=sqlite3.connect('./database/user.db')
    cursor=user_data.cursor()
    return 1

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