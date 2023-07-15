import webbrowser as wb
from tkinter import * 
root=Tk(className=" Navigator_Form")

l1=Label(root,text="Username🚹: ",
        font=("Times New Roman",25))
l1.grid()

e1=Entry(root,font=("Times New Roman",25))
e1.grid()

#for password
l2=Label(root,text="Password🔑: ",
        font=("Times New Roman",25))
l2.grid()

e2=Entry(root,font=("Times New Roman",25),show="*")
e2.grid()

#function
def showhide():
    if e2["show"]=="":
        e2["show"]="*"
    else:
        e2["show"]=""
        c["text"]="Hide password"

#show pass
c=Checkbutton(root,text="Show password",
              font=("Times New Roman",10),
              command=showhide)
c.grid()

def store():
    user=e1.get()
    passwd=e2.get()
    print("UserId : ",user,"|","Password : ",passwd)

#used for padding Or applying space/gap

lspace1=Label(root,text=" ",
         font=("Times New Roman",20))
lspace1.grid()

l3=Label(root,text=" Website🌐",
         font=("Times New Roman",15))
l3.grid()

def store():
    user=e1.get()
    passwd=e2.get()
    print("UserId : ",user,"|","Password : ",passwd)
    if user=="zayed" and passwd=="1":
        f=open("GuiDataEntry.txt","+at")
        f.write(f"\nUsername: {user} \nPassword: {passwd}")
        l3["text"]="Data updated successfully!!"
    else:
        l3["text"]="Invalid username or password"
        
e=Entry(root,font=("Comic Sans MS",20))
e.grid()

def navigate():
    currentweb = webdropdownlist.get()
    if currentweb == "Google":
        wb.open("https://www.google.com/search?q=")
    elif currentweb == "Youtube":
        wb.open("https://www.youtube.com")
    elif currentweb == "Facebook":
        wb.open("https://https://www.facebook.com")
    elif currentweb == "Twitter":
        wb.open("https://www.twitter.com")
    elif currentweb == "Snapchat":
        wb.open("https://www.snapchat.com")

weboptions = ["Options For Sites","Google", "Youtube", "Facebook", "Twitter", "Snapchat"]
webdropdownlist = StringVar(root)
webdropdownlist.set(weboptions[0])
om = OptionMenu(root,webdropdownlist,*weboptions)
om.grid()
b=Button(root,text="Search",
         command=navigate,
         bg="azure3",
         activebackground="Grey",
         font=("Comic Sans MS",10,"bold"))
b.grid()

lspace2=Label(root,text=" ",
         font=("Times New Roman",20))
lspace2.grid()

def submit():
    currentSiteApp = ""
    if varinp.get() == 1:
        currentSiteApp = "Google Ads"
    elif varinp.get() == 2:
        currentSiteApp = "YouTube Ads"
    elif varinp.get() == 3:
        currentSiteApp = "Facebook Ads"
    elif varinp.get() == 3:
        currentSiteApp = "Twitter Ads"
    elif varinp.get() == 3:
        currentSiteApp = "Snapchat Ads"

    if currentSiteApp == "Google Ads":
        wb.open("https://support.pinterest.com/hc/en-us/sections/200613688-FAQ")
    elif currentSiteApp == "YouTube Ads":
        wb.open("https://support.pinterest.com/hc/en-us/sections/200613688-FAQ")
    elif currentSiteApp == "Facebook Ads":
        wb.open("https://support.pinterest.com/hc/en-us/sections/200613688-FAQ")
    elif currentSiteApp == "Twitter Ads":
        wb.open("https://support.pinterest.com/hc/en-us/sections/200613688-FAQ")
    elif currentSiteApp == "Snapchat Ads":
        wb.open("https://support.pinterest.com/hc/en-us/sections/200613688-FAQ")

lquestion = Label(root, text="From Which App or Website did you heard about Us ?",font=('',15))
lquestion.grid()

varinp = IntVar()

radioG = Radiobutton(root, text="Google Ads", variable=varinp, value=1)
radioG.grid()

radioY = Radiobutton(root, text="YouTube Ads", variable=varinp, value=2)
radioY.grid()

radioF = Radiobutton(root, text="Facebook Ads", variable=varinp, value=3)
radioF.grid()

radioT = Radiobutton(root, text="Twitter Ads", variable=varinp, value=1)
radioT.grid()

radioS = Radiobutton(root, text="Snapchat Ads", variable=varinp, value=1)
radioS.grid()

bsubmit = Button(root, text="Submit", command=submit,font=("",15,"bold"))
bsubmit.grid()

b1=Button(root,text="Close",
         command=root.destroy,
         bg="Grey",
         activebackground="black",
         font=("Comic Sans MS",15,"bold"))
b1.grid(row=20,column=1)
root.mainloop()
