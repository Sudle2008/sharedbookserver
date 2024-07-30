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

def list_all(name='%',user='%',clean=-1):
    exc=""
    if clean==0:
        exc="and clean=0"
    elif clean==1:
        exc="and clean=1"
    book_data=sqlite3.connect('./database/book.db')
    cursor=book_data.cursor()
    res = list(cursor.execute("select * from book where name like '"+name+"' and user like '"+user+"'"+exc).fetchall())
    cursor.close()
    return res
    
def delete_book(id,user):
    pass