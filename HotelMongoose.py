from tkinter import *
from tkinter import ttk
import pymongo
import datetime
from tkinter.messagebox import showerror,showinfo,showwarning
client=pymongo.MongoClient("mongodb://localhost:27017/") 
print(client)
db=client["PythonPart2"]
coll=db["HotelUserDetails"]
class HotelM:
    def __init__(self,root):
        self.actualTotal=IntVar()
        self.taxTotal=IntVar()
        self.total=IntVar()
        self.username=StringVar()
        self.phoneNumber=StringVar()
        self.gender=StringVar()
        self.roomtype=StringVar()
        self.mealtype=StringVar()
        self.bookId=IntVar()
        self.roomId=IntVar()
        self.totalDays=IntVar()
        self.person=IntVar()
        self.SearchByVal=StringVar()
        self.DeleteByVal=StringVar()
        self.UpadteByVal=StringVar()
        self.UpadteByval=IntVar()
        self.SearchByval=IntVar()
        self.DeleteByval=IntVar()

        self.usernameUpdt=StringVar()
        self.phoneNumberUpdt=StringVar()
        self.genderUpdt=StringVar()
        self.roomtypeUpdt=StringVar()
        self.mealtypeUpdt=StringVar()
        self.bookIdUpdt=IntVar()
        self.roomIdUpdt=IntVar()
        self.totalDaysUpdt=IntVar()
        self.personUpdt=IntVar()

        self.usernameSearch=StringVar()
        self.phoneNumberSearch=StringVar()
        self.genderSearch=StringVar()
        self.roomtypeSearch=StringVar()
        self.mealtypeSearch=StringVar()
        self.bookIdSearch=IntVar()
        self.roomIdSearch=IntVar()
        self.totalDaysSearch=IntVar()
        self.personSearch=IntVar()
        self.timeSearch=StringVar()
        self.dateSearch=StringVar()

        self.luxury=2000
        self.normal=1000
        self.dinner=500
        self.morning=250
        self.both=600
        self.Total=0
         
        self.root=root
        self.root.title("Hotel Managment System")
        self.root.geometry("1500x750+10+10")
        self.root.resizable(width="false",height="false")
        self.root.iconbitmap("HotelIcon.ico")
        self.FrameLeft=Frame(self.root,bg="grey")
        self.FrameLeft.place(x=0,y=0,height=750,width=300)
        self.FrameRight=Frame(self.root,bg="light grey")
        self.FrameRight.place(x=310,y=0,height=750,width=1190)
        self.AddButton=Button(self.FrameLeft,text="Add User",bg="blue",fg="white",font=("Calibri",20,"bold"),command=self.AddPage)
        self.AddButton.place(x=0,y=250,height=50,width=300)
        self.UpdateButton=Button(self.FrameLeft,text="Update User",bg="blue",fg="white",font=("Calibri",20,"bold"),command=self.UpdatePage)
        self.UpdateButton.place(x=0,y=310,height=50,width=300)
        self.SearchButton=Button(self.FrameLeft,text="Search User",bg="blue",fg="white",font=("Calibri",20,"bold"),command=self.SearchPage)
        self.SearchButton.place(x=0,y=370,height=50,width=300)
        self.DeleteButton=Button(self.FrameLeft,text="Delete User",bg="blue",fg="white",font=("Calibri",20,"bold"),command=self.DeletePage)
        self.DeleteButton.place(x=0,y=430,height=50,width=300)
        self.AllUserButton=Button(self.FrameLeft,text="All User",bg="blue",fg="white",font=("Calibri",20,"bold"),command=self.AllUserPage)
        self.AllUserButton.place(x=0,y=490,height=50,width=300)

    def AddPage(self):
        Frameup=Frame(self.FrameRight)
        Frameup.place(x=0,y=0,height=110,width=1190)
        HotelLabel=Label(Frameup,text="Python Managment Hotel",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelLabel.place(x=0,y=0,height=60,width=1190)
        HotelAdd=Label(Frameup,text="Room Booking",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelAdd.place(x=0,y=70,height=40,width=1190)
        Framedown=Frame(self.FrameRight,bg="light grey")
        Framedown.place(x=0,y=120,height=630,width=1190)   
        CustomerDetailsLabelFrame=LabelFrame(Framedown,text="Customer Details",bd=4,relief="ridge",font=("Calibri",20))
        CustomerDetailsLabelFrame.place(x=20,y=40,height=580,width=1160) 
        BookingIdLabel=Label(CustomerDetailsLabelFrame,text="Booking Id",font=("Calibri",20))
        BookingIdLabel.place(x=30,y=20,height=30,width=150)
        
        BookingIdEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.bookId)
        BookingIdEntry.place(x=230,y=20,height=35,width=300)

        RoomIdLabel=Label(CustomerDetailsLabelFrame,text="Room Id",font=("Calibri",20))
        RoomIdLabel.place(x=30,y=80,height=30,width=128)

        RoomIdEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.roomId)
        RoomIdEntry.place(x=230,y=80,height=35,width=300)

        UserNameLabel=Label(CustomerDetailsLabelFrame,text="Username",font=("Calibri",20))
        UserNameLabel.place(x=30,y=140,height=30,width=150)

        UserNameEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.username)
        UserNameEntry.place(x=230,y=140,height=35,width=300)

        UserPhoneLabel=Label(CustomerDetailsLabelFrame,text="Phone No.",font=("Calibri",20))
        UserPhoneLabel.place(x=30,y=200,height=30,width=155)

        UserPhoneEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.phoneNumber)
        UserPhoneEntry.place(x=230,y=200,height=35,width=300)

        GenderLabel=Label(CustomerDetailsLabelFrame,text="Gender",font=("Calibri",20))
        GenderLabel.place(x=43,y=260,height=30,width=100)

        GenderEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Male","Female","Others"],textvariable=self.gender)
        GenderEntry.place(x=230,y=260,height=35,width=300)
        GenderEntry['state'] = 'readonly'



        RoomTypeLabel=Label(CustomerDetailsLabelFrame,text="Room Type",font=("Calibri",20))
        RoomTypeLabel.place(x=47,y=320,height=30,width=135)

        RoomEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Luxury","Normal"],textvariable=self.roomtype)
        RoomEntry.place(x=230,y=320,height=35,width=300)
        RoomEntry['state'] = 'readonly'


        MealLabel=Label(CustomerDetailsLabelFrame,text="Meal",font=("Calibri",20))
        MealLabel.place(x=40,y=380,height=30,width=85)

        MealEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Morning","Dinner","Both"],textvariable=self.mealtype)
        MealEntry.place(x=230,y=380,height=35,width=300)
        MealEntry['state'] = 'readonly'


        DaysLabel=Label(CustomerDetailsLabelFrame,text="Total Days",font=("Calibri",20))
        DaysLabel.place(x=34,y=440,height=30,width=155)

        DaysEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.totalDays)
        DaysEntry.place(x=230,y=440,height=35,width=300)

        PersonLabel=Label(CustomerDetailsLabelFrame,text="Person",font=("Calibri",20))
        PersonLabel.place(x=600,y=20,height=30,width=130)

        PersonEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["1","2"],textvariable=self.person)
        PersonEntry.place(x=750,y=20,height=35,width=300)
        PersonEntry['state'] = 'readonly'

        PaymentDetailsFrame=LabelFrame(CustomerDetailsLabelFrame,text="Payment Details",font=("Calibri",20),fg="red")
        PaymentDetailsFrame.place(x=630,y=100,height=380,width=500)

        ActualTotalLabel=Label(PaymentDetailsFrame,text="Room Total",font=("Calibri",20))
        ActualTotalLabel.place(x=30,y=40,height=30,width=150)
        
        ActualTotalEntry=Entry(PaymentDetailsFrame,font=("Calibri",20),state=DISABLED,textvariable=self.actualTotal)
        ActualTotalEntry.place(x=230,y=40,height=35,width=200)

        TaxLabel=Label(PaymentDetailsFrame,text="Tax Total",font=("Calibri",20))
        TaxLabel.place(x=30,y=120,height=30,width=128)

        TaxEntry=Entry(PaymentDetailsFrame,font=("Calibri",20),state=DISABLED,textvariable=self.taxTotal)
        TaxEntry.place(x=230,y=120,height=35,width=200)

        TotalLabel=Label(PaymentDetailsFrame,text="Total",font=("Calibri",20),fg="red")
        TotalLabel.place(x=30,y=200,height=30,width=90)

        TotalEntry=Entry(PaymentDetailsFrame,font=("Calibri",20),fg="red",state=DISABLED,textvariable=self.total)
        TotalEntry.place(x=230,y=200,height=35,width=200)

        AddBtn=Button(CustomerDetailsLabelFrame,text="Book",bg="red",fg="white",font=("times new roman",25,"bold"),command=self.Booked)
        AddBtn.place(x=530,y=495,height=40,width=120)
        self.fetchData()


    def Booked(self):
        if(self.bookId.get()!="" and self.roomId.get()!="" and self.username.get()!="" and self.phoneNumber.get()!="" and self.gender.get()!="" and self.roomtype.get()!="" and self.mealtype.get()!="" and self.totalDays.get()!="" and self.person.get()!=""):
            if(len(self.phoneNumber.get())==10):
                data={'BookingId':self.bookId.get(),'RoomNo':self.roomId.get(),'Username':self.username.get(),'PhoneNumber':self.phoneNumber.get(),'Gender':self.gender.get(),'RoomType':self.roomtype.get(),'Meal':self.mealtype.get(),'TotalDays':self.totalDays.get(),'Person':self.person.get(),'BookDate':datetime.datetime.now()}
                coll.insert_one(data)
                # cur.execute("insert into hotelcustomerdetails(BookingId,RoomNo,Username,PhoneNumber,Gender,RoomType ,Meal,TotalDays,Person,BookDate,BookTime)values({},{},'{}','{}','{}','{}','{}',{},{},'{}','{}')".format(self.bookId.get(),self.roomId.get(),self.username.get(),self.phoneNumber.get(),self.gender.get(),self.roomtype.get(),self.mealtype.get(),self.totalDays.get(),self.person.get(),datetime.datetime.now(),datetime.datetime.now()))
                # db.commit()
                print("data Inserted")
                showinfo("Info","Data Inserted Successfully")
                if(self.roomtype.get()=="Luxury"):
                    self.Total=self.Total+self.luxury
                else:
                    self.Total=self.Total+self.normal

                if(self.mealtype.get()=="Morning"):
                    self.Total=self.Total+self.morning
                elif(self.mealtype.get()=="Dinner"):
                    self.Total=self.Total+self.dinner
                else:
                    self.Total=self.Total+self.both
                
                if(self.person.get()==1):
                    self.Total=self.Total*1
                else:
                    self.Total=self.Total*2
                
                self.Total=self.Total*(self.totalDays.get())
                self.actualTotal.set(self.Total)
                self.taxTotal.set(self.Total*0.05)
                self.total.set(self.actualTotal.get()+self.taxTotal.get())
                print(self.Total)      
            else:
                print("\nMobile Number Must Be Of 10 Digits")
                showerror("Error","Mobile Number Must Be Of 10 Digits")

        else:
            print("\nAll Field Reuired")
            showerror("Error","All Field Required")

    def UpdatePage(self):
        Frameup=Frame(self.FrameRight)
        Frameup.place(x=0,y=0,height=110,width=1190)
        HotelLabel=Label(Frameup,text="Python Managment Hotel",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelLabel.place(x=0,y=0,height=60,width=1190)
        HotelUpdate=Label(Frameup,text="Update Page",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelUpdate.place(x=0,y=70,height=40,width=1190)
        self.Framedown=Frame(self.FrameRight,bg="light grey")
        self.Framedown.place(x=0,y=120,height=630,width=1190)
        UpdateByLabel=Label(self.Framedown,text="Update By",font=("Calibri",20),bg="light grey")
        UpdateByLabel.place(x=200,y=10,height=30,width=150)   
        UpdateByEntry=ttk.Combobox(self.Framedown,font=("Calibri",20),values=["BookingId","RoomNo"],textvariable=self.UpadteByVal)
        UpdateByEntry['state']='readonly'
        UpdateByEntry.place(x=380,y=10,height=35,width=250)
        UpdateByEntryValue=Entry(self.Framedown,font=("Calibri",20),textvariable=self.UpadteByval)
        UpdateByEntryValue.place(x=650,y=10,height=35,width=300)

        UpdateByBtn=Button(self.Framedown,text="Search",bg="red",fg="white",font=("times new roman",25,"bold"),command=self.UpdateChck)
        UpdateByBtn.place(x=560,y=60,height=40,width=150)

    def UpdateChck(self):
        data=coll.find_one({"BookingId":self.UpadteByval.get()})
        if(data!=None):
            print("\nData Found")
            showinfo("Info","Data Found")
            self.UpdateData(data['BookingId'],data['RoomNo'],data['Username'],data['PhoneNumber'],data['Gender'],data['RoomType'],data['Meal'],data['TotalDays'],data['Person'],data['BookDate'],data['BookDate'])
        else:
            print("\nData Not Found")
            showwarning("Warning","Data Not Found")
            self.UpdatePage()
 
    def UpdateData(self,bookid,roomno,user,phone,gender,roomtype,meal,totaldays,person,date,time):
        CustomerDetailsLabelFrame=LabelFrame(self.Framedown,text="Customer Details",bd=4,relief="ridge",font=("Calibri",20))
        CustomerDetailsLabelFrame.place(x=20,y=130,height=490,width=1160) 
        BookingIdLabel=Label(CustomerDetailsLabelFrame,text="Booking Id",font=("Calibri",20))
        BookingIdLabel.place(x=30,y=20,height=30,width=150)
        
        BookingIdEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.bookIdUpdt,state=DISABLED)
        BookingIdEntry.place(x=230,y=20,height=35,width=300)

        RoomIdLabel=Label(CustomerDetailsLabelFrame,text="Room Id",font=("Calibri",20))
        RoomIdLabel.place(x=30,y=80,height=30,width=128)

        RoomIdEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.roomIdUpdt,state=DISABLED)
        RoomIdEntry.place(x=230,y=80,height=35,width=300)

        UserNameLabel=Label(CustomerDetailsLabelFrame,text="Username",font=("Calibri",20))
        UserNameLabel.place(x=30,y=140,height=30,width=150)

        UserNameEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.usernameUpdt)
        UserNameEntry.place(x=230,y=140,height=35,width=300)

        UserPhoneLabel=Label(CustomerDetailsLabelFrame,text="Phone No.",font=("Calibri",20))
        UserPhoneLabel.place(x=30,y=200,height=30,width=155)

        UserPhoneEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.phoneNumberUpdt)
        UserPhoneEntry.place(x=230,y=200,height=35,width=300)

        GenderLabel=Label(CustomerDetailsLabelFrame,text="Gender",font=("Calibri",20))
        GenderLabel.place(x=43,y=260,height=30,width=100)

        GenderEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Male","Female","Others"],textvariable=self.genderUpdt)
        GenderEntry.place(x=230,y=260,height=35,width=300)
        GenderEntry['state'] = 'readonly'



        RoomTypeLabel=Label(CustomerDetailsLabelFrame,text="Room Type",font=("Calibri",20))
        RoomTypeLabel.place(x=47,y=320,height=30,width=135)

        RoomEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Luxury","Normal"],textvariable=self.roomtypeUpdt)
        RoomEntry.place(x=230,y=320,height=35,width=300)
        RoomEntry['state'] = 'readonly'


        MealLabel=Label(CustomerDetailsLabelFrame,text="Meal",font=("Calibri",20))
        MealLabel.place(x=620,y=20,height=30,width=85)

        MealEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Morning","Dinner","Both"],textvariable=self.mealtypeUpdt)
        MealEntry.place(x=790,y=20,height=35,width=300)
        MealEntry['state'] = 'readonly'


        DaysLabel=Label(CustomerDetailsLabelFrame,text="Total Days",font=("Calibri",20))
        DaysLabel.place(x=620,y=80,height=30,width=145)

        DaysEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.totalDaysUpdt)
        DaysEntry.place(x=790,y=80,height=35,width=300)

        PersonLabel=Label(CustomerDetailsLabelFrame,text="Person",font=("Calibri",20))
        PersonLabel.place(x=610,y=140,height=30,width=130)

        PersonEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["1","2"],textvariable=self.personUpdt)
        PersonEntry.place(x=790,y=140,height=35,width=300)
        PersonEntry['state'] = 'readonly'

        UpdateBtn=Button(CustomerDetailsLabelFrame,text="Update",bg="red",fg="white",font=("times new roman",25,"bold"),command=self.update)
        UpdateBtn.place(x=530,y=405,height=40,width=120)

        self.usernameUpdt.set(user)
        self.phoneNumberUpdt.set(phone)
        self.genderUpdt.set(gender)
        self.roomtypeUpdt.set(roomtype)
        self.mealtypeUpdt.set(meal)
        self.bookIdUpdt.set(bookid)
        self.roomIdUpdt.set(roomno)
        self.totalDaysUpdt.set(totaldays)
        self.personUpdt.set(person)
 
    def update(self):
        myquery = { "BookingId": self.UpadteByval.get() }
        newvalues = { "$set": { 'Username':self.usernameUpdt.get(),'PhoneNumber':self.phoneNumberUpdt.get() ,'Gender':self.genderUpdt.get() ,'RoomType':self.roomtypeUpdt.get()  ,'Meal':self.mealtypeUpdt.get() ,'TotalDays':self.totalDaysUpdt.get() ,'Person' :self.personUpdt.get()}}
        coll.update_one(myquery, newvalues)
        print("\nUpdated Successfully")
        showinfo("Info","\nData Updated Successfully")

    def SearchPage(self):
        Frameup=Frame(self.FrameRight)
        Frameup.place(x=0,y=0,height=110,width=1190)
        HotelLabel=Label(Frameup,text="Python Managment Hotel",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelLabel.place(x=0,y=0,height=60,width=1190)
        HotelSearch=Label(Frameup,text="Search Page",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelSearch.place(x=0,y=70,height=40,width=1190)
        self.FramedownSearch=Frame(self.FrameRight,bg="light grey")
        self.FramedownSearch.place(x=0,y=120,height=630,width=1190) 
        SearchByLabel=Label(self.FramedownSearch,text="Search By",font=("Calibri",20),bg="light grey")
        SearchByLabel.place(x=200,y=10,height=30,width=150)   
        SearchByEntry=ttk.Combobox(self.FramedownSearch,font=("Calibri",20),values=["BookingId","RoomNo"],textvariable=self.SearchByVal)
        SearchByEntry['state']='readonly'
        SearchByEntry.place(x=380,y=10,height=35,width=250)
        SearchByEntryValue=Entry(self.FramedownSearch,font=("Calibri",20),textvariable=self.SearchByval)
        SearchByEntryValue.place(x=650,y=10,height=35,width=300)
        SearchBtn=Button(self.FramedownSearch,text="Search",bg="red",fg="white",font=("times new roman",25,"bold"),command=self.search)
        SearchBtn.place(x=560,y=60,height=40,width=150)


    def search(self):
        print(self.SearchByVal.get(),self.SearchByval.get())
        data=coll.find_one({'BookingId':self.SearchByval.get()})
        print(data)
        if(data!=None):
            print("\nData Found")
            showinfo("Info","Data Found")
            self.SearchData(data['BookingId'],data['RoomNo'],data['Username'],data['PhoneNumber'],data['Gender'],data['RoomType'],data['Meal'],data['TotalDays'],data['Person'],data['BookDate'],data['BookDate'])
        else:
            print("\nData Not Found")
            showwarning("Warning","Data Not Found")
            self.SearchPage()

    def SearchData(self,bookid,roomno,user,phone,gender,roomtype,meal,totaldays,person,date,time):
        CustomerDetailsLabelFrame=LabelFrame(self.FramedownSearch,text="Customer Details",bd=4,relief="ridge",font=("Calibri",20))
        CustomerDetailsLabelFrame.place(x=20,y=130,height=480,width=1160) 
        BookingIdLabel=Label(CustomerDetailsLabelFrame,text="Booking Id",font=("Calibri",20))
        BookingIdLabel.place(x=30,y=20,height=30,width=150)
        
        BookingIdEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.bookIdSearch,state=DISABLED)
        BookingIdEntry.place(x=230,y=20,height=35,width=300)

        RoomIdLabel=Label(CustomerDetailsLabelFrame,text="Room Id",font=("Calibri",20))
        RoomIdLabel.place(x=30,y=80,height=30,width=128)

        RoomIdEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.roomIdSearch,state=DISABLED)
        RoomIdEntry.place(x=230,y=80,height=35,width=300)

        UserNameLabel=Label(CustomerDetailsLabelFrame,text="Username",font=("Calibri",20))
        UserNameLabel.place(x=30,y=140,height=30,width=150)

        UserNameEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.usernameSearch,state=DISABLED)
        UserNameEntry.place(x=230,y=140,height=35,width=300)

        UserPhoneLabel=Label(CustomerDetailsLabelFrame,text="Phone No.",font=("Calibri",20))
        UserPhoneLabel.place(x=30,y=200,height=30,width=155)

        UserPhoneEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.phoneNumberSearch,state=DISABLED)
        UserPhoneEntry.place(x=230,y=200,height=35,width=300)

        GenderLabel=Label(CustomerDetailsLabelFrame,text="Gender",font=("Calibri",20))
        GenderLabel.place(x=43,y=260,height=30,width=100)

        GenderEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Male","Female","Others"],textvariable=self.genderSearch,state=DISABLED)
        GenderEntry.place(x=230,y=260,height=35,width=300)
        GenderEntry['state'] = 'readonly'



        RoomTypeLabel=Label(CustomerDetailsLabelFrame,text="Room Type",font=("Calibri",20))
        RoomTypeLabel.place(x=47,y=320,height=30,width=135)

        RoomEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Luxury","Normal"],textvariable=self.roomtypeSearch,state=DISABLED)
        RoomEntry.place(x=230,y=320,height=35,width=300)
        RoomEntry['state'] = 'readonly'


        MealLabel=Label(CustomerDetailsLabelFrame,text="Meal",font=("Calibri",20))
        MealLabel.place(x=620,y=20,height=30,width=85)

        MealEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["Morning","Dinner","Both"],textvariable=self.mealtypeSearch,state=DISABLED)
        MealEntry.place(x=790,y=20,height=35,width=300)
        MealEntry['state'] = 'readonly'

        DaysLabel=Label(CustomerDetailsLabelFrame,text="Total Days",font=("Calibri",20))
        DaysLabel.place(x=620,y=80,height=30,width=145)

        DaysEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.totalDaysSearch,state=DISABLED)
        DaysEntry.place(x=790,y=80,height=35,width=300)

        PersonLabel=Label(CustomerDetailsLabelFrame,text="Person",font=("Calibri",20))
        PersonLabel.place(x=610,y=140,height=30,width=130)

        PersonEntry=ttk.Combobox(CustomerDetailsLabelFrame,font=("Calibri",20),values=["1","2"],textvariable=self.personSearch,state=DISABLED)
        PersonEntry.place(x=790,y=140,height=35,width=300)
        PersonEntry['state'] = 'readonly'

        TimeLabel=Label(CustomerDetailsLabelFrame,text="Book Time",font=("Calibri",20))
        TimeLabel.place(x=620,y=200,height=30,width=145)

        TimeEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.timeSearch,state=DISABLED)
        TimeEntry.place(x=790,y=200,height=35,width=300)

        DateLabel=Label(CustomerDetailsLabelFrame,text="Book Date",font=("Calibri",20))
        DateLabel.place(x=620,y=260,height=30,width=145)

        DateEntry=Entry(CustomerDetailsLabelFrame,font=("Calibri",20),textvariable=self.dateSearch,state=DISABLED)
        DateEntry.place(x=790,y=260,height=35,width=300)

        self.usernameSearch.set(user)
        self.phoneNumberSearch.set(phone)
        self.genderSearch.set(gender)
        self.roomtypeSearch.set(roomtype)
        self.mealtypeSearch.set(meal)
        self.bookIdSearch.set(bookid)
        self.roomIdSearch.set(roomno)
        self.totalDaysSearch.set(totaldays)
        self.personSearch.set(person)
        self.timeSearch.set(time)
        self.dateSearch.set(date)
 
    def DeletePage(self):
        Frameup=Frame(self.FrameRight)
        Frameup.place(x=0,y=0,height=110,width=1190)
        HotelLabel=Label(Frameup,text="Python Managment Hotel",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelLabel.place(x=0,y=0,height=60,width=1190)
        HotelDelete=Label(Frameup,text="Delete Page",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelDelete.place(x=0,y=70,height=40,width=1190)
        Framedown=Frame(self.FrameRight,bg="light grey")
        Framedown.place(x=0,y=120,height=630,width=1190) 
        DeleteByLabel=Label(Framedown,text="Delete By",font=("Calibri",20),bg="light grey")
        DeleteByLabel.place(x=200,y=50,height=30,width=150)   
        DeleteByEntry=ttk.Combobox(Framedown,font=("Calibri",20),values=["BookingId","RoomNo"],textvariable=self.DeleteByVal)
        DeleteByEntry['state']='readonly'
        DeleteByEntry.place(x=380,y=50,height=35,width=250)   
        SearchByEntryValue=Entry(Framedown,font=("Calibri",20),textvariable=self.DeleteByval)
        SearchByEntryValue.place(x=650,y=50,height=35,width=300)
        DeleteBtn=Button(Framedown,text="Delete",bg="red",fg="white",font=("times new roman",25,"bold"),command=self.delete)
        DeleteBtn.place(x=560,y=100,height=40,width=150)

    def delete(self):
        # print(self.DeleteByVal.get(),self.DeleteByval.get())
        # cur.execute("select * from hotelcustomerdetails where {} = {}".format(self.DeleteByVal.get(),self.DeleteByval.get()))
        # data=cur.fetchone()
        # print(data)
        data=coll.find_one_and_delete({'BookingId':self.DeleteByval.get()})
        print(data)
        if(data!=None):
            print("\nData Found")
            print("\nData Deleted")
            showinfo("Info","Data Found And Deleted")
        else:
            print("\nData Not Found")
            showwarning("Warning","Data Not Found")

    def AllUserPage(self):
        Frameup=Frame(self.FrameRight)
        Frameup.place(x=0,y=0,height=110,width=1190)
        HotelLabel=Label(Frameup,text="Python Managment Hotel",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelLabel.place(x=0,y=0,height=60,width=1190)
        HotelAllUser=Label(Frameup,text="All User Page",font=("Calibri",30,"bold"),fg="yellow",bg="black")
        HotelAllUser.place(x=0,y=70,height=40,width=1190)
        Framedown=Frame(self.FrameRight,bg="light grey")
        Framedown.place(x=0,y=120,height=630,width=1190)
        scroll_x=ttk.Scrollbar(Framedown,orient=HORIZONTAL)    
        scroll_y=ttk.Scrollbar(Framedown,orient=VERTICAL)    
        self.hotel_table=ttk.Treeview(Framedown,column=("bookid","roomno","username","phonenumber","gender","roomtype","meal","totaldays","person","date","time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hotel_table.xview)
        scroll_y.config(command=self.hotel_table.yview)
        self.hotel_table.heading("bookid",text="Book Id")
        self.hotel_table.heading("roomno",text="Room No")
        self.hotel_table.heading("username",text="Username")
        self.hotel_table.heading("phonenumber",text="Phone Number")
        self.hotel_table.heading("gender",text="Gender")
        self.hotel_table.heading("roomtype",text="Room Type")
        self.hotel_table.heading("meal",text="Meal")
        self.hotel_table.heading("totaldays",text="Days")
        self.hotel_table.heading("person",text="Person")
        self.hotel_table.heading("date",text="Date")
        self.hotel_table.heading("time",text="Time")
        self.hotel_table["show"]="headings"
        self.hotel_table.pack(fill=BOTH,expand=1)
        self.hotel_table.column("bookid",width=150 )
        self.hotel_table.column("roomno",width=150 )
        self.hotel_table.column("username",width=150 )
        self.hotel_table.column("phonenumber",width=150 )
        self.hotel_table.column("gender",width=150 )
        self.hotel_table.column("roomtype",width=150 )
        self.hotel_table.column("meal",width=150 )
        self.hotel_table.column("totaldays",width=150 )
        self.hotel_table.column("person",width=150 )
        self.hotel_table.column("date",width=150 )
        self.hotel_table.column("time",width=150)
        self.fetchData()

    def fetchData(self):
        datas=coll.find({})
        print(datas)
        for data in datas:
            print(data)
            self.hotel_table.insert("",END,values=(data["BookingId"],data["RoomNo"],data['Username'],data['PhoneNumber'],data['Gender'],data['RoomType'],data['Meal'],data['TotalDays'],data['Person'],data["BookDate"],data["BookDate"]))

 

if __name__=="__main__":
    root=Tk()
    obj=HotelM(root)

    root.mainloop()
