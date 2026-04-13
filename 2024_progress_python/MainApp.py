'''
Notes => 
-> My_Frame ctr = 8 ; on_enter CTR = 21
I. Main question => 
- How to create multi window tkinter application
1. System that'll be used => 
- Python tkinter 
2. Pages => 
a. Registration page (first page)
b. Login page 
c. Welcoming screen or Home page containing 
    --> Welcome [username]; show six buttons ; navbar consist of notification icon
    --> Notification bar 
        -> show which customer needs to pay debt 
        -> show duedate of delivery to client 
    when add/edit new subcategory, new ID will be added 
        -> Add/edit Product type [1] 
        -> Add Material [2]
        -> Add Customer record [3]
        -> Add Supplier record [4]
        -> Show insight [5]
         -> Add sale record [6]
    --> [1] Sales recorder page [dropdown menu] 
        -> Sales ID  (PK)
        -> Purchase date 
        -> Product ID (FK)
        -> Customer ID (FK)
    --> [2] Add/edit product type page 
        -> Product ID (automatic, in order)
        -> ProductName
    --> [3] Add material record
        material ID 
        material name 
        material cost per one 
        product ID 
        material ID 
    --> [4] Add customer record
        Customer_ID
        Customer_Name
        Address
        Contact_Number
    --> [5] Add supplier record
         Supplier_ID
         Supplier_Name
         Address
         Contact_NO
         Supplier_Status [dropdown]
   --> [6] Instalasi Page 
      Pekerja type ID 
      Jenis Pekerjaan 
      Gaji Per Hari 
    --> [7] Show insight 
        Annual Sales  
            - profit 
        Annual sales by product 
        Annual sales by customer 
'''
import tkinter 
from tkinter import *
import sqlite3
from tkinter import ttk
from os.path import realpath
from tkinter import Button
#from PIL import ImageTk, Image
#from tkcalendar import *

# this will create the database file 
connection = sqlite3.connect("MainDataFin.db")
# Create the cursor to interact with the database
cursor = connection.cursor()
DATABASE_NAME = realpath('MainDataFin.db')

cursor.execute("""CREATE TABLE IF NOT EXISTS
    Registration(UserID INTEGER PRIMARY KEY, Name TEXT, Username TEXT, Password TEXT)
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS
    ProductT(Product_ID INTEGER PRIMARY KEY, Product_Name TEXT)
    """)

''' Draft 
cursor.execute("""CREATE TABLE IF NOT EXISTS
    ProductT(Product_ID INTEGER PRIMARY KEY, Product_Name TEXT, Material_Cost FLOAT, Labour_Cost FLOAT, Selling_Price FLOAT, Supplier_ID INTEGER)
    """)
'''
cursor.execute("""CREATE TABLE IF NOT EXISTS
    MaterialR(Material_ID INTEGER PRIMARY KEY, Material_Name TEXT, Price_per_one INTEGER, Product_ID INTEGER, Supplier_ID INTEGER)
    """)
cursor.execute("""CREATE TABLE IF NOT EXISTS
    CustomerR(Customer_ID INTEGER PRIMARY KEY, Customer_Name TEXT, Address TEXT,  Contact_Number INTEGER)
    """)


cursor.execute("""CREATE TABLE IF NOT EXISTS
    SupplierR(Supplier_ID INTEGER PRIMARY KEY, Supplier_Name TEXT, Address TEXT, Contact_NO INTEGER, Supplier_Status TEXT)
   """)

cursor.execute("""CREATE TABLE IF NOT EXISTS
    Instalasi(Pekerja_ID INTEGER PRIMARY KEY, Pekerja_Name TEXT, Gaji_Per_Hari TEXT)
   """)

cursor.execute("""CREATE TABLE IF NOT EXISTS
    SaleR(ProjectID INTEGER PRIMARY KEY, Project_Name TEXT, Project_Date DATE, Product_ID INTEGER, Customer_ID INTEGER, Transport_Cost INTEGER, Project_Value INTEGER)
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS
    SaleRF(SummarryID INTEGER PRIMARY KEY, Project_Name TEXT, Project_Value INTEGER, Material_Expense INTEGER, Instalation_Expense INTEGER, Gross_Profit INTEGER)
    """)



RegisterPG = Tk()
RegisterPG.title('Registration Screen')
RegisterPG.geometry('1366x768')  # full screen 
RegisterPG.configure(bg="#E6DDC4") #To Change the Window Color
#btn = Button(Register , text='register' , command= callLogin)
#btn.pack()

lbl1 = Label(RegisterPG, text=" Registration Screen ", font = "Arial 30")
lbl1.place(x=353, y=10)
lbl1.configure(background='yellow',  width=28)

lbl1 = Label(RegisterPG, text="", font = "Arial 20")
lbl1.place(x=203, y=90)
lbl1.configure(background='#678983',  width=58, height=18)

lbl2 = Label(RegisterPG, text="Name", font = "Arial 15")
lbl2.place(x=603, y=110)
lbl2.configure(background='yellow',  width=12)

lbl3 = Label(RegisterPG, text="Username", font = "Arial 15")
lbl3.place(x=603, y=220)
lbl3.configure(background='yellow',  width=12)

lbl4 = Label(RegisterPG, text="Password", font = "Arial 15")
lbl4.place(x=603, y=330)
lbl4.configure(background='yellow',  width=12)

lbl5 = Label(RegisterPG, text="Confirm Password", font = "Arial 15")
lbl5.place(x=573, y=440)
lbl5.configure(background='yellow',  width=18)

lbl6 = Label(RegisterPG, text="I have an account", font = "Arial 10 ")
lbl6.place(x=595, y=603)
lbl6.configure(background='yellow',  width=18)


NameInput = StringVar() # This will hold the input in the Username Textbox    
txtNameInput= Entry(RegisterPG, width=30, textvariable=NameInput, font= "Arial 15")
txtNameInput.place(x=500, y=155) # label += 45

UsernameInput = StringVar() # This will hold the input in the Username Textbox    
txtUsernameInput= Entry(RegisterPG, width=30, textvariable=UsernameInput, font= "Arial 15")
txtUsernameInput.place(x=500, y=265)

PasswordInput = StringVar() # This will hold the input in the Username Textbox    
txtPasswordInput= Entry(RegisterPG, width=30, textvariable=PasswordInput, font= "Arial 15")
txtPasswordInput.place(x=500, y=375)

ConfPasswordInput = StringVar() # This will hold the input in the Username Textbox    
txtConfPasswordInput= Entry(RegisterPG, width=30, textvariable=ConfPasswordInput, font= "Arial 15")
txtConfPasswordInput.place(x=500, y=485)




def on_enter(e):
   cmdRegister.config(background='OrangeRed3', foreground= "white")
   #cmdRegisterL.config(background='OrangeRed3', foreground= "white")
   #cmdLogin.config(background='OrangeRed3', foreground= "white")

def on_leave(e):
   cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   #cmdRegisterL.config(background= 'SystemButtonFace', foreground= 'black')
   #cmdLogin.config(background= 'SystemButtonFace', foreground= 'black')

def on_enter2(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdLogin.config(background='OrangeRed3', foreground= "white")

def on_leave2(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdLogin.config(background= 'SystemButtonFace', foreground= 'black')


global CTRP
def CheckPass():
   global CTRP
   P1 = txtPasswordInput.get()
   P2 = txtConfPasswordInput.get()
   if P1 != P2:
      CTRP = FALSE
      lblMpass = Label(RegisterPG, text="*Password doesn't match", font = "Arial 10")
      lblMpass.place(x=500, y=520)
      lblMpass.configure(background='#678983', foreground='black', width=18)
   else:
      CTRP = TRUE

def SaveRegis():
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   Nout = txtNameInput.get()
   Uout = txtUsernameInput.get()
   P1 = txtPasswordInput.get()
   cursor.execute("INSERT INTO Registration VALUES (NULL, ?, ?, ?)", (Nout, Uout, P1, ))
   connection.commit()
   #connection.close()
   


def RegisterAct():
   Nout = txtNameInput.get()
   Uout = txtUsernameInput.get()
   P1 = txtPasswordInput.get()
   P2 = txtConfPasswordInput.get()
   if (len(Nout) == 0) or (len(Uout) == 0) or (len(P1) == 0) or (len(P2) == 0):
    #print("all boxes must be filled")
    lblRegAct = Label(RegisterPG, text="all boxes must be filled", font = "Arial 10")
    lblRegAct.place(x=500, y=520)
    lblRegAct.configure(background='#678983', foreground='black', width=18)
   else:
      CheckPass()
      if CTRP == TRUE:
        SaveRegis()
        callLogin()

def reglogact():
   callLogin()


def loginact():
   global CTRL
   CTRL = FALSE
   global UsernameIP
   UsernameIP = txtUsernameInputL.get()
   PasswordIP = txtPasswordInputL.get()

   #connection = sqlite3.connect("MainData.db")
   #cursor = connection.cursor()

   cursor.execute("SELECT * FROM Registration")
   results = cursor.fetchall()
   
   for result in results:
      if result[2] == UsernameIP and result[3] == PasswordIP:
        #print("welcome home")
        CTRL = TRUE
      else:
        lbl7 = Label(loginPG, text="Wrong password and/or username", font = "Arial 10 ")
        lbl7.place(x=565, y=470)
        lbl7.configure(background='yellow',  width=25)
      
      if CTRL == TRUE:
        befCallHome()
      else:
        lbl7 = Label(loginPG, text="Wrong password and/or username", font = "Arial 10 ")
        lbl7.place(x=565, y=470)
        lbl7.configure(background='yellow',  width=25)
         

   connection.commit()
   #connection.close()


def befCallHome():
   #loginPG.withdraw()
   callHome()




cmdRegister = Button(RegisterPG, text="Register", width=20, font= "Arial 15", command=RegisterAct)
cmdRegister.place(x=555, y=560)

cmdRegister.bind('<Enter>', on_enter)
cmdRegister.bind('<Leave>', on_leave)

cmdLogin = Button(RegisterPG, text="Log in", width=20, font= "Arial 15", command=reglogact)
cmdLogin.place(x=555, y=630)#

cmdLogin.bind('<Enter>', on_enter2)
cmdLogin.bind('<Leave>', on_leave2)
'''
cmdLogin = Button(RegisterPG, text="Log in", width=20, font= "Arial 15", command=callHome)
cmdLogin.place(x=555, y=630)#

cmdLogin.bind('<Enter>', on_enter2)
cmdLogin.bind('<Leave>', on_leave2)
'''
''' Login Page '''
def bringbackReg():
   #loginPG.withdraw()
   RegisterPG.deiconify()


def callLogin():
    global loginPG
    #RegisterPG.withdraw()
    loginPG = Tk()
    loginPG.title("Login screen")
    loginPG.configure(background= "#E6DDC4")
    loginPG.geometry('1366x768')

    lbl1L = Label(loginPG, text=" Login Screen ", font = "Arial 30")
    lbl1L.place(x=353, y=10)
    lbl1L.configure(background='yellow',  width=28)

    lbl2 = Label(loginPG, text="", font = "Arial 20")
    lbl2.place(x=203, y=90)
    lbl2.configure(background='#678983',  width=58, height=18)
    '''
    lbl2 = Label(RegisterPG, text="Name", font = "Arial 15")
    lbl2.place(x=603, y=110)
    lbl2.configure(background='yellow',  width=12)
    '''
    lbl3 = Label(loginPG, text="Username", font = "Arial 15")
    lbl3.place(x=603, y=220)
    lbl3.configure(background='yellow',  width=12)

    lbl4 = Label(loginPG, text="Password", font = "Arial 15")
    lbl4.place(x=603, y=330)
    lbl4.configure(background='yellow',  width=12)
    '''
    lbl5 = Label(RegisterPG, text="Confirm Password", font = "Arial 15")
    lbl5.place(x=573, y=440)
    lbl5.configure(background='yellow',  width=18)
    '''
    '''
    NameInput = StringVar() # This will hold the input in the Username Textbox    
    txtNameInput= Entry(RegisterPG, width=30, textvariable=NameInput, font= "Arial 15")
    txtNameInput.place(x=500, y=155) # label += 45
    '''
    global txtUsernameInputL
    global txtPasswordInputL
    UsernameInputL = StringVar() # This will hold the input in the Username Textbox    
    txtUsernameInputL= Entry(loginPG, width=30, textvariable=UsernameInputL, font= "Arial 15")
    txtUsernameInputL.place(x=500, y=265)

    PasswordInputL = StringVar() # This will hold the input in the Username Textbox    
    txtPasswordInputL= Entry(loginPG, width=30, textvariable=PasswordInputL, font= "Arial 15")
    txtPasswordInputL.place(x=500, y=375)
    '''
    ConfPasswordInput = StringVar() # This will hold the input in the Username Textbox    
    txtConfPasswordInput= Entry(RegisterPG, width=30, textvariable=ConfPasswordInput, font= "Arial 15")
    txtConfPasswordInput.place(x=500, y=485)
    '''
    global cmdLoginL
    cmdLoginL = Button(loginPG, text="Log in", width=20, font= "Arial 15", command=loginact)
    cmdLoginL.place(x=555, y=500)#original - 60 

    cmdLoginL.bind('<Enter>', on_enter3)
    cmdLoginL.bind('<Leave>', on_leave3)
    global cmdRegisterL
    cmdRegisterL = Button(loginPG, text="Register", width=20, font= "Arial 15", command=bringbackReg)
    cmdRegisterL.place(x=555, y=570)

    cmdRegisterL.bind('<Enter>', on_enter4)
    cmdRegisterL.bind('<Leave>', on_leave4)

    lbl6 = Label(loginPG, text="Back to register screen", font = "Arial 10 ")
    lbl6.place(x=595, y=543)
    lbl6.configure(background='yellow',  width=18)

def callHome():
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   global homePG
   #loginPG.withdraw()
   homePG = Tk()
   homePG.title("Home Screen")
   homePG.configure(background="#E6DDC4")
   homePG.geometry('1366x768')

   befbefcallSaleRecordPG1()

   #connection.commit()

   lblNavb = Label(homePG, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(homePG, text="Manager Application", font = "Arial 25 bold")
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)
   lblCover = Label(homePG, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=18)
   
   ''''''
   lbl2H =  Label(homePG, text=f"Welcome Home, {UsernameIP} ", font = "Arial 30 bold")
   lbl2H.place(x=353, y=120)
   lbl2H.configure(background='#678983',  width=28, foreground='white')
   
   global cmdProductT
   cmdProductT = Button(homePG, text="Add Product Type", width=20, font= "Arial 15", command=callProductT)
   cmdProductT.place(x=555, y=230)
   cmdProductT.bind('<Enter>', on_enter6)
   cmdProductT.bind('<Leave>', on_leave6)

   global cmdCustomerD
   cmdCustomerD = Button(homePG, text="Add Supplier Record", width=20, font= "Arial 15", command=CallAddS_HP)
   cmdCustomerD.place(x=555, y=280) # original + 50
   cmdCustomerD.bind('<Enter>', on_enter7)
   cmdCustomerD.bind('<Leave>', on_leave7)

   global cmdPaymentS
   cmdPaymentS = Button(homePG, text="Add Material Type", width=20, font= "Arial 15", command=befCallMaterialA_H)
   cmdPaymentS.place(x=555, y=330)
   cmdPaymentS.bind('<Enter>', on_enter8)
   cmdPaymentS.bind('<Leave>', on_leave8)

   global cmdSupplierR
   cmdSupplierR = Button(homePG, text="Add Customer Record", width=20, font= "Arial 15", command=callCustA)
   cmdSupplierR.place(x=555, y=380)
   cmdSupplierR.bind('<Enter>', on_enter11)
   cmdSupplierR.bind('<Leave>', on_leave11)

   global cmdAddI
   cmdAddI = Button(homePG, text="Add Instalasi Record", width=20, font= "Arial 15", command=callInstA)
   cmdAddI.place(x=555, y=430)
   cmdAddI.bind('<Enter>', on_enter14)
   cmdAddI.bind('<Leave>', on_leave14)

   global cmdShowI
   cmdShowI = Button(homePG, text="Show Sale Insight", width=20, font= "Arial 15", command=reglogact)
   cmdShowI.place(x=555, y=480)
   cmdShowI.bind('<Enter>', on_enter9)
   cmdShowI.bind('<Leave>', on_leave9)


   global cmdSaleR
   cmdSaleR = Button(homePG, text="Add Sale Record", width=25, font= "Arial 15 bold", command=befcallSaleRecordPG1)
   cmdSaleR.place(x=515, y=605)
   cmdSaleR.bind('<Enter>', on_enter10)
   cmdSaleR.bind('<Leave>', on_leave10)
   #connection.close()


def on_enter3(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdLoginL.config(background='OrangeRed3', foreground= "white")

def on_leave3(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdLoginL.config(background= 'SystemButtonFace', foreground= 'black')

def on_enter4(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdRegisterL.config(background='OrangeRed3', foreground= "white")
   #cmdLogin.config(background='OrangeRed3', foreground= "white")

def on_leave4(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdRegisterL.config(background= 'SystemButtonFace', foreground= 'black')
   #cmdLogin.config(background= 'SystemButtonFace', foreground= 'black')

def on_enter5(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmd1H.config(foreground= "aqua")

def on_leave5(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmd1H.config(foreground= 'white')

def on_enter6(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdProductT.config(foreground= "black", background='OrangeRed3')

def on_leave6(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdProductT.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter7(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdCustomerD.config(foreground= "black", background='OrangeRed3')

def on_leave7(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdCustomerD.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter8(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdPaymentS.config(foreground= "black", background='OrangeRed3')

def on_leave8(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdPaymentS.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter9(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdShowI.config(foreground= "black", background='OrangeRed3')

def on_leave9(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdShowI.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter10(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdSaleR.config(foreground= "black", background='OrangeRed3')

def on_leave10(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdSaleR.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter11(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdSupplierR.config(foreground= "black", background='OrangeRed3')

def on_leave11(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdSupplierR.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter12(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddRec.config(foreground= "black", background='OrangeRed3')

def on_leave12(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddRec.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter13(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddMfP.config(foreground= "black", background='OrangeRed3')

def on_leave13(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddMfP.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter14(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddI.config(foreground= "black", background='OrangeRed3')

def on_leave14(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddI.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter15(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddSuppOri.config(foreground= "black", background='OrangeRed3')

def on_leave15(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddSuppOri.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter16(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddMfS.config(foreground= "black", background='OrangeRed3')

def on_leave16(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddMfS.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter17(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddRec.config(foreground= "black", background='OrangeRed3')

def on_leave17(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddRec.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter18(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddSfM.config(foreground= "black", background='OrangeRed3')

def on_leave18(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddSfM.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter19(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddPfM.config(foreground= "black", background='OrangeRed3')

def on_leave19(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddPfM.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter20(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddCu.config(foreground= "black", background='OrangeRed3')

def on_leave20(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddCu.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter21(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddIns.config(foreground= "black", background='OrangeRed3')

def on_leave21(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddIns.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter22(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddPfR.config(foreground= "black", background='OrangeRed3')

def on_leave22(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddPfR.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter23(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddPRPG1.config(foreground= "black", background='OrangeRed3')

def on_leave23(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddPRPG1.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter24(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddIns.config(foreground= "black", background='OrangeRed3')

def on_leave24(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddIns.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter25(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddCfSR.config(foreground= "black", background='OrangeRed3')

def on_leave25(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddCfSR.config(foreground= 'black', background= 'SystemButtonFace')

def on_enter26(e):
   #cmdRegister.config(background='OrangeRed3', foreground= "white")
   cmdAddRecNext.config(foreground= "black", background='OrangeRed3')

def on_leave26(e):
   #cmdRegister.config(background= 'SystemButtonFace', foreground= 'black')
   cmdAddRecNext.config(foreground= 'black', background= 'SystemButtonFace')


''' Add Product Type Page '''
def callProductT():
   
   global ProductTPG 
   #homePG.withdraw()
   ProductTPG = Tk()
   ProductTPG.title("Add Product Screen")
   ProductTPG.configure(background="#E6DDC4")
   ProductTPG.geometry('1366x768')

   lblNavb = Label(ProductTPG, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(ProductTPG, text="Manager Application", font = "Arial 25 bold", command=callHome)
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(ProductTPG, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   
   ''''''

   lbl3P = Label(ProductTPG, text="Product Name", font = "Arial 15")
   lbl3P.place(x=603, y=120)
   lbl3P.configure(background='yellow',  width=12)

   
   global txtProductNIP
   ProductNInput = StringVar() # This will hold the input in the Username Textbox    
   txtProductNIP= Entry(ProductTPG, width=30, textvariable=ProductNInput, font= "Arial 15")
   txtProductNIP.place(x=500, y=160) # original + 40

   
   global cmdAddRec
   cmdAddRec = Button(ProductTPG, text="Add Record", width=20, font= "Arial 15", command=saveProductT)
   cmdAddRec.place(x=555, y=240)#original - 60 
   cmdAddRec.bind('<Enter>', on_enter12)
   cmdAddRec.bind('<Leave>', on_leave12)

   global cmdAddMfP
   cmdAddMfP = Button(ProductTPG, text="Add Material Record", width=20, font= "Arial 15", command=befCallMaterialA_P)
   cmdAddMfP.place(x=555, y=280)#original - 60 
   cmdAddMfP.bind('<Enter>', on_enter13)
   cmdAddMfP.bind('<Leave>', on_leave13)

   ''''''
   #Create a frame to hold the treeview
   global my_Frame
   global TREEP
   my_Frame=Frame(ProductTPG, height = 68, width = 1, background="yellow")
   my_Frame.place(x=5, y=530)
      
   TREEP = ttk.Treeview(my_Frame, columns=(1,2), show="headings", height="10")
   TREEP.column(1, stretch=NO, width=90)
   TREEP.column(2, stretch=NO, width=120)
  

   #tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
   TREEP.pack()

   TREEP.heading(1, text="Product ID")
   TREEP.heading(2, text="Product Name")
  
   ''' 2nd treeview '''
   global my_Frame3
   global TREEMiP
   my_Frame3=Frame(ProductTPG, height = 68, width = 1, background="yellow")
   my_Frame3.place(x=805, y=530)
      
   TREEMiP = ttk.Treeview(my_Frame3, columns=(1,2,3,4,5), show="headings", height="10")
   TREEMiP.column(1, stretch=NO, width=90)
   TREEMiP.column(2, stretch=NO, width=90)
   TREEMiP.column(3, stretch=NO, width=90)
   TREEMiP.column(4, stretch=NO, width=90)
   TREEMiP.column(5, stretch=NO, width=90)

   #tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
   TREEMiP.pack()

   TREEMiP.heading(1, text="Material ID")
   TREEMiP.heading(2, text="Material Name")
   TREEMiP.heading(3, text="Cost per one")
   TREEMiP.heading(4, text="Product ID")
   TREEMiP.heading(5, text="Supplier ID")
   populateP()
   populateMiP()


def saveProductT():
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   PNout = txtProductNIP.get()
   if (len(PNout) > 0):
      cursor.execute("INSERT INTO ProductT VALUES (NULL, ?)", (PNout, ))
      connection.commit()
      populateP()
      populateMiP()
      clearP()
   else:
      lbl8P = Label(ProductTPG, text="All boxes must be filled", font = "Arial 10")
      lbl8P.place(x=570, y=540)
      lbl8P.configure(background='#678983',  width=25, foreground='white')

   #connection.close()

def clearP():
   txtProductNIP.delete(0, END)

def populateP():
   cursor.execute("SELECT * FROM ProductT")
   result = cursor.fetchall()
   for record in TREEP.get_children():
      TREEP.delete(record)
   if len(result) != 0:
      for i in result:
         TREEP.insert('', 'end', values=i)
def populateMiP():
   cursor.execute("SELECT * FROM MaterialR")
   result = cursor.fetchall()
   for record in TREEMiP.get_children():
      TREEMiP.delete(record)
   if len(result) != 0:
      for i in result:
         TREEMiP.insert('', 'end', values=i)
   
''' Add Supplier Page'''

def CallAddS_PT():
   #ProductTPG.withdraw()
   CallAddS()

def CallAddS_HP():
   #homePG.withdraw()
   CallAddS()

def CallAddS():
   global AddSRPG
   AddSPRG = Tk()
   AddSPRG.title("Add Supplier Screen")
   AddSPRG.configure(background="#E6DDC4")
   AddSPRG.geometry('1366x768')

   lblNavb = Label(AddSPRG, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(AddSPRG, text="Manager Application", font = "Arial 25 bold", command=callHome)
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(AddSPRG, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   ''''''
   lbl3S = Label(AddSPRG, text="Supplier Name", font = "Arial 15")
   lbl3S.place(x=603, y=120)
   lbl3S.configure(background='yellow',  width=12)

   lbl4S = Label(AddSPRG, text="Address", font = "Arial 15")
   lbl4S.place(x=603, y=200)
   lbl4S.configure(background='yellow',  width=12)

   lbl5P = Label(AddSPRG, text="Contact No", font = "Arial 15")
   lbl5P.place(x=603, y=285)
   lbl5P.configure(background='yellow',  width=12)

   lbl6P = Label(AddSPRG, text="Supplier Status", font = "Arial 15")
   lbl6P.place(x=603, y=370)
   lbl6P.configure(background='yellow',  width=12)


   global txtSupplierNIP
   SupplierNIP = StringVar() # This will hold the input in the Username Textbox    
   txtSupplierNIP= Entry(AddSPRG, width=30, textvariable=SupplierNIP, font= "Arial 15")
   txtSupplierNIP.place(x=500, y=160)

   global txtAddIP
   AddIP = StringVar() # This will hold the input in the Username Textbox    
   txtAddIP= Entry(AddSPRG, width=30, textvariable=AddIP, font= "Arial 15")
   txtAddIP.place(x=500, y=240)

   global txtContactNIP
   ContactNIP = StringVar() # This will hold the input in the Username Textbox    
   txtContactNIP= Entry(AddSPRG, width=30, textvariable=ContactNIP, font= "Arial 15")
   txtContactNIP.place(x=500, y=325) #+25
   #
   options = [
      "Active",
      "Inactive",
   ]
   global txtSupplierSTIP
   global SupplierSTIP

   SupplierSTIP = StringVar() # This will hold the input in the Username Textbox    
   SupplierSTIP.set(f"{options[0]}")

   #SupplierSTIP.place(x=500, y=410)
   txtSupplierSTIP= OptionMenu(AddSPRG, SupplierSTIP, *options)
   txtSupplierSTIP.pack()
   txtSupplierSTIP.place(x=650, y=410)

   #drop = OptionMenu(AddSPRG, SupplierSTIP, )


   #
   global cmdAddSuppOri
   cmdAddSuppOri = Button(AddSPRG, text="Add Supplier", width=20, font= "Arial 15", command=saveSupplier)
   cmdAddSuppOri.place(x=555, y=565)#original - 60 
   cmdAddSuppOri.bind('<Enter>', on_enter15)
   cmdAddSuppOri.bind('<Leave>', on_leave15)

   global cmdAddMfS
   cmdAddMfS = Button(AddSPRG, text="Add Material Record", width=20, font= "Arial 15", command=befCallMaterialA_S)
   cmdAddMfS.place(x=555, y=650)#original - 60 
   cmdAddMfS.bind('<Enter>', on_enter16)
   cmdAddMfS.bind('<Leave>', on_leave16)
   ''''''
   global my_Frame2
   global TREES
   my_Frame2=Frame(AddSPRG, height = 68, width = 1, background="yellow")
   my_Frame2.place(x=5, y=530)
      
   TREES = ttk.Treeview(my_Frame2, columns=(1,2,3,4,5), show="headings", height="10")
   TREES.column(1, stretch=NO, width=90)
   TREES.column(2, stretch=NO, width=90)
   TREES.column(3, stretch=NO, width=90)
   TREES.column(4, stretch=NO, width=90)
   TREES.column(5, stretch=NO, width=90)

   #tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
   TREES.pack()

   TREES.heading(1, text="Supplier ID")
   TREES.heading(2, text="Supplier Name")
   TREES.heading(3, text="Address")
   TREES.heading(4, text="Contact No")
   TREES.heading(5, text="Supplier Status")
   populateS()


def clearS():
   txtSupplierNIP.delete(0, END)
   txtAddIP.delete(0, END)
   txtContactNIP.delete(0, END)
   #txtSupplierSTIP.delete(0, END)

def saveSupplier():
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   SNout = txtSupplierNIP.get()
   Aout = txtAddIP.get()
   CNOout = txtContactNIP.get()
   STout = SupplierSTIP.get()

   if (len(SNout) > 0):
      cursor.execute("INSERT INTO SupplierR VALUES (NULL, ?, ?, ?, ?)", (SNout, Aout, CNOout, STout, ))
      connection.commit()
      populateS()
      clearS()
   else:
      lbl8P = Label(ProductTPG, text="All boxes must be filled", font = "Arial 10")
      lbl8P.place(x=570, y=540)
      lbl8P.configure(background='#678983',  width=25, foreground='white')
   
   #connection.close()



def populateS():
   cursor.execute("SELECT * FROM SupplierR")
   result = cursor.fetchall()
   for record in TREES.get_children():
      TREES.delete(record)
   if len(result) != 0:
      for i in result:
         TREES.insert('', 'end', values=i)

''' Add Material Page '''
def befCallMaterialA_P():
   #ProductTPG.withdraw()
   callMaterialA()

def befCallMaterialA_H():
   #homePG.withdraw()
   callMaterialA()

def befCallMaterialA_S():
   #AddSPRG.withdraw()
   callMaterialA()

def callMaterialA():
   global MaterialAPG
   MaterialAPG = Tk()
   MaterialAPG.title("Add Material Screen")
   MaterialAPG.configure(background="#E6DDC4")
   MaterialAPG.geometry('1366x768')

   lblNavb = Label(MaterialAPG, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(MaterialAPG, text="Manager Application", font = "Arial 25 bold", command=callHome)
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(MaterialAPG, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   ''''''
   lbl3M = Label(MaterialAPG, text="Material Name", font = "Arial 15")
   lbl3M.place(x=603, y=120)
   lbl3M.configure(background='yellow',  width=12)

   lbl4M = Label(MaterialAPG, text="Cost per one", font = "Arial 15")
   lbl4M.place(x=603, y=200)
   lbl4M.configure(background='yellow',  width=12)

   lbl5M = Label(MaterialAPG, text="Supplier ID", font = "Arial 15")
   lbl5M.place(x=603, y=280)
   lbl5M.configure(background='yellow',  width=12)

   lbl6M = Label(MaterialAPG, text="Product ID", font = "Arial 15")
   lbl6M.place(x=603, y=360)
   lbl6M.configure(background='yellow',  width=12)

   
   global txtMaterialNIP
   MaterialNInput = StringVar() # This will hold the input in the Username Textbox    
   txtMaterialNIP = Entry(MaterialAPG, width=30, textvariable=MaterialNInput, font= "Arial 15")
   txtMaterialNIP.place(x=500, y=160) # original + 40

   global txtCostPIP
   CostPIP = StringVar() # This will hold the input in the Username Textbox    
   txtCostPIP= Entry(MaterialAPG, width=30, textvariable=CostPIP, font= "Arial 15")
   txtCostPIP.place(x=500, y=240)


   global txtSupplierIDIP
   SupplierIDIP = StringVar() # This will hold the input in the Username Textbox    
   txtSupplierIDIP= Entry(MaterialAPG, width=30, textvariable=SupplierIDIP, font= "Arial 15")
   txtSupplierIDIP.place(x=500, y=320)

   global txtProductIDIP
   ProductIDIP = StringVar() # This will hold the input in the Username Textbox    
   txtProductIDIP= Entry(MaterialAPG, width=30, textvariable=ProductIDIP, font= "Arial 15")
   txtProductIDIP.place(x=500, y=400)


   global cmdAddRec
   cmdAddRec = Button(MaterialAPG, text="Add Record", width=20, font= "Arial 15", command=saveMaterial)
   cmdAddRec.place(x=555, y=500)#original - 60 
   cmdAddRec.bind('<Enter>', on_enter17)
   cmdAddRec.bind('<Leave>', on_leave17)

   global cmdAddPfM
   cmdAddPfM = Button(MaterialAPG, text="Add Product", width=20, font= "Arial 15", command=callProductT)
   cmdAddPfM.place(x=555, y=575)#original - 60 
   cmdAddPfM.bind('<Enter>', on_enter19)
   cmdAddPfM.bind('<Leave>', on_leave19)

   global cmdAddSfM
   cmdAddSfM = Button(MaterialAPG, text="Add Supplier", width=20, font= "Arial 15", command=CallAddS_PT)
   cmdAddSfM.place(x=555, y=650)#original - 60 
   cmdAddSfM.bind('<Enter>', on_enter18)
   cmdAddSfM.bind('<Leave>', on_leave18)
   ''' first treeview '''
   global my_Frame4
   global TREEM
   my_Frame4=Frame(MaterialAPG, height = 68, width = 1, background="yellow")
   my_Frame4.place(x=5, y=530)
      
   TREEM = ttk.Treeview(my_Frame4, columns=(1,2,3,4,5), show="headings", height="10")
   TREEM.column(1, stretch=NO, width=90)
   TREEM.column(2, stretch=NO, width=90)
   TREEM.column(3, stretch=NO, width=90)
   TREEM.column(4, stretch=NO, width=90)
   TREEM.column(5, stretch=NO, width=90)

   #tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
   TREEM.pack()

   TREEM.heading(1, text="Material ID")
   TREEM.heading(2, text="Material Name")
   TREEM.heading(3, text="Cost per one")
   TREEM.heading(4, text="Product ID")
   TREEM.heading(5, text="Supplier ID")
   ''' second treeview (Supplier ID)'''
   global my_Frame5
   global TREESfM
   my_Frame5=Frame(MaterialAPG, height = 68, width = 1, background="yellow")
   my_Frame5.place(x=805, y=530)
      
   TREESfM = ttk.Treeview(my_Frame5, columns=(1,2,3,4,5), show="headings", height="10")
   TREESfM.column(1, stretch=NO, width=90)
   TREESfM.column(2, stretch=NO, width=90)
   TREESfM.column(3, stretch=NO, width=90)
   TREESfM.column(4, stretch=NO, width=90)
   TREESfM.column(5, stretch=NO, width=90)

   #tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
   TREESfM.pack()

   TREESfM.heading(1, text="Supplier ID")
   TREESfM.heading(2, text="Supplier Name")
   TREESfM.heading(3, text="Address")
   TREESfM.heading(4, text="Contact No")
   TREESfM.heading(5, text="Supplier Status")
   '''Third Treeview (product ID)'''
   global my_Frame6
   global TREESPfM
   my_Frame6=Frame(MaterialAPG, height = 68, width = 1, background="yellow")
   my_Frame6.place(x=5, y=200)
      
   TREESPfM = ttk.Treeview(my_Frame6, columns=(1,2), show="headings", height="10")
   TREESPfM.column(1, stretch=NO, width=90)
   TREESPfM.column(2, stretch=NO, width=90)

   #tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
   TREESPfM.pack()

   TREESPfM.heading(1, text="Product ID")
   TREESPfM.heading(2, text="Product Name")
   
   populateM()
   populateSfM()
   populatePfM()



def saveMaterial(): 
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   MNout = txtMaterialNIP.get()
   MCout_D = txtCostPIP.get()
   MCout = MCout_D.replace(' ', '')
   SIout = txtSupplierIDIP.get()
   PIout = txtProductIDIP.get()
   cursor.execute("INSERT INTO MaterialR VALUES (NULL, ?, ?, ?, ?)", (MNout, MCout, PIout, SIout))
   connection.commit()
   populateM()
   populateSfM()
   populatePfM
   clearM()
   '''
   else:
      lbl8P = Label(MaterialAPG, text="All boxes must be filled", font = "Arial 10")
      lbl8P.place(x=570, y=540)
      lbl8P.configure(background='#678983',  width=25, foreground='white')
   '''
   #connection.close()

def populateM():
   cursor.execute("SELECT * FROM MaterialR")
   result = cursor.fetchall()
   for record in TREEM.get_children():
      TREEM.delete(record)
   if len(result) != 0:
      for i in result:
         TREEM.insert('', 'end', values=i)

def populateSfM():
   cursor.execute("SELECT * FROM SupplierR")
   result = cursor.fetchall()
   for record in TREESfM.get_children():
      TREESfM.delete(record)
   if len(result) != 0:
      for i in result:
         TREESfM.insert('', 'end', values=i)

def populatePfM():
   cursor.execute("SELECT * FROM ProductT")
   result = cursor.fetchall()
   for record in TREESPfM.get_children():
      TREESPfM.delete(record)
   if len(result) != 0:
      for i in result:
         TREESPfM.insert('', 'end', values=i)

def clearM(): 
   txtMaterialNIP.delete(0, END)
   txtCostPIP.delete(0, END)
   txtSupplierIDIP.delete(0, END)
   txtProductIDIP.delete(0, END)

''' add customer page '''
def callCustA(): 
   global CustAPG
   CustAPG = Tk()
   CustAPG.title("Add Customer Screen")
   CustAPG.configure(background="#E6DDC4")
   CustAPG.geometry('1366x768')

   lblNavb = Label(CustAPG, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(CustAPG, text="Manager Application", font = "Arial 25 bold", command=callHome)
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(CustAPG, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   ''''''

   lbl3C = Label(CustAPG, text="Customer Name", font = "Arial 15")
   lbl3C.place(x=593, y=120)
   lbl3C.configure(background='yellow',  width=15)

   lbl4C = Label(CustAPG, text="Address", font = "Arial 15")
   lbl4C.place(x=603, y=200)
   lbl4C.configure(background='yellow',  width=12)

   lbl5C = Label(CustAPG, text="Contact Number", font = "Arial 15")
   lbl5C.place(x=593, y=280)
   lbl5C.configure(background='yellow',  width=15)

   

   global txtCustNIP
   CustNInput = StringVar() # This will hold the input in the Username Textbox    
   txtCustNIP = Entry(CustAPG, width=30, textvariable=CustNInput, font= "Arial 15")
   txtCustNIP.place(x=500, y=160) # original + 40

   global txtAddCIP
   AddCIP = StringVar() # This will hold the input in the Username Textbox    
   txtAddCIP= Entry(CustAPG, width=30, textvariable=AddCIP, font= "Arial 15")
   txtAddCIP.place(x=500, y=240)


   global txtCUNOIP
   CUNOIP = StringVar() # This will hold the input in the Username Textbox    
   txtCUNOIP= Entry(CustAPG, width=30, textvariable=CUNOIP, font= "Arial 15")
   txtCUNOIP.place(x=500, y=320)


   global cmdAddCu
   cmdAddCu = Button(CustAPG, text="Add Customer", width=20, font= "Arial 15", command=saveCU)
   cmdAddCu.place(x=555, y=575)#original - 60 
   cmdAddCu.bind('<Enter>', on_enter20)
   cmdAddCu.bind('<Leave>', on_leave20)
   global my_Frame6
   global TREEC
   my_Frame6=Frame(CustAPG, height = 68, width = 1, background="yellow")
   my_Frame6.place(x=5, y=530)
      
   TREEC = ttk.Treeview(my_Frame6, columns=(1,2,3,4), show="headings", height="10")
   TREEC.column(1, stretch=NO, width=90)
   TREEC.column(2, stretch=NO, width=105)
   TREEC.column(3, stretch=NO, width=90)
   TREEC.column(4, stretch=NO, width=120)

   #tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
   TREEC.pack()

   TREEC.heading(1, text="Customer ID")
   TREEC.heading(2, text="Customer Name")
   TREEC.heading(3, text="Address")
   TREEC.heading(4, text="Contact Number")
   populateC()


def saveCU():
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   CNout = txtCustNIP.get()
   CAout = txtAddCIP.get()
   cNOout = txtCUNOIP.get()
   cursor.execute("INSERT INTO CustomerR VALUES (NULL, ?, ?, ?)", (CNout, CAout, cNOout))
   connection.commit()
   populateC()
   #connection.close()

def populateC(): 
   cursor.execute("SELECT * FROM CustomerR")
   result = cursor.fetchall()
   for record in TREEC.get_children():
      TREEC.delete(record)
   if len(result) != 0:
      for i in result:
         TREEC.insert('', 'end', values=i)

''' Instalasi Page '''
def callInstA(): 
   global InstAPG
   InstAPG = Tk()
   InstAPG.title("Add Instalation cost Screen")
   InstAPG.configure(background="#E6DDC4")
   InstAPG.geometry('1366x768')

   lblNavb = Label(InstAPG, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(InstAPG, text="Manager Application", font = "Arial 25 bold", command=callHome)
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(InstAPG, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   ''''''

   lbl3I = Label(InstAPG, text="Jenis Pekerjaan", font = "Arial 15")
   lbl3I.place(x=593, y=120)
   lbl3I.configure(background='yellow',  width=15)

   lbl4I = Label(InstAPG, text="Gaji Per Hari", font = "Arial 15")
   lbl4I.place(x=603, y=200)
   lbl4I.configure(background='yellow',  width=12)


   

   global txtPekJIP
   PekJInput = StringVar() # This will hold the input in the Username Textbox    
   txtPekJIP = Entry(InstAPG, width=30, textvariable=PekJInput, font= "Arial 15")
   txtPekJIP.place(x=500, y=160) # original + 40

   global txtGajiIP
   GajiIP = StringVar() # This will hold the input in the Username Textbox    
   txtGajiIP= Entry(InstAPG, width=30, textvariable=GajiIP, font= "Arial 15")
   txtGajiIP.place(x=500, y=240)



   global cmdAddIns
   cmdAddIns = Button(InstAPG, text="Add Instalation Record", width=20, font= "Arial 15", command=saveIns)
   cmdAddIns.place(x=555, y=575)#original - 60 
   cmdAddIns.bind('<Enter>', on_enter24)
   cmdAddIns.bind('<Leave>', on_leave24)
   ''''''
   global my_Frame7
   global TREEI
   my_Frame7=Frame(InstAPG, height = 68, width = 1, background="yellow")
   my_Frame7.place(x=5, y=530)
      
   TREEI = ttk.Treeview(my_Frame7, columns=(1,2,3), show="headings", height="10")
   TREEI.column(1, stretch=NO, width=90)
   TREEI.column(2, stretch=NO, width=105)
   
   #tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
   TREEI.pack()

   TREEI.heading(1, text="Jenis Pekerja ID")
   TREEI.heading(2, text="Jenis Pekerja")
   TREEI.heading(3, text="Gaji per hari")
   populateI()


def saveIns():
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   JPout = txtPekJIP.get()
   GPHout_D = txtGajiIP.get()
   GPHout = GPHout_D.replace(' ', '')
   cursor.execute("INSERT INTO Instalasi VALUES (NULL, ?, ?)", (JPout, GPHout))
   connection.commit()
   populateI()
   #connection.close()

def populateI(): 
   cursor.execute("SELECT * FROM Instalasi")
   result = cursor.fetchall()
   for record in TREEI.get_children():
      TREEI.delete(record)
   if len(result) != 0:
      for i in result:
         TREEI.insert('', 'end', values=i)

''' Show insight page  - SKIP dulu '''

''' Add Sale Record Page 1 '''
''' 
1. Project ID [automatic]
1. Project Name 
2. Project_Date
3. Product_ID [dropdown]
4. Customer_ID [dropdown]
5. Transport cost - textbox
'''
def callRECPG1(): 
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   global AddRecPG1
   AddRecPG1 = Tk()
   AddRecPG1.title("Add Sale Record Screen")
   AddRecPG1.configure(background="#E6DDC4")
   AddRecPG1.geometry('1366x768')

   lblNavb = Label(AddRecPG1, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(AddRecPG1, text="Manager Application", font = "Arial 25 bold", command=callHome)
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(AddRecPG1, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   ''''''
   lbl3SR = Label(AddRecPG1, text="Project Name", font = "Arial 15")
   lbl3SR.place(x=603, y=120)
   lbl3SR.configure(background='yellow',  width=12)

   lbl4SR = Label(AddRecPG1, text="Project Date", font = "Arial 15")
   lbl4SR.place(x=603, y=200)
   lbl4SR.configure(background='yellow',  width=12)

   lbl5SR = Label(AddRecPG1, text="Product ID", font = "Arial 15")
   lbl5SR.place(x=603, y=280)
   lbl5SR.configure(background='yellow',  width=12)

   lbl6SR = Label(AddRecPG1, text="Customer ID", font = "Arial 15")
   lbl6SR.place(x=603, y=360)
   lbl6SR.configure(background='yellow',  width=12)

   lbl7SR = Label(AddRecPG1, text="Transport Cost", font = "Arial 15")
   lbl7SR.place(x=603, y=440)
   lbl7SR.configure(background='yellow',  width=12)

   lbl8SR = Label(AddRecPG1, text="Project Value", font = "Arial 15")
   lbl8SR.place(x=603, y=520)
   lbl8SR.configure(background='yellow',  width=12)
   ''''''
   global txtProjectNIP
   ProjectNIP = StringVar() # This will hold the input in the Username Textbox    
   txtProjectNIP= Entry(AddRecPG1, width=30, textvariable=ProjectNIP, font= "Arial 15")
   txtProjectNIP.place(x=500, y=160)

   global txtProjectDIP
   #ProjectDIP = StringVar() # This will hold the input in the Username Textbox    
   txtProjectDIP= Entry(AddRecPG1, highlightthickness=0, relief=FLAT, width=30, font= "Arial 15")
   txtProjectDIP.place(x=500, y=240)
   txtProjectDIP.insert(0, 'dd/mm/yy')
   txtProjectDIP.bind("<1>", pick_date)
   # dropdown one

   
   global txtProductNPick
   global ProductNPick

   cursor.execute("SELECT Product_Name FROM ProductT")
   global resultPN
   resultPN = cursor.fetchall()

   ProductNPick = StringVar() # This will hold the input in the Username Textbox    
   ProductNPick.set(resultPN[0])

   #SupplierSTIP.place(x=500, y=410)
   txtProductNPick= OptionMenu(AddRecPG1, ProductNPick, *resultPN)
   txtProductNPick.pack()
   txtProductNPick.place(x=650, y=320)

   # dropdown two 
   cursor.execute("SELECT Customer_Name FROM CustomerR")
   global resultCN
   resultCN = cursor.fetchall()

   global txtCustomerNPick
   global CustomerNPick

   CustomerNPick = StringVar() # This will hold the input in the Username Textbox    
   CustomerNPick.set(resultCN[0])

   txtCustomerNPick= OptionMenu(AddRecPG1, CustomerNPick, *resultCN)
   txtCustomerNPick.pack()
   txtCustomerNPick.place(x=650, y=400)
   
   # back to textbox 
   global txtTCIP
   TCIP = StringVar() # This will hold the input in the Username Textbox    
   txtTCIP= Entry(AddRecPG1, width=30, textvariable=TCIP, font= "Arial 15")
   txtTCIP.place(x=500, y=480)

   global txtPVIP
   PVIP = StringVar() # This will hold the input in the Username Textbox    
   txtPVIP= Entry(AddRecPG1, width=30, textvariable=PVIP, font= "Arial 15")
   txtPVIP.place(x=500, y=560)


   ''''''
   global cmdAddPRPG1
   cmdAddPRPG1 = Button(AddRecPG1, text="Add Project Record", width=17, font= "Arial 12", command=saveSaleRecord1)
   cmdAddPRPG1.place(x=400, y=650)#original - 60 
   cmdAddPRPG1.bind('<Enter>', on_enter23)
   cmdAddPRPG1.bind('<Leave>', on_leave23)

   global cmdAddCfSR
   cmdAddCfSR = Button(AddRecPG1, text="Add Customer Record", width=17, font= "Arial 12", command=callCustA)
   cmdAddCfSR.place(x=580, y=650)#original - 60 
   cmdAddCfSR.bind('<Enter>', on_enter25)
   cmdAddCfSR.bind('<Leave>', on_leave25)

   global cmdAddPfR
   cmdAddPfR = Button(AddRecPG1, text="Add Product Record", width=17, font= "Arial 12", command=callProductT)
   cmdAddPfR.place(x=760, y=650)#original - 60 
   cmdAddPfR.bind('<Enter>', on_enter22)
   cmdAddPfR.bind('<Leave>', on_leave22)
   #connection.close()


def pick_date(event):
   global cal
   global date_window
   date_window = Toplevel()
   date_window.grab_set()
   date_window.title('Choose date')
   date_window.geometry('250x220+590+370')
   cal = Calendar(date_window, selectmode = "day", date_pattern="mm/dd/y")
   cal.place(x=0, y=0)

   submit_dt_btn = Button(date_window, text='Submit', command=grab_date)
   submit_dt_btn.place(x=80, y=190)
   
def grab_date():
   txtProjectDIP.delete(0, END)
   txtProjectDIP.insert(0, cal.get_date())
   date_window.withdraw()



def clearSR1():
   txtProjectNIP.delete(0, END)
   txtProjectDIP.delete(0, END)
   txtTCIP.delete(0, END)
   txtPVIP.delete(0, END)


def saveSaleRecord1():
   #connection = sqlite3.connect('MainData.db')
   #connection.commit()
   ''' Take Product ID and Customer ID '''
   ProdNameDraft = ProductNPick.get()
   new_ProdNameDraft = eval(ProdNameDraft)
   global C_ProdName
   C_ProdName = new_ProdNameDraft[0]
   #print(C_ProdName)
   #connection.commit()
   cursor.execute(f"SELECT Product_ID FROM ProductT WHERE Product_Name = '{C_ProdName}' ")
   resultPI_raw = cursor.fetchall()
   #print(f"Product ID result => {resultPI_raw}")

   CustNameDraft = CustomerNPick.get()
   new_CustNameDraft = eval(CustNameDraft)
   C_CustName = new_CustNameDraft[0]
   cursor.execute(f"SELECT Customer_ID FROM CustomerR WHERE Customer_Name = '{C_CustName}' ")
   resultCI = cursor.fetchall()
   #print(f"Customer ID result => {resultCI}")

   ''''''
   global PIoutSR
   PIoutSR = resultPI_raw[0]
   #print(type(PIoutSR))
   #print(f' new number => {PIoutSR[0]}')
   CIout = resultCI[0]

   global PRNout
   global PVout_D 

   PRNout = txtProjectNIP.get()
   PRDout = txtProjectDIP.get()
   global PIoutSR_F
   PIoutSR_F = PIoutSR[0]
   CIout_F = CIout[0]
   TCout_D = txtTCIP.get()
   global TCout
   TCout = TCout_D.replace(' ', '')
   global TCoutI
   TCoutI = int(TCout)
   PVout_D = txtPVIP.get()
   global PVout
   PVout = PVout_D.replace(' ', '')
   global PVoutI
   PVoutI = int(PVout)


   #connection.commit()
   

   if (len(PRNout) > 0):
      cursor.execute("INSERT INTO SaleR VALUES (NULL, ?, ?, ?, ?, ?, ?)", (PRNout, PRDout, PIoutSR_F, CIout_F, TCout, PVout))
      connection.commit()
      clearSR1()
      getMName()
      callRECPG2()
   else:
      lbl8P = Label(AddRecPG1, text="All boxes must be filled", font = "Arial 10")
      lbl8P.place(x=570, y=540)
      lbl8P.configure(background='#678983',  width=25, foreground='white')
   
   
   #connection.close()

def getMName():
   cursor.execute(f'''
      SELECT MaterialR.Material_Name 
      FROM MaterialR INNER JOIN SaleR ON MaterialR.Product_ID = SaleR.Product_ID
      WHERE MaterialR.Product_ID = {PIoutSR_F}
   ''')
   global resultMN
   resultMN = cursor.fetchall()
   #print(f"Material Name => {resultMN}")
   #print(type(resultMN))
   resultMN_D = {}
   for item in resultMN:
      #print(item)
      letter = item[0]
      if letter not in resultMN_D:
         resultMN_D[letter] = item
   global resultMN_F
   resultMN_F = list(resultMN_D.values())
   #print(f'final result => {resultMN_F}')
   #print(f'first item => {resultMN_F[0]}')


#connection.commit()
cursor.execute("SELECT Product_Name FROM ProductT")
global resultPN
resultPN = cursor.fetchall()

cursor.execute("SELECT Customer_Name FROM CustomerR")
global resultCN
resultCN = cursor.fetchall()

#connection.commit()


def befbefcallSaleRecordPG1():
   cursor.execute("SELECT * FROM ProductT")
   global resultPNA
   resultPNA = cursor.fetchall()

   cursor.execute("SELECT * FROM CustomerR")
   global resultCNA
   resultCNA = cursor.fetchall()


   global resultPNNumb
   global resultCNNumb

   resultPNNumb = len(resultPNA)
   resultCNNumb = len(resultCNA)

def befcallSaleRecordPG1():
   befbefcallSaleRecordPG1()
   if (resultPNNumb < 1) and (resultCNNumb < 1):
      lblW = Label(homePG, text="Product and Customer Table must first be filled!", font = "Arial 10 ")
      lblW.place(x=525, y=580)
      lblW.configure(background='yellow',  width=35)
   else:
      #print("beyond zero")
      callRECPG1()


''' Sale Record Page 2 - Choose Material '''
def convMname(): 
   #new_resultMN_F = eval(resultMN_F)
   global MName_array
   MName_array = [item[0] for item in resultMN_F]
   global CTR_ARR
   CTR_ARR = len(MName_array)



CTRMN1  = 1
CTRMN2 = 1
CTRMN3 = 1
CTRMN4 = 1
CTRMN5 = 1
CTRMN6 = 1
CTRMN7 = 1
CTRMN8 = 1
CTRMN9 = 1
CTRMN10 = 1
CTRMN11 = 1

def callRECPG2():
   '''
   global CTRMN1
   global CTRMN2
   CTRMN1  = 1
   CTRMN2 = 1
   '''
   convMname()
   global AddRecPG2
   AddRecPG2 = Tk()
   AddRecPG2.title("Modify Screen")
   AddRecPG2.configure(background="#E6DDC4")
   AddRecPG2.geometry('1366x768')

   lblNavb = Label(AddRecPG2, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(AddRecPG2, text="Manager Application", font = "Arial 25 bold")
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(AddRecPG2, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   ''''''
   lbl2H =  Label(AddRecPG2, text=f"Add material for {C_ProdName} ", font = "Arial 25 bold")
   lbl2H.place(x=390, y=100)
   lbl2H.configure(background='#678983',  width=28, foreground='white')
   ''' Menu 1 '''
   lbl1pg2 = Label(AddRecPG2, text=MName_array[0], font = "Arial 15")
   lbl1pg2.place(x=350, y=160)
   lbl1pg2.configure(background='yellow',  width=12)

   global cmdadd1pg2
   cmdadd1pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR1)
   cmdadd1pg2.place(x=500, y=160)#original - 60 

   global cmdred1pg2
   cmdred1pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR1)
   cmdred1pg2.place(x=650, y=160)#original - 60 

   global lbl1Cpg2_old
   lbl1Cpg2_old = Label(AddRecPG2, text=CTRMN1, font = "Arial 15")
   lbl1Cpg2_old.place(x=800, y=160)
   lbl1Cpg2_old.configure(background='yellow',  width=12)

   global cmdAddRecNext
   cmdAddRecNext = Button(AddRecPG2, text="Save record and next", width=20, font= "Arial 12", command=SaveAndNext)
   cmdAddRecNext.place(x=580, y=650)#original - 60 
   cmdAddRecNext.bind('<Enter>', on_enter25)
   cmdAddRecNext.bind('<Leave>', on_leave25)
   
   ''' END MENU 1 '''


   if (CTR_ARR ==2):
      ''' END MENU 1 '''

      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 
   elif (CTR_ARR == 3):
      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      #global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      #global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      #global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 

      lbl3pg2 = Label(AddRecPG2, text=MName_array[2], font = "Arial 15")
      lbl3pg2.place(x=350, y=240)
      lbl3pg2.configure(background='yellow',  width=12)

      global cmdadd3pg2
      cmdadd3pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR3)
      cmdadd3pg2.place(x=500, y=240)#original - 60 

      global cmdred3pg2
      cmdred3pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR3)
      cmdred3pg2.place(x=650, y=240)#original - 60 

      global lbl3Cpg2_old
      lbl3Cpg2_old = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2_old.place(x=800, y=240)
      lbl3Cpg2_old.configure(background='yellow',  width=12)
   elif (CTR_ARR == 4):
      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      #global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      #global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      #global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 
      lbl3pg2 = Label(AddRecPG2, text=MName_array[2], font = "Arial 15")
      lbl3pg2.place(x=350, y=240)
      lbl3pg2.configure(background='yellow',  width=12)

      #global cmdadd3pg2
      cmdadd3pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR3)
      cmdadd3pg2.place(x=500, y=240)#original - 60 

      #global cmdred3pg2
      cmdred3pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR3)
      cmdred3pg2.place(x=650, y=240)#original - 60 

      #global lbl3Cpg2_old
      lbl3Cpg2_old = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2_old.place(x=800, y=240)
      lbl3Cpg2_old.configure(background='yellow',  width=12)



      lbl4pg2 = Label(AddRecPG2, text=MName_array[3], font = "Arial 15")
      lbl4pg2.place(x=350, y=280)
      lbl4pg2.configure(background='yellow',  width=12)

      global cmdadd4pg2
      cmdadd4pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR4)
      cmdadd4pg2.place(x=500, y=280)#original - 60 

      global cmdred4pg2
      cmdred4pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR4)
      cmdred4pg2.place(x=650, y=280)#original - 60 

      global lbl4Cpg2_old
      lbl4Cpg2_old = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2_old.place(x=800, y=280)
      lbl4Cpg2_old.configure(background='yellow',  width=12)
   elif (CTR_ARR == 5):
      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      #global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      #global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      #global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 
      lbl3pg2 = Label(AddRecPG2, text=MName_array[2], font = "Arial 15")
      lbl3pg2.place(x=350, y=240)
      lbl3pg2.configure(background='yellow',  width=12)

      #global cmdadd3pg2
      cmdadd3pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR3)
      cmdadd3pg2.place(x=500, y=240)#original - 60 

      #global cmdred3pg2
      cmdred3pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR3)
      cmdred3pg2.place(x=650, y=240)#original - 60 

      #global lbl3Cpg2_old
      lbl3Cpg2_old = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2_old.place(x=800, y=240)
      lbl3Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl4pg2 = Label(AddRecPG2, text=MName_array[3], font = "Arial 15")
      lbl4pg2.place(x=350, y=280)
      lbl4pg2.configure(background='yellow',  width=12)

      #global cmdred4pg2
      cmdadd4pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR4)
      cmdadd4pg2.place(x=500, y=280)#original - 60 

      #global cmdred4pg2
      cmdred4pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR4)
      cmdred4pg2.place(x=650, y=280)#original - 60 

      #global lbl4Cpg2_old
      lbl4Cpg2_old = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2_old.place(x=800, y=280)
      lbl4Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl5pg2 = Label(AddRecPG2, text=MName_array[4], font = "Arial 15")
      lbl5pg2.place(x=350, y=320)
      lbl5pg2.configure(background='yellow',  width=12)

      global cmdadd5pg2
      cmdadd5pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR5)
      cmdadd5pg2.place(x=500, y=320)#original - 60 

      global cmdred5pg2
      cmdred5pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR5)
      cmdred5pg2.place(x=650, y=320)#original - 60 

      global lbl5Cpg2_old
      lbl5Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl5Cpg2_old.place(x=800, y=320)
      lbl5Cpg2_old.configure(background='yellow',  width=12)
      ''''''
   elif (CTR_ARR == 6):
      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      #global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      #global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      #global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 
      lbl3pg2 = Label(AddRecPG2, text=MName_array[2], font = "Arial 15")
      lbl3pg2.place(x=350, y=240)
      lbl3pg2.configure(background='yellow',  width=12)

      #global cmdadd3pg2
      cmdadd3pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR3)
      cmdadd3pg2.place(x=500, y=240)#original - 60 

      #global cmdred3pg2
      cmdred3pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR3)
      cmdred3pg2.place(x=650, y=240)#original - 60 

      #global lbl3Cpg2_old
      lbl3Cpg2_old = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2_old.place(x=800, y=240)
      lbl3Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl4pg2 = Label(AddRecPG2, text=MName_array[3], font = "Arial 15")
      lbl4pg2.place(x=350, y=280)
      lbl4pg2.configure(background='yellow',  width=12)

      #global cmdred4pg2
      cmdadd4pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR4)
      cmdadd4pg2.place(x=500, y=280)#original - 60 

      #global cmdred4pg2
      cmdred4pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR4)
      cmdred4pg2.place(x=650, y=280)#original - 60 

      #global lbl4Cpg2_old
      lbl4Cpg2_old = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2_old.place(x=800, y=280)
      lbl4Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl5pg2 = Label(AddRecPG2, text=MName_array[4], font = "Arial 15")
      lbl5pg2.place(x=350, y=320)
      lbl5pg2.configure(background='yellow',  width=12)

      #global cmdadd5pg2
      cmdadd5pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR5)
      cmdadd5pg2.place(x=500, y=320)#original - 60 

      #global cmdred5pg2
      cmdred5pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR5)
      cmdred5pg2.place(x=650, y=320)#original - 60 

      #global lbl5Cpg2_old
      lbl5Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl5Cpg2_old.place(x=800, y=320)
      lbl5Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl6pg2 = Label(AddRecPG2, text=MName_array[5], font = "Arial 15")
      lbl6pg2.place(x=350, y=360)
      lbl6pg2.configure(background='yellow',  width=12)

      global cmdadd6pg2
      cmdadd6pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR6)
      cmdadd6pg2.place(x=500, y=360)#original - 60 

      global cmdred6pg2
      cmdred6pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR6)
      cmdred6pg2.place(x=650, y=360)#original - 60 

      global lbl6Cpg2_old
      lbl6Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl6Cpg2_old.place(x=800, y=360)
      lbl6Cpg2_old.configure(background='yellow',  width=12)
      ''''''
   elif (CTR_ARR == 7):
      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      #global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      #global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      #global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 
      lbl3pg2 = Label(AddRecPG2, text=MName_array[2], font = "Arial 15")
      lbl3pg2.place(x=350, y=240)
      lbl3pg2.configure(background='yellow',  width=12)

      #global cmdadd3pg2
      cmdadd3pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR3)
      cmdadd3pg2.place(x=500, y=240)#original - 60 

      #global cmdred3pg2
      cmdred3pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR3)
      cmdred3pg2.place(x=650, y=240)#original - 60 

      #global lbl3Cpg2_old
      lbl3Cpg2_old = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2_old.place(x=800, y=240)
      lbl3Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl4pg2 = Label(AddRecPG2, text=MName_array[3], font = "Arial 15")
      lbl4pg2.place(x=350, y=280)
      lbl4pg2.configure(background='yellow',  width=12)

      #global cmdred4pg2
      cmdadd4pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR4)
      cmdadd4pg2.place(x=500, y=280)#original - 60 

      #global cmdred4pg2
      cmdred4pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR4)
      cmdred4pg2.place(x=650, y=280)#original - 60 

      #global lbl4Cpg2_old
      lbl4Cpg2_old = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2_old.place(x=800, y=280)
      lbl4Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl5pg2 = Label(AddRecPG2, text=MName_array[4], font = "Arial 15")
      lbl5pg2.place(x=350, y=320)
      lbl5pg2.configure(background='yellow',  width=12)

      #global cmdadd5pg2
      cmdadd5pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR5)
      cmdadd5pg2.place(x=500, y=320)#original - 60 

      #global cmdred5pg2
      cmdred5pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR5)
      cmdred5pg2.place(x=650, y=320)#original - 60 

      #global lbl5Cpg2_old
      lbl5Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl5Cpg2_old.place(x=800, y=320)
      lbl5Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl6pg2 = Label(AddRecPG2, text=MName_array[5], font = "Arial 15")
      lbl6pg2.place(x=350, y=360)
      lbl6pg2.configure(background='yellow',  width=12)

      #global cmdadd6pg2
      cmdadd6pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR6)
      cmdadd6pg2.place(x=500, y=360)#original - 60 

      #global cmdred6pg2
      cmdred6pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR6)
      cmdred6pg2.place(x=650, y=360)#original - 60 

      #global lbl6Cpg2_old
      lbl6Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl6Cpg2_old.place(x=800, y=360)
      lbl6Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl7pg2 = Label(AddRecPG2, text=MName_array[6], font = "Arial 15")
      lbl7pg2.place(x=350, y=400)
      lbl7pg2.configure(background='yellow',  width=12)

      global cmdadd7pg2
      cmdadd7pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR7)
      cmdadd7pg2.place(x=500, y=400)#original - 60 

      global cmdred7pg2
      cmdred7pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR7)
      cmdred7pg2.place(x=650, y=400)#original - 60 

      global lbl7Cpg2_old
      lbl7Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl7Cpg2_old.place(x=800, y=400)
      lbl7Cpg2_old.configure(background='yellow',  width=12)
      ''''''
   elif (CTR_ARR == 8):
      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      #global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      #global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      #global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 
      lbl3pg2 = Label(AddRecPG2, text=MName_array[2], font = "Arial 15")
      lbl3pg2.place(x=350, y=240)
      lbl3pg2.configure(background='yellow',  width=12)

      #global cmdadd3pg2
      cmdadd3pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR3)
      cmdadd3pg2.place(x=500, y=240)#original - 60 

      #global cmdred3pg2
      cmdred3pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR3)
      cmdred3pg2.place(x=650, y=240)#original - 60 

      #global lbl3Cpg2_old
      lbl3Cpg2_old = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2_old.place(x=800, y=240)
      lbl3Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl4pg2 = Label(AddRecPG2, text=MName_array[3], font = "Arial 15")
      lbl4pg2.place(x=350, y=280)
      lbl4pg2.configure(background='yellow',  width=12)

      #global cmdred4pg2
      cmdadd4pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR4)
      cmdadd4pg2.place(x=500, y=280)#original - 60 

      #global cmdred4pg2
      cmdred4pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR4)
      cmdred4pg2.place(x=650, y=280)#original - 60 

      #global lbl4Cpg2_old
      lbl4Cpg2_old = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2_old.place(x=800, y=280)
      lbl4Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl5pg2 = Label(AddRecPG2, text=MName_array[4], font = "Arial 15")
      lbl5pg2.place(x=350, y=320)
      lbl5pg2.configure(background='yellow',  width=12)

      #global cmdadd5pg2
      cmdadd5pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR5)
      cmdadd5pg2.place(x=500, y=320)#original - 60 

      #global cmdred5pg2
      cmdred5pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR5)
      cmdred5pg2.place(x=650, y=320)#original - 60 

      #global lbl5Cpg2_old
      lbl5Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl5Cpg2_old.place(x=800, y=320)
      lbl5Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl6pg2 = Label(AddRecPG2, text=MName_array[5], font = "Arial 15")
      lbl6pg2.place(x=350, y=360)
      lbl6pg2.configure(background='yellow',  width=12)

      #global cmdadd6pg2
      cmdadd6pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR6)
      cmdadd6pg2.place(x=500, y=360)#original - 60 

      #global cmdred6pg2
      cmdred6pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR6)
      cmdred6pg2.place(x=650, y=360)#original - 60 

      #global lbl6Cpg2_old
      lbl6Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl6Cpg2_old.place(x=800, y=360)
      lbl6Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl7pg2 = Label(AddRecPG2, text=MName_array[6], font = "Arial 15")
      lbl7pg2.place(x=350, y=400)
      lbl7pg2.configure(background='yellow',  width=12)

      #global cmdadd7pg2
      cmdadd7pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR7)
      cmdadd7pg2.place(x=500, y=400)#original - 60 

      #global cmdred7pg2
      cmdred7pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR7)
      cmdred7pg2.place(x=650, y=400)#original - 60 

      #global lbl7Cpg2_old
      lbl7Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl7Cpg2_old.place(x=800, y=400)
      lbl7Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl8pg2 = Label(AddRecPG2, text=MName_array[7], font = "Arial 15")
      lbl8pg2.place(x=350, y=440)
      lbl8pg2.configure(background='yellow',  width=12)

      global cmdadd8pg2
      cmdadd8pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR8)
      cmdadd8pg2.place(x=500, y=440)#original - 60 

      global cmdred8pg2
      cmdred8pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR8)
      cmdred8pg2.place(x=650, y=440)#original - 60 

      global lbl8Cpg2_old
      lbl8Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl8Cpg2_old.place(x=800, y=440)
      lbl8Cpg2_old.configure(background='yellow',  width=12)
      ''''''
   elif (CTR_ARR == 9):
      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      #global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      #global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      #global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 
      lbl3pg2 = Label(AddRecPG2, text=MName_array[2], font = "Arial 15")
      lbl3pg2.place(x=350, y=240)
      lbl3pg2.configure(background='yellow',  width=12)

      #global cmdadd3pg2
      cmdadd3pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR3)
      cmdadd3pg2.place(x=500, y=240)#original - 60 

      #global cmdred3pg2
      cmdred3pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR3)
      cmdred3pg2.place(x=650, y=240)#original - 60 

      #global lbl3Cpg2_old
      lbl3Cpg2_old = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2_old.place(x=800, y=240)
      lbl3Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl4pg2 = Label(AddRecPG2, text=MName_array[3], font = "Arial 15")
      lbl4pg2.place(x=350, y=280)
      lbl4pg2.configure(background='yellow',  width=12)

      #global cmdred4pg2
      cmdadd4pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR4)
      cmdadd4pg2.place(x=500, y=280)#original - 60 

      #global cmdred4pg2
      cmdred4pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR4)
      cmdred4pg2.place(x=650, y=280)#original - 60 

      #global lbl4Cpg2_old
      lbl4Cpg2_old = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2_old.place(x=800, y=280)
      lbl4Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl5pg2 = Label(AddRecPG2, text=MName_array[4], font = "Arial 15")
      lbl5pg2.place(x=350, y=320)
      lbl5pg2.configure(background='yellow',  width=12)

      #global cmdadd5pg2
      cmdadd5pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR5)
      cmdadd5pg2.place(x=500, y=320)#original - 60 

      #global cmdred5pg2
      cmdred5pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR5)
      cmdred5pg2.place(x=650, y=320)#original - 60 

      #global lbl5Cpg2_old
      lbl5Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl5Cpg2_old.place(x=800, y=320)
      lbl5Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl6pg2 = Label(AddRecPG2, text=MName_array[5], font = "Arial 15")
      lbl6pg2.place(x=350, y=360)
      lbl6pg2.configure(background='yellow',  width=12)

      #global cmdadd6pg2
      cmdadd6pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR6)
      cmdadd6pg2.place(x=500, y=360)#original - 60 

      #global cmdred6pg2
      cmdred6pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR6)
      cmdred6pg2.place(x=650, y=360)#original - 60 

      #global lbl6Cpg2_old
      lbl6Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl6Cpg2_old.place(x=800, y=360)
      lbl6Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl7pg2 = Label(AddRecPG2, text=MName_array[6], font = "Arial 15")
      lbl7pg2.place(x=350, y=400)
      lbl7pg2.configure(background='yellow',  width=12)

      #global cmdadd7pg2
      cmdadd7pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR7)
      cmdadd7pg2.place(x=500, y=400)#original - 60 

      #global cmdred7pg2
      cmdred7pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR7)
      cmdred7pg2.place(x=650, y=400)#original - 60 

      #global lbl7Cpg2_old
      lbl7Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl7Cpg2_old.place(x=800, y=400)
      lbl7Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl8pg2 = Label(AddRecPG2, text=MName_array[7], font = "Arial 15")
      lbl8pg2.place(x=350, y=440)
      lbl8pg2.configure(background='yellow',  width=12)

      #global cmdadd8pg2
      cmdadd8pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR8)
      cmdadd8pg2.place(x=500, y=440)#original - 60 

      #global cmdred8pg2
      cmdred8pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR8)
      cmdred8pg2.place(x=650, y=440)#original - 60 

      #global lbl8Cpg2_old
      lbl8Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl8Cpg2_old.place(x=800, y=440)
      lbl8Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      ''''''
      lbl9pg2 = Label(AddRecPG2, text=MName_array[8], font = "Arial 15")
      lbl9pg2.place(x=350, y=480)
      lbl9pg2.configure(background='yellow',  width=12)

      global cmdadd9pg2
      cmdadd9pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR9)
      cmdadd9pg2.place(x=500, y=480)#original - 60 

      global cmdred9pg2
      cmdred9pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR9)
      cmdred9pg2.place(x=650, y=480)#original - 60 

      global lbl9Cpg2_old
      lbl9Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl9Cpg2_old.place(x=800, y=480)
      lbl9Cpg2_old.configure(background='yellow',  width=12)
      ''''''
   elif (CTR_ARR == 10):
      lbl2pg2 = Label(AddRecPG2, text=MName_array[1], font = "Arial 15")
      lbl2pg2.place(x=350, y=200)
      lbl2pg2.configure(background='yellow',  width=12)

      #global cmdadd2pg2
      cmdadd2pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR2)
      cmdadd2pg2.place(x=500, y=200)#original - 60 

      #global cmdred2pg2
      cmdred2pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR2)
      cmdred2pg2.place(x=650, y=200)#original + 40 
      #global lbl2Cpg2_old 
      lbl2Cpg2_old = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2_old.place(x=800, y=200)
      lbl2Cpg2_old.configure(background='yellow',  width=12) 
      lbl3pg2 = Label(AddRecPG2, text=MName_array[2], font = "Arial 15")
      lbl3pg2.place(x=350, y=240)
      lbl3pg2.configure(background='yellow',  width=12)

      #global cmdadd3pg2
      cmdadd3pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR3)
      cmdadd3pg2.place(x=500, y=240)#original - 60 

      #global cmdred3pg2
      cmdred3pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR3)
      cmdred3pg2.place(x=650, y=240)#original - 60 

      #global lbl3Cpg2_old
      lbl3Cpg2_old = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2_old.place(x=800, y=240)
      lbl3Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl4pg2 = Label(AddRecPG2, text=MName_array[3], font = "Arial 15")
      lbl4pg2.place(x=350, y=280)
      lbl4pg2.configure(background='yellow',  width=12)

      #global cmdred4pg2
      cmdadd4pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR4)
      cmdadd4pg2.place(x=500, y=280)#original - 60 

      #global cmdred4pg2
      cmdred4pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR4)
      cmdred4pg2.place(x=650, y=280)#original - 60 

      #global lbl4Cpg2_old
      lbl4Cpg2_old = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2_old.place(x=800, y=280)
      lbl4Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl5pg2 = Label(AddRecPG2, text=MName_array[4], font = "Arial 15")
      lbl5pg2.place(x=350, y=320)
      lbl5pg2.configure(background='yellow',  width=12)

      #global cmdadd5pg2
      cmdadd5pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR5)
      cmdadd5pg2.place(x=500, y=320)#original - 60 

      #global cmdred5pg2
      cmdred5pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR5)
      cmdred5pg2.place(x=650, y=320)#original - 60 

      #global lbl5Cpg2_old
      lbl5Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl5Cpg2_old.place(x=800, y=320)
      lbl5Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl6pg2 = Label(AddRecPG2, text=MName_array[5], font = "Arial 15")
      lbl6pg2.place(x=350, y=360)
      lbl6pg2.configure(background='yellow',  width=12)

      #global cmdadd6pg2
      cmdadd6pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR6)
      cmdadd6pg2.place(x=500, y=360)#original - 60 

      #global cmdred6pg2
      cmdred6pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR6)
      cmdred6pg2.place(x=650, y=360)#original - 60 

      #global lbl6Cpg2_old
      lbl6Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl6Cpg2_old.place(x=800, y=360)
      lbl6Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl7pg2 = Label(AddRecPG2, text=MName_array[6], font = "Arial 15")
      lbl7pg2.place(x=350, y=400)
      lbl7pg2.configure(background='yellow',  width=12)

      #global cmdadd7pg2
      cmdadd7pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR7)
      cmdadd7pg2.place(x=500, y=400)#original - 60 

      #global cmdred7pg2
      cmdred7pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR7)
      cmdred7pg2.place(x=650, y=400)#original - 60 

      #global lbl7Cpg2_old
      lbl7Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl7Cpg2_old.place(x=800, y=400)
      lbl7Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      lbl8pg2 = Label(AddRecPG2, text=MName_array[7], font = "Arial 15")
      lbl8pg2.place(x=350, y=440)
      lbl8pg2.configure(background='yellow',  width=12)

      #global cmdadd8pg2
      cmdadd8pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR8)
      cmdadd8pg2.place(x=500, y=440)#original - 60 

      #global cmdred8pg2
      cmdred8pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR8)
      cmdred8pg2.place(x=650, y=440)#original - 60 

      #global lbl8Cpg2_old
      lbl8Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl8Cpg2_old.place(x=800, y=440)
      lbl8Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      ''''''
      lbl9pg2 = Label(AddRecPG2, text=MName_array[8], font = "Arial 15")
      lbl9pg2.place(x=350, y=480)
      lbl9pg2.configure(background='yellow',  width=12)

      #global cmdadd9pg2
      cmdadd9pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR9)
      cmdadd9pg2.place(x=500, y=480)#original - 60 

      #global cmdred9pg2
      cmdred9pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR9)
      cmdred9pg2.place(x=650, y=480)#original - 60 

      #global lbl9Cpg2_old
      lbl9Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl9Cpg2_old.place(x=800, y=480)
      lbl9Cpg2_old.configure(background='yellow',  width=12)
      ''''''
      ''''''
      lbl10pg2 = Label(AddRecPG2, text=MName_array[9], font = "Arial 15")
      lbl10pg2.place(x=350, y=520)
      lbl10pg2.configure(background='yellow',  width=12)

      global cmdadd10pg2
      cmdadd10pg2 = Button(AddRecPG2, text="Add", width=12, font= "Arial 12", command=addCTR10)
      cmdadd10pg2.place(x=500, y=520)#original - 60 

      global cmdred10pg2
      cmdred10pg2 = Button(AddRecPG2, text="Reduce", width=12, font= "Arial 12", command=redCTR10)
      cmdred10pg2.place(x=650, y=520)#original - 60 

      global lbl10Cpg2_old
      lbl10Cpg2_old = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl10Cpg2_old.place(x=800, y=520)
      lbl10Cpg2_old.configure(background='yellow',  width=12)
      ''''''


TMprice1 = 0
TMprice2 = 0
TMprice3 = 0
TMprice4 = 0
TMprice5 = 0
TMprice6 = 0
TMprice7 = 0
TMprice8 = 0
TMprice9 = 0
TMprice10 = 0


def SaveAndNext():
   e_MPrice()
   global TMprice1
   global TMprice2
   global TMprice3
   global TMprice4
   global TMprice5
   global TMprice6
   global TMprice7
   global TMprice8
   global TMprice9
   global TMprice10
   global TOTALPRICE_M
   CTRMN1F = CTRMN1
   print(type(CTRMN1F))
   print(f'number of material one => {CTRMN1F}')
   TMprice1 = CTRMN1F * Mprice1F
   if CTR_ARR == 2:
      CTRMN2F = CTRMN2
      TMprice2 = CTRMN2F * Mprice2F
   elif CTR_ARR == 3:
      CTRMN2F = CTRMN2
      CTRMN3F = CTRMN3
      TMprice2 = CTRMN2F * Mprice2F
      TMprice3 = CTRMN3F * Mprice3F
   elif CTR_ARR == 4:
      CTRMN2F = CTRMN2
      CTRMN3F = CTRMN3
      CTRMN4F = CTRMN4
      TMprice2 = CTRMN2F * Mprice2F
      TMprice3 = CTRMN3F * Mprice3F
      TMprice4 = CTRMN4F * Mprice4F
   elif CTR_ARR == 5:
      CTRMN2F = CTRMN2
      CTRMN3F = CTRMN3
      CTRMN4F = CTRMN4
      CTRMN5F = CTRMN5
      TMprice2 = CTRMN2F * Mprice2F
      TMprice3 = CTRMN3F * Mprice3F
      TMprice4 = CTRMN4F * Mprice4F
      TMprice5 = CTRMN5F * Mprice5F
   elif CTR_ARR == 6:
      CTRMN2F = CTRMN2
      CTRMN3F = CTRMN3
      CTRMN4F = CTRMN4
      CTRMN5F = CTRMN5
      CTRMN6F = CTRMN6
      TMprice2 = CTRMN2F * Mprice2F
      TMprice3 = CTRMN3F * Mprice3F
      TMprice4 = CTRMN4F * Mprice4F
      TMprice5 = CTRMN5F * Mprice5F
      TMprice6 = CTRMN6F * Mprice6F
   elif CTR_ARR == 7:
      CTRMN2F = CTRMN2
      CTRMN3F = CTRMN3
      CTRMN4F = CTRMN4
      CTRMN5F = CTRMN5
      CTRMN6F = CTRMN6
      CTRMN7F = CTRMN7
      TMprice2 = CTRMN2F * Mprice2F
      TMprice3 = CTRMN3F * Mprice3F
      TMprice4 = CTRMN4F * Mprice4F
      TMprice5 = CTRMN5F * Mprice5F
      TMprice6 = CTRMN6F * Mprice6F
      TMprice7 = CTRMN7F * Mprice7F
   elif CTR_ARR == 8:
      CTRMN2F = CTRMN2
      CTRMN3F = CTRMN3
      CTRMN4F = CTRMN4
      CTRMN5F = CTRMN5
      CTRMN6F = CTRMN6
      CTRMN7F = CTRMN7
      CTRMN8F = CTRMN8
      TMprice2 = CTRMN2F * Mprice2F
      TMprice3 = CTRMN3F * Mprice3F
      TMprice4 = CTRMN4F * Mprice4F
      TMprice5 = CTRMN5F * Mprice5F
      TMprice6 = CTRMN6F * Mprice6F
      TMprice7 = CTRMN7F * Mprice7F
      TMprice8 = CTRMN8F * Mprice8F

   elif CTR_ARR == 9:
      CTRMN2F = CTRMN2
      CTRMN3F = CTRMN3
      CTRMN4F = CTRMN4
      CTRMN5F = CTRMN5
      CTRMN6F = CTRMN6
      CTRMN7F = CTRMN7
      CTRMN8F = CTRMN8
      CTRMN9F = CTRMN9
      TMprice2 = CTRMN2F * Mprice2F
      TMprice3 = CTRMN3F * Mprice3F
      TMprice4 = CTRMN4F * Mprice4F
      TMprice5 = CTRMN5F * Mprice5F
      TMprice7 = CTRMN7F * Mprice7F
      TMprice8 = CTRMN8F * Mprice8F
      TMprice9 = CTRMN9F * Mprice9F
   elif CTR_ARR == 10:
      CTRMN2F = CTRMN2
      CTRMN3F = CTRMN3
      CTRMN4F = CTRMN4
      CTRMN5F = CTRMN5
      CTRMN6F = CTRMN6
      CTRMN7F = CTRMN7
      CTRMN8F = CTRMN8
      CTRMN9F = CTRMN9
      CTRMN10F = CTRMN10
      TMprice2 = CTRMN2F * Mprice2F
      TMprice3 = CTRMN3F * Mprice3F
      TMprice4 = CTRMN4F * Mprice4F
      TMprice5 = CTRMN5F * Mprice5F
      TMprice6 = CTRMN6F * Mprice6F
      TMprice7 = CTRMN7F * Mprice7F
      TMprice8 = CTRMN8F * Mprice8F
      TMprice9 = CTRMN9F * Mprice9F
      TMprice10 = CTRMN10F * Mprice10F
   
   TOTALPRICE_M = int(TMprice1 + TMprice2 + TMprice3 + TMprice4 + TMprice5 + TMprice6 + TMprice7 + TMprice8 + TMprice9 + TMprice10)
   print(TOTALPRICE_M)
   callREGPG3()

def e_MPrice():
   global Mprice1F
   global Mprice2F
   global Mprice3F
   global Mprice4F
   global Mprice5F
   global Mprice6F
   global Mprice7F
   global Mprice8F
   global Mprice9F
   global Mprice10F
   cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[0]}' ")
   Mprice1 = cursor.fetchall()
   Mprice1F = integer_checker(Mprice1)
   print(f'type mprice1f => {type(Mprice1F)}')
   if CTR_ARR == 2:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
   elif CTR_ARR == 3:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[2]}' ")
      Mprice3 = cursor.fetchall()
      Mprice3F = integer_checker(Mprice3)
   elif CTR_ARR == 4:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[2]}' ")
      Mprice3 = cursor.fetchall()
      Mprice3F = integer_checker(Mprice3)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[3]}' ")
      Mprice4 = cursor.fetchall()
      Mprice4F = integer_checker(Mprice4)
   elif CTR_ARR == 5:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[2]}' ")
      Mprice3 = cursor.fetchall()
      Mprice3F = integer_checker(Mprice3)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[3]}' ")
      Mprice4 = cursor.fetchall()
      Mprice4F = integer_checker(Mprice4)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[4]}' ")
      Mprice5 = cursor.fetchall()
      Mprice5F = integer_checker(Mprice5)
   elif CTR_ARR == 6:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[2]}' ")
      Mprice3 = cursor.fetchall()
      Mprice3F = integer_checker(Mprice3)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[3]}' ")
      Mprice4 = cursor.fetchall()
      Mprice4F = integer_checker(Mprice4)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[4]}' ")
      Mprice5 = cursor.fetchall()
      Mprice5F = integer_checker(Mprice5)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[5]}' ")
      Mprice6 = cursor.fetchall()
      Mprice6F = integer_checker(Mprice6)
   elif CTR_ARR == 7:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[2]}' ")
      Mprice3 = cursor.fetchall()
      Mprice3F = integer_checker(Mprice3)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[3]}' ")
      Mprice4 = cursor.fetchall()
      Mprice4F = integer_checker(Mprice4)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[4]}' ")
      Mprice5 = cursor.fetchall()
      Mprice5F = integer_checker(Mprice5)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[5]}' ")
      Mprice6 = cursor.fetchall()
      Mprice6F = integer_checker(Mprice6)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[6]}' ")
      Mprice7 = cursor.fetchall()
      Mprice7F = integer_checker(Mprice7)
   elif CTR_ARR == 8:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[2]}' ")
      Mprice3 = cursor.fetchall()
      Mprice3F = integer_checker(Mprice3)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[3]}' ")
      Mprice4 = cursor.fetchall()
      Mprice4F = integer_checker(Mprice4)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[4]}' ")
      Mprice5 = cursor.fetchall()
      Mprice5F = integer_checker(Mprice5)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[5]}' ")
      Mprice6 = cursor.fetchall()
      Mprice6F = integer_checker(Mprice6)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[6]}' ")
      Mprice7 = cursor.fetchall()
      Mprice7F = integer_checker(Mprice7)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[7]}' ")
      Mprice8 = cursor.fetchall()
      Mprice8F = integer_checker(Mprice8)
   elif CTR_ARR == 9:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[2]}' ")
      Mprice3 = cursor.fetchall()
      Mprice3F = integer_checker(Mprice3)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[3]}' ")
      Mprice4 = cursor.fetchall()
      Mprice4F = integer_checker(Mprice4)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[4]}' ")
      Mprice5 = cursor.fetchall()
      Mprice5F = integer_checker(Mprice5)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[5]}' ")
      Mprice6 = cursor.fetchall()
      Mprice6F = integer_checker(Mprice6)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[6]}' ")
      Mprice7 = cursor.fetchall()
      Mprice7F = integer_checker(Mprice7)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[7]}' ")
      Mprice8 = cursor.fetchall()
      Mprice8F = integer_checker(Mprice8)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[8]}' ")
      Mprice9 = cursor.fetchall()
      Mprice9F = integer_checker(Mprice9)
   elif CTR_ARR == 10:
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[1]}' ")
      Mprice2 = cursor.fetchall()
      Mprice2F = integer_checker(Mprice2)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[2]}' ")
      Mprice3 = cursor.fetchall()
      Mprice3F = integer_checker(Mprice3)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[3]}' ")
      Mprice4 = cursor.fetchall()
      Mprice4F = integer_checker(Mprice4)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[4]}' ")
      Mprice5 = cursor.fetchall()
      Mprice5F = integer_checker(Mprice5)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[5]}' ")
      Mprice6 = cursor.fetchall()
      Mprice6F = integer_checker(Mprice6)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[6]}' ")
      Mprice7 = cursor.fetchall()
      Mprice7F = integer_checker(Mprice7)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[7]}' ")
      Mprice8 = cursor.fetchall()
      Mprice8F = integer_checker(Mprice8)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[8]}' ")
      Mprice9 = cursor.fetchall()
      Mprice9F = integer_checker(Mprice9)
      cursor.execute(f"SELECT Price_per_one FROM MaterialR WHERE Material_Name = '{MName_array[9]}' ")
      Mprice10 = cursor.fetchall()
      Mprice10F = integer_checker(Mprice10)

def integer_checker(input): 
   if (isinstance(input, int) == True):
      input = input
      print(f'integer{input}')
      return input
   elif (isinstance(input, list) == True):
      input = int(input[0][0])
      print(f'list => {input}')
      return input
   else: 
      input = int(input[0][0].replace(' ', ''))


def addCTR1():
   global CTRMN1
   lbl1Cpg2_old.destroy()
   CTRMN1 = CTRMN1 + 1
   lbl1Cpg2 = Label(AddRecPG2, text= CTRMN1, font = "Arial 15")
   lbl1Cpg2.place(x=800, y=160)
   lbl1Cpg2.configure(background='yellow',  width=12)


      
def addCTR2():
   global CTRMN2
   lbl2Cpg2_old.destroy()
   CTRMN2 = CTRMN2 + 1
   lbl2Cpg2 = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
   lbl2Cpg2.place(x=800, y=200)
   lbl2Cpg2.configure(background='yellow',  width=12)

def addCTR3():
   global CTRMN3
   lbl3Cpg2_old.destroy()
   CTRMN3 = CTRMN3 + 1
   lbl3Cpg2 = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
   lbl3Cpg2.place(x=800, y=240)
   lbl3Cpg2.configure(background='yellow',  width=12)

def addCTR4():
   global CTRMN4
   lbl4Cpg2_old.destroy()
   CTRMN4 = CTRMN4 + 1
   lbl4Cpg2 = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
   lbl4Cpg2.place(x=800, y=280)
   lbl4Cpg2.configure(background='yellow',  width=12)

def addCTR5():
   global CTRMN5
   lbl5Cpg2_old.destroy()
   CTRMN5 = CTRMN5 + 1
   lbl5Cpg2 = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
   lbl5Cpg2.place(x=800, y=320)
   lbl5Cpg2.configure(background='yellow',  width=12)

def addCTR6():
   global CTRMN6
   lbl6Cpg2_old.destroy()
   CTRMN6 = CTRMN6 + 1
   lbl6Cpg2 = Label(AddRecPG2, text=CTRMN6, font = "Arial 15")
   lbl6Cpg2.place(x=800, y=360)
   lbl6Cpg2.configure(background='yellow',  width=12)

def addCTR7():
   global CTRMN7
   lbl7Cpg2_old.destroy()
   CTRMN7 = CTRMN7 + 1
   lbl7Cpg2 = Label(AddRecPG2, text=CTRMN7, font = "Arial 15")
   lbl7Cpg2.place(x=800, y=400)
   lbl7Cpg2.configure(background='yellow',  width=12)

def addCTR8():
   global CTRMN8
   lbl8Cpg2_old.destroy()
   CTRMN8 = CTRMN8 + 1
   lbl8Cpg2 = Label(AddRecPG2, text=CTRMN8, font = "Arial 15")
   lbl8Cpg2.place(x=800, y=440)
   lbl8Cpg2.configure(background='yellow',  width=12)

def addCTR9():
   global CTRMN9
   lbl9Cpg2_old.destroy()
   CTRMN9 = CTRMN9 + 1
   lbl9Cpg2 = Label(AddRecPG2, text=CTRMN9, font = "Arial 15")
   lbl9Cpg2.place(x=800, y=480)
   lbl9Cpg2.configure(background='yellow',  width=12)

def addCTR10():
   global CTRMN10
   lbl10Cpg2_old.destroy()
   CTRMN10 = CTRMN10 + 1
   lbl10Cpg2 = Label(AddRecPG2, text=CTRMN10, font = "Arial 15")
   lbl10Cpg2.place(x=800, y=520)
   lbl10Cpg2.configure(background='yellow',  width=12)
'''
def addCTR11():
   global CTRMN11
   lbl11Cpg2_old.destroy()
   CTRMN11 = CTRMN11 + 1
   lbl11Cpg2 = Label(AddRecPG2, text=CTRMN11, font = "Arial 15")
   lbl11Cpg2.place(x=800, y=560)
   lbl11Cpg2.configure(background='yellow',  width=12)
'''
def redCTR1():
   global CTRMN1
   lbl1Cpg2_old.destroy()
   if CTRMN1 == 0:
      CTRMN1 = CTRMN1
      lbl1Cpg2 = Label(AddRecPG2, text= CTRMN1, font = "Arial 15")
      lbl1Cpg2.place(x=800, y=160)
      lbl1Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN1 = CTRMN1 - 1
      lbl1Cpg2 = Label(AddRecPG2, text= CTRMN1, font = "Arial 15")
      lbl1Cpg2.place(x=800, y=160)
      lbl1Cpg2.configure(background='yellow',  width=12)

def redCTR2():
   global CTRMN2
   lbl2Cpg2_old.destroy()
   if CTRMN2 == 0:
      CTRMN2 = CTRMN2
      lbl2Cpg2 = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2.place(x=800, y=200)
      lbl2Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN2 = CTRMN2 - 1
      lbl2Cpg2 = Label(AddRecPG2, text=CTRMN2, font = "Arial 15")
      lbl2Cpg2.place(x=800, y=200)
      lbl2Cpg2.configure(background='yellow',  width=12)

def redCTR3():
   global CTRMN3
   lbl3Cpg2_old.destroy()
   if CTRMN3 == 0:
      CTRMN3 = CTRMN3
      lbl3Cpg2 = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2.place(x=800, y=240)
      lbl3Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN3 = CTRMN3 - 1
      lbl3Cpg2 = Label(AddRecPG2, text=CTRMN3, font = "Arial 15")
      lbl3Cpg2.place(x=800, y=240)
      lbl3Cpg2.configure(background='yellow',  width=12)

def redCTR4():
   global CTRMN4
   lbl4Cpg2_old.destroy()
   if CTRMN4 == 0:
      CTRMN4 = CTRMN4
      lbl4Cpg2 = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2.place(x=800, y=280)
      lbl4Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN4 = CTRMN4 - 1
      lbl4Cpg2 = Label(AddRecPG2, text=CTRMN4, font = "Arial 15")
      lbl4Cpg2.place(x=800, y=280)
      lbl4Cpg2.configure(background='yellow',  width=12)

def redCTR5():
   global CTRMN5
   lbl5Cpg2_old.destroy()
   if CTRMN5 == 0:
      CTRMN5 = CTRMN5
      lbl5Cpg2 = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl5Cpg2.place(x=800, y=320)
      lbl5Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN5 = CTRMN5 - 1
      lbl5Cpg2 = Label(AddRecPG2, text=CTRMN5, font = "Arial 15")
      lbl5Cpg2.place(x=800, y=320)
      lbl5Cpg2.configure(background='yellow',  width=12)

def redCTR6():
   global CTRMN6
   lbl6Cpg2_old.destroy()
   if CTRMN6 == 0:
      CTRMN6 = CTRMN6
      lbl6Cpg2 = Label(AddRecPG2, text=CTRMN6, font = "Arial 15")
      lbl6Cpg2.place(x=800, y=360)
      lbl6Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN6 = CTRMN6 - 1
      lbl6Cpg2 = Label(AddRecPG2, text=CTRMN6, font = "Arial 15")
      lbl6Cpg2.place(x=800, y=360)
      lbl6Cpg2.configure(background='yellow',  width=12)

def redCTR7():
   global CTRMN7
   lbl7Cpg2_old.destroy()
   if CTRMN7 == 0:
      CTRMN7 = CTRMN7
      lbl7Cpg2 = Label(AddRecPG2, text=CTRMN7, font = "Arial 15")
      lbl7Cpg2.place(x=800, y=400)
      lbl7Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN7 = CTRMN7 - 1
      lbl7Cpg2 = Label(AddRecPG2, text=CTRMN7, font = "Arial 15")
      lbl7Cpg2.place(x=800, y=400)
      lbl7Cpg2.configure(background='yellow',  width=12)

def redCTR8():
   global CTRMN8
   lbl8Cpg2_old.destroy()
   if CTRMN8 == 0:
      CTRMN8 = CTRMN8
      lbl8Cpg2 = Label(AddRecPG2, text=CTRMN8, font = "Arial 15")
      lbl8Cpg2.place(x=800, y=440)
      lbl8Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN8 = CTRMN8 - 1
      lbl8Cpg2 = Label(AddRecPG2, text=CTRMN8, font = "Arial 15")
      lbl8Cpg2.place(x=800, y=440)
      lbl8Cpg2.configure(background='yellow',  width=12)

def redCTR9():
   global CTRMN9
   lbl9Cpg2_old.destroy()
   if CTRMN9 == 0:
      CTRMN9 = CTRMN9
      lbl9Cpg2 = Label(AddRecPG2, text=CTRMN9, font = "Arial 15")
      lbl9Cpg2.place(x=800, y=480)
      lbl9Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN9 = CTRMN9 - 1
      lbl9Cpg2 = Label(AddRecPG2, text=CTRMN9, font = "Arial 15")
      lbl9Cpg2.place(x=800, y=480)
      lbl9Cpg2.configure(background='yellow',  width=12)

def redCTR10():
   global CTRMN10
   lbl10Cpg2_old.destroy()
   if CTRMN10 == 0:
      CTRMN10 = CTRMN10
      lbl10Cpg2 = Label(AddRecPG2, text=CTRMN10, font = "Arial 15")
      lbl10Cpg2.place(x=800, y=520)
      lbl10Cpg2.configure(background='yellow',  width=12)
   else:
      CTRMN10 = CTRMN10 - 1
      lbl10Cpg2 = Label(AddRecPG2, text=CTRMN10, font = "Arial 15")
      lbl10Cpg2.place(x=800, y=520)
      lbl10Cpg2.configure(background='yellow',  width=12)


''' Add instalation cost '''
def callREGPG3():
   global AddRecPG3
   AddRecPG3 = Tk()
   AddRecPG3.title("Modify instalasi Screen")
   AddRecPG3.configure(background="#E6DDC4")
   AddRecPG3.geometry('1366x768')

   lblNavb = Label(AddRecPG3, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(AddRecPG3, text="Manager Application", font = "Arial 25 bold")
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(AddRecPG3, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   ''''''
   lbl3SR = Label(AddRecPG3, text="Nama Pekerjaan", font = "Arial 15")
   lbl3SR.place(x=603, y=120)
   lbl3SR.configure(background='yellow',  width=13)

   global txtPekerjaNPick
   global PekerjaNPick

   cursor.execute("SELECT Pekerja_Name FROM Instalasi")
   global resultPekN
   resultPekN = cursor.fetchall()

   PekerjaNPick = StringVar() # This will hold the input in the Username Textbox    
   PekerjaNPick.set(resultPekN[0])

   #SupplierSTIP.place(x=500, y=410)
   txtPekerjaNPick= OptionMenu(AddRecPG3, PekerjaNPick, *resultPekN)
   txtPekerjaNPick.pack()
   txtPekerjaNPick.place(x=650, y=160)

   lbl4SR = Label(AddRecPG3, text="Jumlah Pekerja", font = "Arial 15")
   lbl4SR.place(x=603, y=200)
   lbl4SR.configure(background='yellow',  width=12)

   global txtPekNIP
   PekNIP = StringVar() # This will hold the input in the Username Textbox    
   txtPekNIP= Entry(AddRecPG3, width=30, textvariable=PekNIP, font= "Arial 15")
   txtPekNIP.place(x=500, y=240)

   lbl5SR = Label(AddRecPG3, text="Jumlah hari", font = "Arial 15")
   lbl5SR.place(x=603, y=280)
   lbl5SR.configure(background='yellow',  width=12)

   global txtHariNIP
   HariNIP = StringVar() # This will hold the input in the Username Textbox    
   txtHariNIP= Entry(AddRecPG3, width=30, textvariable=HariNIP, font= "Arial 15")
   txtHariNIP.place(x=500, y=320)

   global cmdAddAnother
   cmdAddAnother = Button(AddRecPG3, text="Add another", width=17, font= "Arial 12", command=saveandreload)
   cmdAddAnother.place(x=400, y=650)#original - 60 

   global cmdGoSumm
   cmdGoSumm = Button(AddRecPG3, text="Save and summarize", width=20, font= "Arial 12", command=saveandsumm)
   cmdGoSumm.place(x=580, y=650)#original - 60 

def saveSaleRecord3(): 
   ''' Take Pekerja Gaji'''
   PekNameDraft = PekerjaNPick.get()
   new_PekNameDraft = eval(PekNameDraft)
   global C_PekName 
   C_PekName = new_PekNameDraft[0]
   cursor.execute(f"SELECT Gaji_Per_Hari FROM Instalasi WHERE Pekerja_Name = '{C_PekName}' ")
   resultGH_raw = cursor.fetchall()
   resultGH = resultGH_raw[0]
   ''''''
   global resultGH_F 
   global PNUMoutI
   global DNUMoutI
   resultGH_F = int(resultGH[0])
   print(type(resultGH))
   PNUMout_D = txtPekNIP.get()
   PNUMout = PNUMout_D.replace(' ', '')
   PNUMoutI = int(PNUMout)
   print(f'jumlah karyawan => {PNUMoutI}')
   DNUMout_D = txtHariNIP.get()
   DNUMout = DNUMout_D.replace(' ', '')
   DNUMoutI = int(DNUMout)
   add_everything()

def saveandreload():
   saveSaleRecord3()
   clearins()
   callREGPG3()

def saveandsumm():
   saveSaleRecord3()
   clearins()
   callSummary()

def clearins():
   txtHariNIP.delete(0, END)
   txtPekNIP.delete(0, END)

total_instalasi = 0

def add_everything():
   global total_instalasi 
   total_instalasi_D = resultGH_F * PNUMoutI * DNUMoutI
   total_instalasi = total_instalasi + total_instalasi_D
   print(total_instalasi)
   




def callSummary(): 
   global SummPG
   SummPG = Tk()
   SummPG.title("Modify instalasi Screen")
   SummPG.configure(background="#E6DDC4")
   SummPG.geometry('1366x768')

   lblNavb = Label(SummPG, text="", font = "Arial 20")
   lblNavb.place(x=0, y=0)
   lblNavb.configure(background='#678983',  width=100, height=2)
   
   global cmd1H
   cmd1H =  Button(SummPG, text="Manager Application", font = "Arial 25 bold")
   cmd1H.place(x=8, y=0)
   cmd1H.configure(  background ="#678983", width=18, foreground="white", borderwidth=0)

   cmd1H.bind('<Enter>', on_enter5)
   cmd1H.bind('<Leave>', on_leave5)

   lblCover = Label(SummPG, text="", font = "Arial 20")
   lblCover.place(x=203, y=90)
   lblCover.configure(background='#678983',  width=58, height=19)
   ''''''
   lbl3SR = Label(SummPG, text="Summary", font = "Arial 20 bold")
   lbl3SR.place(x=580, y=100)
   lbl3SR.configure(background='yellow',  width=15)

   lbl1SM = Label(SummPG, text= "Project Name", font = "Arial 20")
   lbl1SM.place(x=350, y=160)
   lbl1SM.configure(background='yellow',  width=15)

   lbl1AM = Label(SummPG, text= PRNout, font = "Arial 20")
   lbl1AM.place(x=650, y=160)
   lbl1AM.configure(background='white',  width=25)

   lbl2SM = Label(SummPG, text= "Project Value", font = "Arial 20")
   lbl2SM.place(x=350, y=220)
   lbl2SM.configure(background='yellow',  width=15)

   lbl2AM = Label(SummPG, text= PVout_D, font = "Arial 20")
   lbl2AM.place(x=650, y=220)
   lbl2AM.configure(background='white',  width=25)

   lbl3SM = Label(SummPG, text= "Material Expense", font = "Arial 20")
   lbl3SM.place(x=350, y=280)
   lbl3SM.configure(background='yellow',  width=15)

   lbl3AM = Label(SummPG, text= TOTALPRICE_M, font = "Arial 20")
   lbl3AM.place(x=650, y=280)
   lbl3AM.configure(background='white',  width=25)

   lbl4SM = Label(SummPG, text= "Instalation Expense", font = "Arial 20")
   lbl4SM.place(x=350, y=340)
   lbl4SM.configure(background='yellow',  width=15)

   lbl4AM = Label(SummPG, text= total_instalasi, font = "Arial 20")
   lbl4AM.place(x=650, y=340)
   lbl4AM.configure(background='white',  width=25)


   lbl5SM = Label(SummPG, text= "Labour Expense", font = "Arial 20")
   lbl5SM.place(x=350, y=400)
   lbl5SM.configure(background='yellow',  width=15) 

   print(f'type pvouti => {type(PVoutI)}')
   labExp = (PVoutI * 10) // 100

   lbl5AM = Label(SummPG, text= labExp, font = "Arial 20")
   lbl5AM.place(x=650, y=400)
   lbl5AM.configure(background='white',  width=25)

   lbl8SM = Label(SummPG, text= "Transport Expense", font = "Arial 20")
   lbl8SM.place(x=350, y=480)
   lbl8SM.configure(background='yellow',  width=15) 


   lbl8AM = Label(SummPG, text= TCout, font = "Arial 20")
   lbl8AM.place(x=650, y=480)
   lbl8AM.configure(background='white',  width=25)

   lbl6SM = Label(SummPG, text= "Gross Profit", font = "Arial 20")
   lbl6SM.place(x=350, y=540)
   lbl6SM.configure(background='yellow',  width=15)
   global GrossP
   GrossP = PVoutI - (labExp + TOTALPRICE_M + total_instalasi + TCoutI)

   lbl6AM = Label(SummPG, text= GrossP, font = "Arial 20")
   lbl6AM.place(x=650, y=540)
   lbl6AM.configure(background='white',  width=25)
   '''
   lbl7SM = Label(SummPG, text= "Gross Profit Margin", font = "Arial 20")
   lbl7SM.place(x=350, y=580)
   lbl7SM.configure(background='yellow',  width=15)
   global GrossPM
   GrossPM = (GrossP // PVoutI) * 100


   lbl7AM = Label(SummPG, text= GrossPM, font = "Arial 20")
   lbl7AM.place(x=650, y=580)
   lbl7AM.configure(background='white',  width=25)
   '''

   global cmdConfRec
   cmdConfRec = Button(SummPG, text="Confirm Record", width=20, font= "Arial 15", command=ConfSumm)
   cmdConfRec.place(x=555, y=650)#original - 60 

def ConfSumm():
   ProjectNF = PRNout
   ProjectVF = PVoutI
   MaterialEF = TOTALPRICE_M
   InstalationE = total_instalasi
   GrossProfitF = GrossP
   cursor.execute("INSERT INTO SaleRF VALUES (NULL, ?, ?, ?, ?, ?)", (ProjectNF, ProjectVF, MaterialEF, InstalationE, GrossProfitF))
   connection.commit()
   callHome()


#connection.close()
RegisterPG.mainloop()




