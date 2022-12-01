import pymysql as sql

def getConnection():
    return sql.connect(host='localhost',user='root',port=3306,database="flask_curd_operation")

def addData(t):
    con=getConnection()
    cur=con.cursor()
    q1="insert into register (email_id,username,password) values(%s,%s,%s)"
    cur.execute(q1,t)
    con.commit()
    con.close()

def fetchData():
    con=getConnection()
    cur=con.cursor()
    q1="select * from register"
    cur.execute(q1)
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def specificData(id):
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from register where id=%s",(id,))
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]

def updateData(t):
    con=getConnection()
    cur=con.cursor()
    q1="update register set email_id=%s,username=%s,password=%s where id=%s"
    cur.execute(q1,t)
    con.commit()
    con.close()

def deleteData(id):
    con=getConnection()
    cur=con.cursor()
    q1="delete from register where id=%s"
    cur.execute(q1,(id,))
    con.commit()
    con.close()