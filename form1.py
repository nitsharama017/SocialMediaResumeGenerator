from tkinter import *
import sqlite3
import RegisterForm as R
import SocialResumePage as S
from tkinter import messagebox
def login():
    def exitprogram():
        messagebox.showinfo("Exit",'Exiting the Program')
        login_screen.destroy()
    def sigin_clicked():
        login_screen.destroy()
        R.register_function()
    def login_clicked():
        messagebox.showinfo("Directing", "Directing to your SocialMedia Resume...")
        usernameValue =username.get()
        try:
            try:
                conn = sqlite3.connect('data_base1.db')
                cur = conn.cursor()
            except:
                cur.execute("CREATE TABLE user_details(Name VARCHAR(128), Username VARCHAR(128), Gender VARCHAR(128), Bio VARCHAR(128), Email VARCHAR(128), LinkedinURL VARCHAR(128),FacebookURL VARCHAR(128), InstagramURL VARCHAR(128), SpotifyURL VARCHAR(128),SnapchatURL VARCHAR(128), TwitterURL VARCHAR(128), ImageName VARCHAR(128)")
            finally:
                cur.execute(f'SELECT Username FROM user_details WHERE Username="{usernameValue}"')
            value1 = cur.fetchone()
            userstr =value1[0]
            print(f"value from database {userstr}")
            print(f"value from tkinter entry {usernameValue}")
            if (userstr == usernameValue):
                login_screen.destroy()
                S.resumepage(userstr)
        except:
            messagebox.showerror("Error", 'Enter correct Username!')
        finally:
            conn.commit()
            conn.close()

    login_screen= Tk()
    login_screen.title("Login Page")
    login_screen.geometry("950x950")
    login_screen.config(bg='#EAE3CB')
    f1=Frame(login_screen).grid()
    f2=Frame(login_screen).grid()

    l1=Label(f1,text="   WELCOME TO", bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 20 bold")
    l1.grid(row=0, columnspan=5,padx=250,pady=10)

    l2=Label(f1,text="SOCIAL MEDIA RESUME GENERATOR!", bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 20 bold")
    l2.grid(row=1, columnspan=5,padx=250)
    lab = Label(f1, text="Enter UserName ", width=20,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 15 bold")
    lab.grid(row=5,column=1,padx=150,pady=40)
    l1_2=Label(f1,text="Already registered? Enter user name",fg='#63535B',font="TimesNewRoman 20 bold")
    l1_2.grid(row=4, columnspan=5,padx=150,pady=10)
    ########get username#######3
    username = Entry(f1,width=35)
    username.grid(row=5,column=2,sticky="W")

    ######login button######
    loginbutton = Button(f2, text = "Get SocialMedia Resume",height=2,width=20,bg="#2F9576", fg="#63535B",font="TimesNewRoman 10 bold",command=login_clicked)
    loginbutton.grid(row=7, columnspan=20,padx=250,pady=10)

    l1_2=Label(f1,text="OR",fg='#63535B',font="TimesNewRoman 20 bold")
    l1_2.grid(row=8, columnspan=5,padx=150,pady=10)
    ########Sigin button######
    signin = Button(f2, text = "Register Details",height=2,width=20,bg="#2F9576", fg="#63535B",font="TimesNewRoman 10 bold",command=sigin_clicked)
    signin.grid(row=9, columnspan=20,padx=250,pady=10)

    signin = Button(f2, text="Exit", height=2, width=20, bg="black", fg="white",font="TimesNewRoman 10 bold", command=exitprogram)
    signin.grid(row=15, columnspan=20, padx=250, pady=10)

    login_screen.mainloop()