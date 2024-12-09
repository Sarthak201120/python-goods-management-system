import mysql.connector
def createdb():
    mydb=mysql.connector.connect(host="localhost",user="root",password="8279")
    mycursor=mydb.cursor()
    mycursor.execute("create database if not exists goods_management")
    mycursor.execute("show databases")
    for i in mycursor:
        print(i)
def createtable():
    mydb=mysql.connector.connect(host="localhost",user="root",password="8279",database="goods_management")
    mycursor=mydb.cursor()
    sql1="create table if not exists customers(cid mediumint not null auto_increment,cname varchar(20) not null,doj date default(current_date),email varchar(50) not null,password varchar(20) not null,contact int not null,primary key(cid))"
    inc1="alter table customers auto_increment=199670"
    sql2="create table if not exists goods(cid integer,gid mediumint not null auto_increment,cname varchar(20),category varchar(50) not null,price int not null,details varchar(30),status char(4) default('A'),email varchar(50),contact int,primary key(gid))"
    inc2="alter table goods auto_increment=6753480"
    sql3="create table if not exists transactions(tid mediumint not null auto_increment,gid int,cname varchar(30),dot date default(current_date),contact int,primary key(tid))"
    inc3="alter table transactions auto_increment=5345480"
    mycursor.execute(sql1)
    mycursor.execute(inc1)
    mycursor.execute(sql2)
    mycursor.execute(inc2)
    mycursor.execute(sql3)
    mycursor.execute(inc3)
createdb()
createtable()

