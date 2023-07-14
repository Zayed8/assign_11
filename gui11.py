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

lspace=Label(root,text=" ",
         font=("Times New Roman",30))
lspace.grid()

l3=Label(root,text=" Website🌐",
         font=("Times New Roman",15))
l3.grid()

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
         font=("Comic Sans MS",20,"bold"))
b.grid()
b1=Button(root,text="Close",
         command=root.destroy,
         bg="Grey",
         activebackground="black",
         font=("Comic Sans MS",15,"bold"))
b1.grid(row=10,column=1)
root.mainloop()