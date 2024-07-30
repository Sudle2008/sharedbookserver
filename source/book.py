import sqlite3

def check_user(name,password):
    book_data=sqlite3.connect('./database/book.db')
    cursor=book_data.cursor()
    pwd=cursor.execute("select password from user where name='"+name+"'").fetchone()
    cursor.close()
    print(pwd)
    if (password,)==pwd:
        return 1
    return 0

def add_book(name,place,user):
    book_data=sqlite3.connect('./database/book.db')
    cursor=book_data.cursor()
    try:
        cursor.execute("insert into book (name,place,clean,user) values ("+name+","+place+",0,"+user+")")
        book_data.commit()
        cursor.close()
        return 1
    except:
        cursor.close()
        return 0

def list_all():
    book_data=sqlite3.connect('./database/book.db')
    cursor=book_data.cursor()
    res = list(cursor.execute("select * from book").fetchall())
    cursor.close()
    return res
    