import mysql.connector as sql
import pandas as pd
con=sql.connect(host="localhost",user="root",password="admin",database="airline")



def create_passenger():
    c1=con.cursor()
    c1.execute("""create table if not exists passenger(
               name varchar(25),
               address varchar(50),
               mobile varchar(15),
               rdate date,
               source varchar(25),
               destination varchar(25))""")
create_passenger()


def create_food():
    c1=con.cursor()
    c1.execute("""create table if not exists food(
               sno int(5) primary key,
               itemname varchar(20),
               rate varchar(20))""")
create_food()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


def menu():
    print()
    print("="*95)
    print("*"*40,"WELCOME TO FLIGHT MANAGEMENT SYSTEM","*"*40)
    print("1.  add new passenger detail")
    print("2.  display passenger detail")
    print("3.  delete passenger detail")
    print("4.  add food item details")
    print("5.  display food item detail")
    print("6.  search by food item name")
    print("7.  delete food item detail")
    print("8. total ticket price , food and luggage bill")
    print("9. Exit")
    print("="*95)
    print(" "*190)
    



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

def add_passenger():
    c1=con.cursor()
    while True:
        name=input('ENTER NAME: ')
        address=input("ENTER ADDRESS: ")
        phno=input("ENTER MOBILE: ")
        rdate=input("ENTER RESEVATION DATE: ")
        source=input("ENTER SOURCE: ")
        destination=input("ENTER DESTINATION: ")
        rec=(name,address,phno,rdate,source,destination)
        sql="insert into passenger values(%s,%s,%s,%s,%s,%s)"
        c1.execute(sql,rec)
        x=input('press y to add more records')
        if x not in 'y''Y':
            break
    con.commit()
    
    

def display_passenger():
    c1=con.cursor()
    x=("select* from passenger")
    c1.execute(x)
    x=c1.fetchall()
    for i in x:
        print(i)
    if c1.rowcount==0:
            print("no records exists in the the table")
    c1.close()
    


    

def delpass():
    c1=con.cursor()
    x=("select* from passenger")
    c1.execute(x)
    x=c1.fetchall()
    for i in x:
        print(i)
    while True:
        print(' '*200)
        print('-'*100)
        name=input("enter name to be deleted:  ")
        rec=(name,)
        s=(" delete from passenger where name=%s")
        c1.execute(s,rec)
        if c1.rowcount==0:
            print("no such records exists in the the table")
        else:
            print(c1.rowcount,"data deleted successfully")
        x=input("press y to delete more records")
        if x not in 'y''Y':
            break
    c1.close()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_food():
    c1=con.cursor()
    df=pd.read_sql("select * from food",con)
    print(df)
    while True:
        sno=input('ENTER SERIAL NO.:  ')
        itemname=input("ENTER NAME OF FOOD ITEM: ")
        rate=input("ENTER RATE OF FOOD ITEM PER PIECE:: ")
        rec=(sno,itemname,rate)
        sql="insert into food values(%s,%s,%s)"
        c1.execute(sql,rec)
        x=input('press y to add more records')
        if x not in 'y''Y':
            break
    con.commit()
    print('Record inserted in food')




def display_food():
    c1=con.cursor()
    x=("select* from food")
    c1.execute(x)
    x=c1.fetchall()
    for i in x:
        print(i)
    if c1.rowcount==0:
            print("no records exists in the the table")
    c1.close()




def search_byfooditem():
    print("ALL FOOD ITEMS AVAILABLE")
    df=pd.read_sql("select* from food",con)
    print(df)
    print('-'*100)
    print('search Rate of food item by entering food item no')
    a=int(input("Enter FOOD ITEM NO. : "))
    qry="select* from food where sno=%s;"%(a,)
    df=pd.read_sql(qry,con)
    print(df)




def delfood():
    c1=con.cursor()
    x=("select* from food")
    c1.execute(x)
    x=c1.fetchall()
    for i in x:
        print(i)
        print('-'*100)
    while True:
        print('*'*100)
        print('*'*100)
        itemname=input("enter itemname to be deleted:  ")
        rec=(itemname,)
        s=(" delete from food where itemname=%s")
        c1.execute(s,rec)
        if c1.rowcount==0:
            print("no such records exists in the the table")
        else:
            print(c1.rowcount,"data deleted successfully")
        x=input("press y to delete more records")
        if x not in 'y''Y':
            break
    c1.close()



def fnlbill():
    print(" WE HAVE THE FOLLOWING SEAT TYPES FOR YOU.")
    print("1. ECONOMY CLASS  RS5000 PER PERSON")
    print("2.FIRST CLASS RS 6000 PER PERSON")
    print("3. BUISNESS CLASS   RS11000 PER PERSON")
    print("4. KING ROOM  RS 16000 PER PERSON")
    x=int(input("ENTER YOUR CHOICE OF TICKET PLEASE--->"))
    n=int(input("HOW MANY TICKETS YOU NEED: "))
    if(x==1):
        print("YOU HAVE CHOOSEN FIRST CLASS")
        s=5000*n
    elif(x==2):
        print("YOU HAVE CHOOSEN BUSINESS CLASS")
        s=6000*n
    elif(x==3):
        print("YOU HAVE CHOOSEN ECONOMY CLASS")
        s=11000*n
    elif(x==4):
        print("YOU HAVE CHOOSEN KING ROOM")
        s=16000*n
    else:
        print("PLEASE CHOOSE A ROOM")
    print("YOUR TOTAL TICKET PRICE is =",s,"\n")
    
    print("1.  YOU HAVE 0 KG EXTRA")
    print("2.  YOU HAVE 1 KG EXTRA")
    print("3.  YOU HAVE 2 KG EXTRA")
    print("4.  YOU HAVE 5 KG EXTRA")
    print("5.  YOU HAVE 10 KG EXTRA")
    print("6.  YOU HAVE 15 KG EXTRA")
    x=int(input("ENTER SERIAL NO. OF WEIGHT OF EXTRA LUGGAGE->"))
    if(x==1):
        print("YOU HAVE 0 KG EXTRA")
        l=0
    elif(x==2):
        print("YOU HAVE 1 KG EXTRA")
        l=800
    elif(x==3):
        print("YOU HAVE 2 KG EXTRA")
        l=1800
    elif(x==4):
        print("YOU HAVE 5 KG EXTRA")
        l=3000
    elif(x==5):
        print("YOU HAVE 10 KG EXTRA")
        l=5000
    elif(x==6):
        print("YOU HAVE 15 KG EXTRA")
        l=7000
    else:
        print("PLEASE CHOOSE A CORRECT Serial No. ")

    print("your cost of extra luggage is",l)
    
    print ('ALL FOOD ITEMS AVAILABLE')
    df=pd.read_sql("select * from food",con)
    print(df)
    p=0
    while True:
        c=int(input("order your ITEM no. : "))
        d=int(input("enter the quantity : "))
        if (c==1):
            t = 50 * d
        elif (c==2):
            t = 150* d
        elif (c==3):
            t = 95 * d
        elif (c==4):
            t = 40 * d
        elif (c==5):
            t = 75 * d
        elif (c==6):
            t = 120 * d
        elif (c==7):
            t = 350 * d
        elif (c==8):
            t = 200 * d
        elif (c==9):
            t = 125 * d
        elif (c==10):
            t = 55 * d
        elif (c==11):
            t = 65 * d
        else:
            print("Invalid option")
        p+=t
        x=input("press y to delete more records")
        if x not in 'y''Y':
            break
    
    print("total food bill=Rs",p,"\n")
    print("grand total=Rs",s+l+p,"\n")
    


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
while True:
    menu()
    opt=int(input("enter your choice:  "))
    if opt==1:
        add_passenger()
    elif opt==2:
        display_passenger()
    elif opt==3:
        delpass()
    elif opt==4:
        add_food()
    elif opt==5:
        display_food()
    elif opt==6:
        search_byfooditem()
    elif opt==7:
        delfood()
    elif opt==8:
        fnlbill()     
    elif opt==9:
        break
    else:
        print('invalid option')

    


















