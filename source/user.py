import sqlite3

user_data=sqlite3.connect('./database/user.db')

def check_user(name,password):
    user_data=sqlite3.connect('./database/user.db')
    cursor=user_data.cursor()
    return 0

def add_user(name,password):
    user_data=sqlite3.connect('./database/user.db')
    cursor=user_data.cursor()
    a="insert into user (name,password) values ("+name+","+password+")"
    cursor.execute(a)
    return 1