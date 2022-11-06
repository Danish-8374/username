from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import re
import mysql.connector
import pyttsx3

class Register():
    def __init__(self,root):
        self.root=root
        self.root.title('Register Page')
        self.root.geometry('1600x790+0+0')
        
        # text-to-speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')

        self.engine.setProperty('voice',self.voices[1].id)

        # Variable
        self.name_var= StringVar()
        self.email_var= StringVar()
        self.contact_var= StringVar()
        self.gender_var= StringVar()
        self.country_var=StringVar()
        self.id_var= StringVar()
        self.id_num_var= StringVar()
        self.password_var= StringVar()
        self.con_password_var= StringVar()
        self.check_var= IntVar()

        # Background Image
        self.bg=ImageTk.PhotoImage(file='bg_beach.jpg')
        bg_lbl=Label(self.root,image=self.bg,bd=0,relief=RAISED)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        logo_img=Image.open('logo.png')
        logo_img=logo_img.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)


        #Title Frame
        title_frame=Frame(self.root,bd=1,relief=RIDGE)
        title_frame.place(x=450,y=28,width=550,height=82)

        title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text='USER REGISTER FORM',font=('times new roman',25,'bold','italic'),fg='darkblue')
        title_lbl.place(x=10,y=10)


        # Information Frame
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=550,height=550)


        #Unsername
        username_lbl=Label(main_frame,text='Username:',font=('times new roman',16,'bold'))
        username_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        entry_username=ttk.Entry(main_frame,textvariable=self.name_var,font=('times new roman',15),width=25)
        entry_username.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # callback and validation register
        validate_name=self.root.register(self.check_name)
        entry_username.config(validate='key',validatecommand=(validate_name,'%P'))


        #Email
        email_lbl=Label(main_frame,text='Email:',font=('times new roman',16,'bold'))
        email_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        entry_email=ttk.Entry(main_frame,textvariable=self.email_var,font=('times new roman',15),width=25)
        entry_email.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #Contact
        contact_lbl=Label(main_frame,text='Contact:',font=('times new roman',16,'bold'))
        contact_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        entry_contact=ttk.Entry(main_frame,textvariable=self.contact_var,font=('times new roman',15),width=25)
        entry_contact.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # callback and validation register
        validate_contact=self.root.register(self.check_contact)
        entry_contact.config(validate='key',validatecommand=(validate_contact,'%P'))

        #Gender
        gender_lbl=Label(main_frame,text='Select Gender:',font=('times new roman',16,'bold'))
        gender_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        gender_frame=Frame(main_frame)
        gender_frame.place(x=200,y=125,width=280,height=35)
        
        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value='Male',text='Male',font=('times new roman',15))
        radio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set('Male')
        radio_female=Radiobutton(gender_frame,value='Female',variable=self.gender_var,text='Female',font=('times new roman',15))
        radio_female.grid(row=0,column=1,padx=10,pady=0,sticky=W)

        #Country
        country_lbl=Label(main_frame,text='Select Country:',font=('times new roman',16,'bold'))
        country_lbl.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        country_name_list=['India','UK','USA','Afganistan','Germany','Pakistan']
        droplist=OptionMenu(main_frame,self.country_var,*country_name_list)
        droplist.config(width=21,font=('times new roman',15),bg='White')
        self.country_var.set('Select your Country')
        droplist.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Select ID Type
        id_type_lbl=Label(main_frame,text='Select ID Type:',font=('times new roman',16,'bold'))
        id_type_lbl.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_var,font=('times new roman',15),justify='center',state='readonly',width=23)
        self.combo_id_type['values']=('Select your ID','Aadhar Card','Passport','Driving Licence')

        self.combo_id_type.grid(row=5,column=1,padx=10,pady=5)
        self.combo_id_type.current(0)

        #Select ID Number
        id_num_lbl=Label(main_frame,text='ID Number:',font=('times new roman',16,'bold'))
        id_num_lbl.grid(row=6,column=0,padx=10,pady=5,sticky=W)

        entry_id_num=ttk.Entry(main_frame,textvariable=self.id_num_var,font=('times new roman',15),width=25)
        entry_id_num.grid(row=6,column=1,padx=10,pady=5,sticky=W)

        #Password
        password_lbl=Label(main_frame,text='Password:',font=('times new roman',16,'bold'))
        password_lbl.grid(row=7,column=0,padx=10,pady=5,sticky=W)

        entry_password=ttk.Entry(main_frame,textvariable=self.password_var,font=('times new roman',15),width=25)
        entry_password.grid(row=7,column=1,padx=10,pady=5,sticky=W)

        # Confirm Password
        conf_password_lbl=Label(main_frame,text='Confirm Password:',font=('times new roman',16,'bold'))
        conf_password_lbl.grid(row=8,column=0,padx=10,pady=5,sticky=W)

        entry_conf_password=ttk.Entry(main_frame,textvariable=self.con_password_var,font=('times new roman',15),width=25)
        entry_conf_password.grid(row=8,column=1,padx=10,pady=5,sticky=W)

        # Check Frame
        check_frame=Frame(main_frame)
        check_frame.place(x=130,y=380,width=300,height=60)
        
        check_btn=Checkbutton(check_frame,variable=self.check_var,text='Agree Our terms & Conditions',font=('times new roman',16),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=0,sticky=W)

        self.check_lbl=Label(check_frame,text='',font=('times new roman',12,'bold'),fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)

        # Button Frame
        btn_frame=Frame(main_frame)
        btn_frame.place(x=30,y=450,width=480,height=70)

        save_data=Button(btn_frame,text='Save Data',command=self.validation,font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        verify_data=Button(btn_frame,text='Verify Data',command=self.verify_data,font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        verify_data.grid(row=0,column=1,padx=1,sticky=W)

        clear_data=Button(btn_frame,command=self.clear_data,text='Clear Data',font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)

    #called back Function
    def check_name(self,name):
        if name.isalname():
            return True
        if name=="":
            return True
        else:
            messagebox.showerror('Invalid','Not allowed'+name[-1])
            return False

    # Check Contact
    def check_contact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror('Invalid','Invalid Entry')
            return False

    def check_password(self,password):
        if len(password)<=21:
            return True
            # if re.match("^(?=.*[0,9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
            #     return True
            # else:
            #     messagebox.showinfo('Invalid','Enter valid password (Example:Danish@123)')
            #     return False
        else:
            messagebox.showerror('Invalid','Length Try to exceed')
            return False

    def check_email(self,email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                messagebox.showinfo('Alert','Invalid email enter valid user email (Example:Danish@gmail.com)')
                return False
        else:
            messagebox.showerror('Invalid','Email length is too small')
            return False
    
    # validation
    def validation(self):
        if self.name_var.get()=="":
            self.engine.say('Please enter your name.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your name.',parent=self.root)
        
        elif self.email_var.get()=="":
            self.engine.say('Please enter your E-mail ID.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your E-mail ID.',parent=self.root)
        
        elif self.contact_var.get()=="" or len(self.contact_var.get())!=10:
            self.engine.say('Please enter the Valid Contact.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter the Valid Contact.',parent=self.root)
        
        elif self.gender_var.get()=="":
            self.engine.say('Please enter your Gender.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your Gender.',parent=self.root)
        
        elif self.country_var.get()=='Select your Country':
            self.engine.say('Please enter your Country name.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your Country name.',parent=self.root)
        
        elif self.id_var.get()=='Select your ID':
            self.engine.say('Please enter your ID Type.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your ID Type.',parent=self.root)
        
        elif self.id_num_var.get()=="":
            self.engine.say('Please enter your ID Number.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your ID Number.',parent=self.root)
        
        elif len(self.id_num_var.get())!=14:
            self.engine.say('Please enter 14 Digit ID Number only.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter 14 Digit Number only.',parent=self.root)
        
        elif self.password_var.get()=="":
            self.engine.say('Please enter your Password.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please enter your Password.',parent=self.root)
        
        elif self.con_password_var.get()=="":
            self.engine.say('Please confirm your Password.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please confirm your Password.',parent=self.root)

        elif self.con_password_var.get()!=self.password_var.get():
            self.engine.say('Password and Confirm Password must be same.')
            self.engine.runAndWait()
            messagebox.showerror('Error','Password and Confirm Password must be same.',parent=self.root)
        
        elif self.email_var.get()!=None and self.password_var.get()!=None:
            x=self.check_email(self.email_var.get())
            y=self.check_password(self.password_var.get())
        
        if (x==True) and (y==True):
            if self.check_var.get()==0:
                self.engine.say('Please Agree Our terms & Conditions')
                self.engine.runAndWait()
                self.check_lbl.config(text='Please Agree Our terms & Conditions',fg='red')
            else:
                self.check_lbl.config(text='Checked',fg='green')

                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Danish@123',database='mydata_register')
                    mycursor=conn.cursor()
                    mycursor.execute('Insert into register (name_var,email_var,contact_var,gender_var,country_var,id_var,id_num_var,password_var) values (%s,%s,%s,%s,%s,%s,%s,%s)',(self.name_var.get(),self.email_var.get(),self.contact_var.get(),self.gender_var.get(),self.country_var.get(),self.id_var.get(),self.id_num_var.get(),self.password_var.get()))                    
                    conn.commit()
                    conn.close()

                    self.engine.say(f'Your registration successfully completed your username:{self.name_var.get()},Password:{self.password_var.get()}.')
                    self.engine.runAndWait()
                    messagebox.showinfo('Successfully',f'Your registration successfully completed your username:{self.name_var.get()},Password:{self.password_var.get()}.')
                except Exception as es:
                    messagebox.showerror('Error',f'Due to:{list(es)}',parent=self.root)
                    
    def verify_data(self):
        value=(self.name_var.get(),self.email_var.get(),self.contact_var.get(),self.gender_var.get(),self.country_var.get(),self.id_var.get(),self.id_num_var.get(),self.password_var.get())

        data=f'Name: {value[0]}\n\nEmail: {value[1]}\n\nContact: {value[2]}\n\nGender: {value[3]}\n\nCountry_name: {value[4]}\n\nID: {value[5]}\n\nID_Number: {value[6]}\n\nPassword: {value[7]}'
        messagebox.showinfo("Details",data)

    def clear_data(self):
        self.name_var.set('')
        self.email_var.set('')
        self.contact_var.set('')
        self.gender_var.set('Male')
        self.country_var.set('Select your Country')
        self.id_var.set('Select your ID')
        self.id_num_var.set('')
        self.password_var.set('')
        self.con_password_var.set('')
        self.check_var.set(0)



if __name__=='__main__':
    root=Tk()
    
    obj=Register(root)
    
    root.mainloop()