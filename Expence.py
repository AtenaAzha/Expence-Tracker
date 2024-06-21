import tkinter as tk
from tkinter import *
from tkinter import ttk
from twilio.rest import Client
import random
import smtplib
from tkinter import messagebox
import mysql.connector

#create main class
class APP(tk.Tk):
    def __init__(self , *args , **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        self.title('expence tracker')
        self.geometry('500x800')

        #create pages
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (StartPage, Page1, Page2, Page3 , Page4 , Page5 ):
            frame =F(container , self) 

            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)


    def show_frame(self , cont):
        frame = self.frames[cont]
        frame.tkraise()
#creating and handelling the getting phone or email page
class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.configure(bg = 'light blue')
        self.start_lab = Label(self , text = 'Exprence Tracker' , font=('Helvetica', 16, 'bold') , bg = 'light blue')
        self.start_lab.place(x = 150 , y = 50)

        label1 = Label(self , text = 'Hi dear user welcome :)' , width = 20 , font = ('bold' , 15) , bg = 'light blue')
        label1.place(x = 120 , y = 110)
        


        label2 = Label(self , text = 'Please Enter your Email'  , font = ('bold' , 10) , bg = 'light blue')
        label2.place(x = 50 , y = 260)
        self.email_ent = Entry(self , width = 30 , fg = 'gray')
        self.email_ent.place(x = 50 , y = 290)
        self.email_ent.insert(0 , 'Email')

        #handeling the frequently username
        def fre_user():
            userlist = []
            users = self.email_ent.get()
            if users in userlist:
                controller.show_frame(Page3)
                userlist.append(users)
                print(userlist)
            else:
                erorr_mes = messagebox.showerror('error box','You have to sign in first')

        button3 = ttk.Button(self, text = 'Home',
        command = fre_user)
        button3.place(x = 40 , y = 720)

        #sendig code
        def sending():
            if self.email_ent.get() == '':
                top2 =  messagebox.showerror('error box','your entries are empty!')
            else:
                #you should insert sender email or gmail
                sender = 'azha82.atena@gmail.com'
                subject = 'expence code'
                message = ['1234' , '4567' , '8345' ,'1209' , '3561' , '3481','9023', '7219','2137']
                message_ = random.choice(message)
                text = f'subject{subject}\n\n{message_}'
                server = smtplib.SMTP('smtp.gmail.com' , 587)
                server.starttls()
                #you should sender password
                server.login(sender , '***********')
                server.sendmail(sender , self.email_ent.get() , text)
                self.start_lab.config(text = 'the code has sent on Email')

        button1 = Button(self , text = 'send' , command = sending)
        button1.place(x = 150 , y = 320)
        #error handelling
        def handel():
            if self.email_ent.get().strip() == '':
                top1 = messagebox.showerror('error box','your entries are empty!')
            else:
                 controller.show_frame(Page1)
        #swich buttons         
        button2 = Button(self , text = 'next >>' ,command = handel)
        button2.place(x = 450 , y = 720)

#creating and handelling the getting code page
class Page1(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.configure(bg = 'light yellow')

        cod_lab = Label(self , text = 'Please enter the code has sent to you' , bg = 'light yellow')
        cod_lab.place(x = 40 , y = 150)
        self.code_ent = Entry(self , fg = 'gray')
        self.code_ent.insert(0 ,'Code')
        self.code_ent.place(x = 40 , y = 180)
        #error handelling
        def handel():
            if self.code_ent.get().strip() == '':
                top1 = messagebox.showerror('error box','you have to enter the code that was sent!')

            else:
                 controller.show_frame(Page2)
        #swich buttons         
        button1 = ttk.Button(self, text = ' next>>',
            command = handel)
        button1.place(x = 430 , y = 210)

        
        button2 = ttk.Button(self, text = ' <<back',
            command = lambda : controller.show_frame(StartPage))
        button2.place(x = 350 , y = 210)
      
 

#creating and handelling the getting username and whole money page 
class Page2(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = 'light green')
        label = Label(self, text = 'We try you can expend your money in right way \n and you can save some money for your future \n so enter whole the money you have right now. :)' , 
                bg = 'light green')
        label.place(x = 10 , y = 50)

        money_ent = Entry(self , fg = 'gray')
        money_ent.insert(0 ,'Whole Money')
        money_ent.place(x = 40 , y = 180)

        self.name_ent = Entry(self , fg = 'gray')
        self.name_ent.insert(0 ,'username')
        self.name_ent.place(x = 40 , y = 240)

        #design the database of user information
        app_db = mysql.connector.connect(
              host = 'localhost',
              user = 'root',
              #you should use your password
              password = '5560813192',
              database = 'expence_data'
        )
        app_cursor = app_db.cursor(buffered = True)
        # query = ('CREATE TABLE users (Username VARCHAR(255) PRIMARY KEY , WholeMoney VARCHAR(255))')
        # result = app_cursor.execute(query)
        # app_db.commit()
        
        #error handelling
        def handel():
             if self.name_ent.get().strip() == '' or money_ent.get().strip() == '':
                 top1 = messagebox.showerror('error box','your entries are empty!')
             else:
                  controller.show_frame(Page3)
        #swich buttons
        button1 = ttk.Button(self, text = 'next>>',
                            command = handel)
     
        button1.place(x = 430 , y = 210)
  
        button2 = ttk.Button(self, text = '<<back',
                command = lambda : controller.show_frame(Page1))
        button2.place(x = 350 , y = 210)
 
        #insert the entry data into database 
        def enter_money():
            query1 = ('INSERT INTO users (WholeMoney) VALUES (%s)' , (money_ent.get(),))
            result1 = app_cursor.execute(*query1)
            app_db.commit()
        def enter_name():
            query2 = ('INSERT INTO users (Username) VALUES (%s)' , (self.name_ent.get(),))
            result2 = app_cursor.execute(*query2)
            app_db.commit()
        get_button = Button(self, text = 'Enter' , bg = 'light green' , command = enter_money)
        get_button.place(x = 180 , y = 170)
        get_button2 = Button(self, text = 'Enter' , bg = 'light green' , command = enter_name)
        get_button2.place(x = 180 , y = 240)
#creating and handelling the home page
class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = 'light blue')
        self.label = Label(self , text = 'Please enter your items like example' , bg = 'light blue')
        self.label.place(x = 500, y = 30)
        self.label1 = Label(self , text = '' , bg = 'light blue')
        self.label1.place(x = 700 , y = 220)
        
        app_db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            #you should use your password
            password  = '5560813192',
            database = 'expence_data'
        )
        app_cursor = app_db.cursor(buffered = True)
        # query = ('CREATE TABLE items(Category VARCHAR(255) , Item VARCHAR(255) , Date VARCHAR(255) , Price VARCHAR(255))')
        # result = app_cursor.execute(query)
        # app_db.commit()
        
        #gettin the items 
        def stulist():


            item_ent = Entry(self)
            item_ent.grid(row = 40 , column = 70)

            
            #create menu to show example
            var = tk.StringVar()
            optionMenu = ttk.OptionMenu(parent , var , 'For Example')
            optionMenu.grid(row = 10)

            menu = optionMenu["menu"]
            


            sublist1 = Menu(menu , tearoff = False)
            menu.add_cascade(label = 'Fun' , menu = sublist1)
            sublist1.add_command(label = 'movie ticket' , command = None)
            sublist1.add_command(label = 'fooball game ticket' , command = None)
            sublist1.add_command(label = 'another' , command = None)



            sublist2 = tk.Menu(menu , tearoff= False)
            menu.add_cascade(label = "Food" , menu = sublist2)
            sublist2.add_command(label = "pizza" , command = None)
            sublist2.add_command(label = "coffee" , command = None)
            sublist2.add_command(label = 'stace' , command = None)
            sublist2.add_command(label = 'another' , command = None)

            
            sublist3 = Menu(menu , tearoff = False)
            menu.add_cascade(label = 'Clothe' , menu = sublist3) 
            sublist3.add_command(label = 'dress' , command = None)       
            sublist3.add_command(label = 'pants' , command = None)       
            sublist3.add_command(label = 'shirt' , command = None)       
            sublist3.add_command(label = 'shoes' , command = None)       
            sublist3.add_command(label = 'another' , command = None)  


            sublist4 = Menu(menu , tearoff = False)
            menu.add_cascade(label = "Class's fee" , menu = sublist4) 
            sublist4.add_command(label = 'English' , command = None)       
            sublist4.add_command(label = 'dance' , command = None)       
            sublist4.add_command(label = 'sport' , command = None)       
            sublist4.add_command(label = 'sntrument' , command = None)       
            sublist4.add_command(label = 'another' , command = None) 


            sublist5 = Menu(menu , tearoff = False)
            menu.add_cascade(label = 'beauty' , menu = sublist5) 
            sublist5.add_command(label = 'makeup stuff' , command = None)       
            sublist5.add_command(label = 'hulthy stuff' , command = None)       
            sublist5.add_command(label = 'another' , command = None) 


            sublist6 = Menu(menu , tearoff = False)
            menu.add_cascade(label = 'remedial job' , menu = sublist6) 
            sublist6.add_command(label = 'dental' , command = None)       
            sublist6.add_command(label = 'sik' , command = None)       
            sublist6.add_command(label = 'tropy' , command = None)
            sublist6.add_command(label = 'another' , command = None)
             
            #insert items into database
            def saved():
               
                query1 = ('INSERT INTO items (Item) VALUES (%s)' , (item_ent.get(),)) 
                result1 = app_cursor.execute(*query1)
                app_db.commit()
            save_butt = Button(self , text = 'Save' , bg = 'light blue' , command = saved)
            save_butt.grid(row = 40 , column = 100)
        #getting category    
        def catlist():
            cat_ent = Entry(self)
            cat_ent.grid(row = 30 , column = 70)
            #insert categories into database
            def saving():
                query_ = ('INSERT INTO items (Category) VALUES (%s)' , (cat_ent.get(),))
                result_ = app_cursor.execute(*query_)
                app_db.commit()
            save_but = Button(self , text = 'save' , command = saving)
            save_but.grid(row = 30 , column = 100)    

        cat_button = ttk.Button(self , text = 'category' , command = catlist)
        cat_button.grid(row = 30 , column = 50 , padx=10 , pady=10)
        stu_button = ttk.Button(self , text = 'stuff' , command = stulist)
        stu_button.grid(row = 40 , column = 50 , padx=10 , pady=10)
        #getting date of bueing the items
        def date():
            date_ent = Entry(parent)
            date_ent.insert(0 , '1/1/2000')
            date_ent.grid(row = 50 , column = 70)  
            #insert date into database 
            def entery():
                query7 = ('INSERT INTO items (Date) VALUES (%s)' , (date_ent.get(),))
                result7 = app_cursor.execute(*query7)
                app_db.commit()

            butt = Button(parent , text = 'enter' , command = entery)
            butt.grid(row = 50 , column = 100)            

        dat_button = ttk.Button(self , text = 'date' , command = date)
        dat_button.grid(row = 50 , column = 50 , padx=10 ,pady=10)
        #getting the prive of items
        def price():
            price_ent = Entry(parent)
            price_ent.insert(0 , 'price $')
            price_ent.grid(row = 60 , column = 70)
            #insert price into  database
            def entry2():
                query8 = ('INSERT INTO items (Price) VALUES (%s)' , (price_ent.get(),))
                result8 = app_cursor.execute(*query8)
                app_db.commit()
                #worning about price of items
                p = int(price_ent.get())
                if p > 1000:
                   self.label1.config(text = 'you spend too much for this item depend on how much you have!!')
        
            butto = Button(parent , text = 'enter' , command = entry2)            
            butto.grid(row = 60 , column = 100)

        pri_button = ttk.Button(self , text = 'price' , command = price)
        pri_button.grid(row = 60 , column = 50 , padx=10 , pady=10)


        button1 = Button(self , text = 'History' , 
                command = lambda : controller.show_frame(Page4))
        button1.place(x = 430 , y = 250)

        
        button1 = Button(self , text = 'Profile' , 
                command = lambda : controller.show_frame(Page5))
        button1.place(x = 430 , y = 210)

        

#creating and handelling history page
class Page4(tk.Frame):
    def __init__(self , parent , controller):
        tk.Frame.__init__(self , parent)
        self.configure(bg = 'light blue')
        self.his_lab = Label(self , text = 'History' , font=('Helvetica', 16, 'bold') , bg = 'light blue')
        self.his_lab.place(x = 150 , y = 50)
        
        app_db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            #you should use your password
            password  = '5560813192',
            database = 'expence_data'
        )
        app_cursor = app_db.cursor(buffered = True)

        #create table to show data that insert into database
        ind = 0
        def show_his():
            global ind
            data_table = ttk.Treeview(self , columns = ('Category','Items','Date','Price'))
            data_table.place(x = 180 , y = 280)
            data_table.heading('Category', text = 'CATEGORY')
            data_table.heading('Items' , text = 'ITEMS')
            data_table.heading('Date' , text = 'DATE')
            data_table.heading('Price' , text = 'PRICE')
            scroller = Scrollbar(self)
            scroller.grid(row = 200 , column = 200)
            scroller.config(command = data_table.yview)


            query3 = ('SELECT * FROM items')
            result3 = app_cursor.execute(query3)
            item_ = app_cursor.fetchall()
            for item in item_:
                data_table.insert('' , 'end' , value = (item[0] , item[1] , item[2] ,item[3]))
            app_db.commit()
        #swich buttons
        button_show = Button(self , text = 'show history' , command = show_his)
        button_show.grid(row=1 , column=1)


        button1 = ttk.Button(self, text = 'Home',
        command = lambda : controller.show_frame(Page3))
     
        button1.place(x = 430 , y = 210)

#creating and hanelling the profile page
class Page5(tk.Frame):
    def __init__(self , parent , controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = 'light blue')
        self.pro_lab = Label(self , text = 'Your Profile' , font=('Helvetica', 16, 'bold') , bg = 'light blue')
        self.pro_lab.place(x = 150 , y = 50)

        app_db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            #you should use your password
            password  = '5560813192',
            database = 'expence_data'
        )
        app_cursor = app_db.cursor(buffered = True)


        #create table to show data that insert into database
        def show_info():
            data_user = ttk.Treeview(self , columns = ('YourWholeMoney','YourUsername'))
            data_user.place(x = 180 , y = 280)
            data_user.heading('YourWholeMoney', text = 'Your whole money')
            data_user.heading('YourUsername' , text = 'Your user name')
            
            query9 = ('SELECT * FROM users')
            result9 = app_cursor.execute(query9)
            user_ = app_cursor.fetchall()
            for user in user_:
                data_user.insert('' , 'end' , value = (user[0] , user[-1]))
            app_db.commit()

        show_bott = Button(self , text = 'show profile' , command = show_info)
        show_bott.place(x = 1 , y = 1)
        button1 = ttk.Button(self, text = 'Home',
                command = lambda : controller.show_frame(Page3))
     
        button1.place(x = 430 , y = 210)

        button1 = ttk.Button(self, text = 'Home',
        command = lambda : controller.show_frame(Page3))
     
        button1.place(x = 430 , y = 210)




app = APP()
app.mainloop()