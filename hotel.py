import datetime
import xlrd
import xlwt
from xlutils.copy import copy
y="n"
while(True):
    print("Welcome to hotel Oberoi hotels")
    y=input("WELCOME\nTo continue press Y else press N:")
    if(y=="Y"):
        a=xlrd.open_workbook("atmsheet.xls")
        b=a.sheet_by_index(0)
        c=copy(a)
        d=c.get_sheet(0)
        ch=0
        ch=int(input("1.Check in\n2.Check out"))
        if(ch==1):
            i=0
            u=input("Enter username:")
            d.write(i,0,u)
            op=0
            op=int(input("1.single\n2.double\n3.triple\n4.quad\n5.queen\n6.king"))
            room_no=b.cell_value(i,1)
            d.write(i,1,room_no)
            time_of_entry=datetime.datetime.now()
            d.write(i,2,time_of_entry)
            c.save("atmsheet.xls")
            print("per day charge is:200 bucks")
            print("available room according to your choosed option is",room_no)
            print(time_of_entry)
        else:
            j=6
            v=input("Enter username:")
            d.write(j,0,v)
            r=input("Enter your aadhar number:")
            d.write(j,1,r)
            t=input("your total stay is from in hours")
            d.write(j,2,t)
            m=(t*200)
            print("total money to pay",m)
            d.write(j,3,m)
            c.save("atmsheet.xls")
    else:
        print("THANK YOU!!")
        break
