from tkinter import *
import webbrowser
import sqlite3
import form1 as f
from PIL import ImageTk,Image
from tkinter import messagebox


#window
def resumepage(value):
    usernameArgs = value
    def exitpage():
            messagebox.askokcancel("Redirecting","To Main Page?")
            root.destroy()
            f.login()
    def openlinkedin():#-------------------------------------#########
            url1 = resumeLinkedin
            webbrowser.open(url1)
    def openfacebook():#-------------------------------------#########
            url2 = resumeFacebook
            webbrowser.open(url2)
    def openinstagram():#-------------------------------------#########
            url3 = resumeInstagram
            webbrowser.open(url3)
    def openspotify():#-------------------------------------#########
            url4 = resumeSpotify
            webbrowser.open(url4)
    def opensnapchat():#-------------------------------------#########
            url5 = resumeSnapchat
            webbrowser.open(url5)
    def opentwitter():#-------------------------------------#########
            url6 = resumeTwitter
            webbrowser.open(url6)
    try:
        conn = sqlite3.connect('data_base1.db')
        cur = conn.cursor()
    except:
        cur.execute("CREATE TABLE user_details(Name VARCHAR(128), Username VARCHAR(128), Gender VARCHAR(128), Bio VARCHAR(128), Email VARCHAR(128), LinkedinURL VARCHAR(128),FacebookURL VARCHAR(128), InstagramURL VARCHAR(128), SpotifyURL VARCHAR(128),SnapchatURL VARCHAR(128), TwitterURL VARCHAR(128), ImageName VARCHAR(128)")
    finally:
        cur.execute(f'SELECT * FROM user_details WHERE Username="{usernameArgs}"')
        userList = cur.fetchall()
    Newlist =userList
    emptylist = []
    for i in Newlist[0]:
        print(i)
        emptylist.append(i)

    resumeName, resumeUsername, resumeGender, resumeBio, resumeEmail, resumeLinkedin, resumeFacebook, resumeInstagram, resumeSpotify, resumeSnapchat, resumeTwitter, resumeImage = emptylist

####-------TKINTER------####
    root = Tk()
    root.geometry('1300x900')
    root.title('Social Media Resume')
#Frames
    frame1=Frame(root).grid()
    frame2=Frame(root).grid()
    frame3 =Frame(root).grid()

    Label (root,text="Social Media Resume",fg='#0e005b',font="TimesNewRoman 40 bold").grid(row=0,column=0, columnspan=15)

#name label
    label1 = Label(frame1,text="NAME", width=20,bg="#c590ff",fg='#0e005b',font="TimesNewRoman 14 bold").grid(row=1, column=0,padx=20,pady=20)
    label1 = StringVar()
    namelabel= Label(frame1,text=f"{resumeName}", width=20,fg='black',font="TimesNewRoman 12").grid(row=1, column=1)
#Gender label
    label3 = Label( frame1, text= "GENDER", width=20,bg="#c590ff",fg='#0e005b',font="TimesNewRoman 14 bold")
    label3.grid(row=2,column=0,sticky='W',padx=20,pady=20)
    genderlabel = Label(frame1,text=f"{resumeGender}", width=20,fg='black',font="TimesNewRoman 12").grid(row=2, column=1)
#Email label
    label5 = Label(frame1,text="EMAIL-ID",  width=20,bg="#c590ff",fg='#0e005b',font="TimesNewRoman 14 bold").grid(row=3, column=0)
    emaillabel = Label(frame1,text=f"{resumeEmail}",  width=20,fg='black',font="TimesNewRoman 12").grid(row=3, column=1)
#bio label
    label4 = Label(frame2, text="BIO", width=20, bg="#c590ff", fg='#0e005b',font="TimesNewRoman 14 bold").grid(row=7, column=0)
    biolabel = Label(frame2, text=f"{resumeBio}", width=50, fg='black', font="TimesNewRoman 12").grid(row=7,column=1)
    biolabel = StringVar()
#DP canvas
    dp = Image.open(r"images clicked\{}.png".format(resumeImage))
    resized_img = dp.resize((200,160), Image.ANTIALIAS)
    dpfinal = ImageTk.PhotoImage(resized_img)
    dpLabel = Label(frame1,width=200, height=160,image=dpfinal)
    dpLabel.grid(row=0,column=0, columnspan=1)

    canvas1 = Canvas(frame3, width = 120, height = 110)
    canvas1.grid(row=8,column=1,padx=10)
    img = PhotoImage(file=r"linkdin.png")
    canvas1.create_image(10,10, anchor=NW, image=img)
    linkedinbtn=Button(root,text=f"LINKEDIN", height=1, width=20, bg="#c590ff", fg="black",font="TimesNewRoman 10 bold",command=openlinkedin)
    linkedinbtn.grid(row=9,column=1,padx=35)
    urllabel = Label(frame3, text=f"{resumeLinkedin}", height=1, width=20, fg='#0e005b',font="TimesNewRoman 8 bold").grid(row=10, column=1)

    canvas = Canvas(frame3, width = 120, height = 110)
    canvas.grid(row=8,column=2,padx=10)
    img1 = PhotoImage(file=r"fb.png")
    canvas.create_image(10,10, anchor=NW, image=img1)
    facebookbtn=Button(root,text=f"FACEBOOK", height=1, width=20, bg="#c590ff", fg="black",font="TimesNewRoman 10 bold",command=openfacebook)
    facebookbtn.grid(row=9,column=2,sticky='W',padx=50)
    urllabel2 = Label(frame3, text=f"{resumeFacebook}", height=1, width=20, fg='#0e005b',font="TimesNewRoman 8 bold").grid(row=10, column=2)

    canvas = Canvas(frame3, width = 120, height = 110)
    canvas.grid(row=8,column=3,padx=10)
    img3 = PhotoImage(file=r"instagram.png")
    canvas.create_image(10,10, anchor=NW, image=img3)
    instagrambtn=Button(root,text=f"INSTAGRAM", height=1, width=20, bg="#c590ff", fg="black",font="TimesNewRoman 10 bold",command=openinstagram)
    instagrambtn.grid(row=9,column=3,sticky='W',padx=55)
    urllabe3 = Label(frame3, text=f"{resumeInstagram}", height=1, width=20, fg='#0e005b',font="TimesNewRoman 8 bold").grid(row=10, column=3)

    canvas = Canvas(frame3, width = 120, height = 110)
    canvas.grid(row=12,column=1,padx=10)
    img4 = PhotoImage(file=r"spot.png")
    canvas.create_image(10,10, anchor=NW, image=img4)
    spotifybtn=Button(root,text=f"SPOTIFY", height=1, width=20, bg="#c590ff", fg="black",font="TimesNewRoman 10 bold",command=openspotify)
    spotifybtn.grid(row=13,column=1,padx=55)
    urllabel4 = Label(frame3, text=f"{resumeSpotify}", height=1, width=20,fg='#0e005b',font="TimesNewRoman 8 bold").grid(row=14, column=1)

    canvas = Canvas(frame3, width = 120, height = 110)
    canvas.grid(row=12,column=2,padx=10)
    img5 = PhotoImage(file=r"snap.png")
    canvas.create_image(20,30, anchor=NW, image=img5)
    snapchatbtn=Button(root,text=f"SNAPCHAT", height=1, width=20, bg="#c590ff", fg="black",font="TimesNewRoman 10 bold",command=opensnapchat)
    snapchatbtn.grid(row=13,column=2,sticky='W',padx=55)
    urllabel5 = Label(frame3, text=f"{resumeSpotify}", height=1, width=20, fg='#0e005b',font="TimesNewRoman 8 bold").grid(row=14, column=2)

    canvas = Canvas(frame3, width = 120, height = 110)
    canvas.grid(row=12,column=3,padx=10)
    img6 = PhotoImage(file=r"twitter.png")
    canvas.create_image(10,10, anchor=NW, image=img6)
    twitterbtn = Button(root,text=f"TWITTER", height=1, width=20, bg="#c590ff", fg="black",font="TimesNewRoman 10 bold",command=opentwitter)
    twitterbtn.grid(row=13,column=3,sticky='W',padx=55)
    urllabel4 = Label(frame3, text=f"{resumeSpotify}", height=1, width=20, fg='#0e005b',font="TimesNewRoman 8 bold").grid(row=14, column=3)

#download button
    b7=Button(root,text="Go Back", height=1, width=20, bg="Beige", fg="Black",font="TimesNewRoman 15 bold",command=exitpage)
    b7.grid(row=16,column=2,pady=12)

    root.mainloop()