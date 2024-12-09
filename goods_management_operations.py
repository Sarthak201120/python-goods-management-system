import mysql.connector
def menu():
    print("*********************************** WELCOME! ********************************** \n************************ YOU CAN BUY AND SELL GOODS HERE ************************************")
    print("1. Register \n2. Login \n3. Exit \n")
    c=int(input("Enter Your Choice (1-3): "))
    if c==1:
        register()
        menu2()
    elif c==2:
        login()
        menu2()
    elif c==3:
        print("******* Thank You For Using Our Service ********")
    else:
        print("\n******* Please Type The Number Between 1-3 ********\n")
        menu()
def register():
    mydb=mysql.connector.connect(host="localhost",user="root",password="8279",database="goods_management")
    print("\n******* REGISTRATION *********")
    came=input("Enter Your Name        : ")
    global emil
    emil=input("Enter Your Email       : ")
    conct=int(input("Enter Your Contact No  : "))
    passwd=input("Create Your Password   : ")
    l=[came,emil,conct,passwd]
    Input="insert into customers(cname,email,contact,password) values(%s,%s,%s,%s)"
    print("******** You Have Been Registered *********\n")
    mycursor=mydb.cursor()
    mycursor.execute(Input,l)
    mydb.commit()
        
def login():
    import mysql.connector
    m=mysql.connector.connect(host="localhost",user="root",password="8279",database="goods_management")
    global a
    a=input("Email     : ")
    b=input("Password  : ")
    mycursor=m.cursor()
    mycursor.execute("select email,password from customers")
    x=mycursor.fetchall()
    for e in x:
        if e[0]==a and e[1]==b:
            print("*********Succesful Login**********\n")
            break
    else:
        print("Enter a Valid Email and Password \n")
        login()
def menu2():
    print("1. Buy Item \n2. Sell Item \n3. View All Transactions \n4. View Items Listed For Selling \n5. Logout")
def buy():
    print("1. Car \n2. Bike \n3. Bicycle ")
    mydb=mysql.connector.connect(host="localhost",user="root",password="8279",database="goods_management")
    mycursor=mydb.cursor()
    s=input("Choose Your Cateregory : ")
    if s=="1" or s=="Car" or s=="car":
        print("CUSTOMER ID\tGOODS ID\t\tNAME\t\tPRICE\t\tDETAILS\t\tEMAIL\t\tCONTACT")
        mycursor.execute("select cid,gid,cname,price,details,email,contact from goods where category='car' or category='bike'")
        for e in mycursor:
            for ch in e:
                print(ch,end=" \t\t ")
            print()
    elif s=="2" or s=="Bike" or s=="bike":
        print("CUSTOMER ID\tGOODS ID\tNAME\t\tPRICE\t\tDETAILS\t\tEMAIL\t\tCONTACT")
        print()
        mycursor.execute("select cid,gid,cname,price,details,email,contact from goods where category='bike'")
        for e in mycursor:
            for ch in e:
                print(ch,end="\t")
            print()
    elif s=="3" or s=="Bicycle" or s=="bicycle":
        print("CUSTOMER ID\tGOODS ID\tNAME\t\tPRICE\t\tDETAILS\tEMAIL\t\tCONTACT")
        print()
        mycursor.execute("select cid,gid,cname,price,details,email,contact from goods where category='bicycle'")
        for e in mycursor:
            for ch in e:
                print(ch,end="\t\t")
            print()        
    else:
        print("please enter choice between 1-3\n")
        buy()
def logout():
    print("****************************** Logout Successful ************************************\n")
    menu()
def sell():
    cate=input("Category of Item(in lower case: )")
    pri=int(input("Enter Price of Item: "))
    det=input("Enter Details of Item: ")
    ema=input("email")
    l=[cate,pri,det,ema]
    mydb=mysql.connector.connect(host="localhost",user="root",password="8279",database="goods_management")
    mycursor=mydb.cursor()
    m="insert into goods(category,price,details,email) values(%s,%s,%s,%s)"
    mycursor.execute(m,l)
    mycursor.execute("update customers,goods set goods.cid=customers.cid,goods.cname=customers.cname,goods.contact=customers.contact where customers.email=goods.email")
    mydb.commit()
logout()
