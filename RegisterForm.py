import sqlite3
from urllib.parse import urlparse
import urllib.request
from tkinter import *
from tkinter import messagebox
import cv2
from time import sleep
import SocialResumePage as s
import form1 as l

imgname = ''
def register_function():

    def save():
        root1 = Tk()
        root1.title('ImageCapture')
        key = cv2.waitKey(1)
        webcam = cv2.VideoCapture(0)
        sleep(2)
        def img():
            global imgname
            imgname = enter1.get()
            while True:
                try:
                    check, frame = webcam.read()
                    cv2.imshow("Capturing", frame)
                    key = cv2.waitKey(1)
                    if key == ord('s'):
                        cv2.imwrite(filename=f"images clicked\{imgname}.png", img=frame)
                        # give path to where you want to save these photos
                        webcam.release()
                        img_ = cv2.imread(f"images clicked\{imgname}.png", cv2.IMREAD_ANYCOLOR)
                        gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                        messagebox.showinfo("Infomation", "Image Saved!")
                        print("Image saved!")
                        print(imgname)
                        cv2.destroyAllWindows()
                        root1.destroy()
                        break
                    elif key == ord('q'):
                        webcam.release()
                        cv2.destroyAllWindows()
                        break
                except(cv2.error):
                    messagebox.showerror("Error","No Webcam found")
                    imgname = 'default'
                    cv2.destroyAllWindows()
                    root1.destroy()
                    break
                except(KeyboardInterrupt):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break
        thetext = Label(root1, text="Enter image name", fg="white", bg="black").grid(row=0, column=0)
        thetext1 = Label(root1, text="After clicking on Capture").grid(row=1, column=0)
        thetext2 = Label(root1, text="Press s form your keybord to click the picture").grid(row=2, column=0)
        thetext3 = Label(root1, text="Press q form your keybord to quit").grid(row=3, column=0)
        enter1 = Entry(root1, textvariable=imgname)
        enter1.grid(row=0, column=3, padx=20, pady=20)
        button1 = Button(root1, text="Capture", bg="yellow", fg="#800000", command=img).grid(row=1, column=3)
        root1.mainloop()

    def login_page():
        root.destroy()
        l.login()

    def url_converter(url1):
        URL=''
        try:
            requestUrl = urllib.request.Request(url1)
            response = urllib.request.urlopen(requestUrl)
            urlStr = urlparse(url1)
            URL = urlStr.geturl()
        except:
            URL = "No URL"
        finally:
            return URL

    def Insert_Data():
        i=1
        while i:
            name = name1.get()
            if len(name) < 3:
                messagebox.showerror("Error", 'Please Enter a Valid Name')
                raise Exception("Please Enter Valid Name")
            else:
                i=0
                if i==0:
                    break
                else:
                    continue
        username = username1.get()#####
        gender = gender1.get()#####
        bio = bio1.get("1.0","end")######
        email = email1.get()######
        if (not ("@" in email)):
            messagebox.showerror("Error", 'Please enter a Valid Mail Id')
            raise Exception("Please Enter Valid Mail Id")
        try:
            conn = sqlite3.connect('data_base1.db')
            cur = conn.cursor()
        except:
            messagebox.showerror("Error", 'No Database Created one!')
            cur.execute("CREATE TABLE user_details(Name VARCHAR(128), Username VARCHAR(128), Gender VARCHAR(128), Bio VARCHAR(128), Email VARCHAR(128), LinkedinURL VARCHAR(128),FacebookURL VARCHAR(128), InstagramURL VARCHAR(128), SpotifyURL VARCHAR(128),SnapchatURL VARCHAR(128), TwitterURL VARCHAR(128), ImageName VARCHAR(128)")
        finally:
            cur.execute(f"SELECT Email FROM user_details WHERE Email = '{email}'")
            emailvalue = cur.fetchone()
        if emailvalue is None:
            pass
        else:
            emailstr = emailvalue[0]
            if (email == emailstr):
                messagebox.showerror("Error", 'This email already exits Go Back')
                root.destroy()
                l.login()
        conn.commit()
        conn.close()
        linkedinURLlocal = linkedinURL1.get()
        linkedinURL = url_converter(linkedinURLlocal)#####
        facebookURLlocal = facebookURL1.get()
        facebookURL = url_converter(facebookURLlocal)######
        spotifyURLlocal = spotifyURL1.get()
        spotifyURL = url_converter(spotifyURLlocal)######
        instagramURLlocal = instagramURL1.get()
        instagramURL = url_converter(instagramURLlocal)######
        snapchatURLlocal = snapchatURL1.get()
        snapchatURL = url_converter(snapchatURLlocal)######
        twitterURLlocal = twitterURL1.get()
        twitterURL = url_converter(twitterURLlocal)#######
        try:
            conn = sqlite3.connect('data_base1.db')
            cur = conn.cursor()
        except:
            messagebox.showerror("Error", 'No Database created one!')
            cur.execute("CREATE TABLE user_details(Name VARCHAR(128), Username VARCHAR(128), Gender VARCHAR(128), Bio VARCHAR(128), Email VARCHAR(128), LinkedinURL VARCHAR(128),FacebookURL VARCHAR(128), InstagramURL VARCHAR(128), SpotifyURL VARCHAR(128),SnapchatURL VARCHAR(128), TwitterURL VARCHAR(128), ImageName VARCHAR(128)")
        finally:
            cur.execute('INSERT INTO user_details(Name,Username,Gender,Bio,Email,LinkedinURL,FacebookURL,InstagramURL,SpotifyURL,SnapchatURL,TwitterURL,ImageName) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
                        (name, username, gender, bio, email, linkedinURL, facebookURL, instagramURL, spotifyURL, snapchatURL,twitterURL,imgname))
            conn.commit()
            conn.close()
        root.destroy()
        s.resumepage(username)
          # select query end

    '''---------------------------------------------loginpage tkiner window starts here----------------------------------------------------'''
    root = Tk()
    root.title("Add details")
    root.geometry("940x950")
    root.config(bg='#EAE3CB')
#root.attributes('-fullscreen',True)
#frame
    f1=Frame(root).grid()
    f2=Frame(root).grid(pady=20)
    f3=Frame(root).grid(pady=20)

#data collection
    Label (f1,text="Social media is not a media.The key is to listen,engage and build relationship. ~David Alston \n To get started register yourself!", bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 16 bold").grid(row=0, columnspan=6)

#########Name
    lab = Label(f1, text="Name ", height=1, width=10,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=1,column=1,sticky='W',pady=2)
    name1 = Entry(f1)
    name1.grid(row=1,column=2,sticky='E')

######username
    lab = Label(f1, text="Username", height=1, width=10,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=2,column=1,sticky='W',pady=2)
    username1 = Entry(f1)
    username1.grid(row=2,column=2,sticky='E')

#########gender
    lab= Label(f1, text= "Gender", height=1, width=10,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=3,column=1,sticky='W',pady=2)
    gender1 = Entry(f1)
    gender1.grid(row=3,column=2,sticky='E')

######bio
    lab = Label(f1, text= "Bio", height=1, width=10,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=5,column=1,sticky='W')
    bio1 = Text(f1, bd=2,height=5,width=15,relief=RAISED)
    bio1.insert(INSERT,"Write here!")
    bio1.grid(row=5,column=2,sticky='E')

#####email
    lab = Label(f1, text="Email id", height=1, width=10,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=6,column=1,sticky='W',pady=2)
    email1 = Entry(f1)
    email1.grid(row=6,column=2,sticky='E')

######photo
    lab = Label(f1, text= "Add/Upload Photo", height=1, width=15,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=7,column=1,sticky='W',pady=2)
    upload1 = Button(f1,text='Upload Files',command=save,width=10,bg="#2F9576",fg='#63535B',font="BOLD")
    upload1.grid(row=7, column=2,sticky='E',pady=10)

#####linkedin
    canvas1 = Canvas(f2, width = 120, height = 110)
    canvas1.grid(row=8,column=1)
    img = PhotoImage(file=r"linkdin.png")
    canvas1.create_image(10,10, anchor=NW, image=img)
    lab = Label(f2, text="Enter The URL",width=35,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 8 bold")
    lab.grid(row=9,column=1,sticky='W')
    linkedinURL1 = Entry(root,width=40)
    linkedinURL1.grid(row=10,column=1,sticky='W')

######facebook
    canvas = Canvas(f2, width = 120, height = 110)
    canvas.grid(row=8,column=2)
    img1 = PhotoImage(file=r"fb.png")
    canvas.create_image(10,10, anchor=NW, image=img1)
    lab = Label(f2, text="Enter The URL", width=30,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=9,column=2,sticky='W',padx=15)
    facebookURL1 = Entry(root,width=40)
    facebookURL1.grid(row=10,column=2,sticky='w',padx=15,pady=2)

#######instagram
    canvas = Canvas(f2, width = 120, height = 110)
    canvas.grid(row=8,column=3)
    img3 = PhotoImage(file=r"instagram.png")
    canvas.create_image(10,10, anchor=NW, image=img3)
    lab = Label(f2, text="Enter The URL",width=30,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=9,column=3,sticky='W',padx=15)
    instagramURL1= Entry(root,width=40)
    instagramURL1.grid(row=10,column=3,sticky='w',padx=15,pady=2)

####spotify
    canvas = Canvas(f2, width = 120, height = 110)
    canvas.grid(row=11,column=1)
    img4 = PhotoImage(file=r"spot.png")
    canvas.create_image(10,10, anchor=NW, image=img4)
    lab = Label(f2, text="Enter The URL",width=30,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=12,column=1,sticky='W',padx=15)
    spotifyURL1 = Entry(root,width=40)
    spotifyURL1.grid(row=13,column=1,sticky='w',padx=15,pady=2)

#####snapchat
    canvas = Canvas(f2, width = 120, height = 110)
    canvas.grid(row=11,column=2)
    img5 = PhotoImage(file=r"snap.png")
    canvas.create_image(10,10, anchor=NW, image=img5)
    lab = Label(f2, text="Enter The URL", width=30,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=12,column=2,sticky='W',padx=15)
    snapchatURL1 = Entry(root,width=40)
    snapchatURL1.grid(row=13,column=2,sticky='w',padx=15,pady=2)

######twitter
    canvas = Canvas(f2, width = 120, height = 110)
    canvas.grid(row=11,column=3)
    img6 = PhotoImage(file=r"twitter.png")
    canvas.create_image(10,10, anchor=NW, image=img6)
    lab = Label(f2, text="Enter The URL", width=30,bg="#ACD7C6",fg='#63535B',font="TimesNewRoman 10 bold")
    lab.grid(row=12,column=3,sticky='W',padx=15)
    twitterURL1 = Entry(root,width=40)
    twitterURL1.grid(row=13,column=3,sticky='w',padx=15,pady=2)

#######button to go back to loginpage
    backbtn=Button(f3,text="Back", width=5, bg="#2F9576", fg="#63535B",font="TimesNewRoman 10 bold",command=login_page)
    backbtn.grid(row=14,column=0)
########button  to save details and go to resumepage
    registerbtn=Button(f3,text="Register",width=5, bg="#2F9576", fg="#63535B",font="TimesNewRoman 10 bold",command=Insert_Data)
    registerbtn.grid(row=14,column=4,pady=10)

    root.mainloop()
'''---------------------------------------------loginpage tkiner window ends here----------------------------------------------------'''