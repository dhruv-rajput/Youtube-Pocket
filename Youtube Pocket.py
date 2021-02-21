from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Please enter all feilds",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!")



root = Tk()
root.title("YouTube Pocket")
root.geometry("500x700") #set window
root.columnconfigure(0,weight=1)#set all content in center.


mycolor3 = '#%02x%02x%02x' % (200,0,0)
ytdLabel = Label(root,text="YouTube Pocket",font=("Comic Sans MS",30,'bold'),pady=10,fg=mycolor3)
ytdLabel.grid()
#Ytd Link Label
ytdLabel = Label(root,text="Enter the Link to YouTube Video",font=("Comic Sans MS",15),pady=10)
ytdLabel.grid()

#Entry Box

ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=35,textvariable=ytdEntryVar,justify = CENTER,font = ('courier', 15, 'bold'),borderwidth=10,relief=FLAT)
ytdEntry.grid()


ytdError = Label(root,fg="green",font=("jost",10))
ytdError.grid()
#Asking save file label
saveLabel = Label(root,text="Choose folder to save file",font=("Comic Sans MS",15),pady=10)
saveLabel.grid()

mycolor1 = '#%02x%02x%02x' % (64, 204, 208)
mycolor2 = '#%02x%02x%02x' % (0 , 234 ,0)
saveEntry = Button(root,width=15,bg=mycolor1,fg="white",text="Choose Path",command=openLocation,bd=5,relief=FLAT,font = ('courier', 10, 'bold'))
saveEntry.grid()

locationError = Label(root,fg="red",font=("jost",10))
locationError.grid()

ytdQuality = Label(root,font=("Comic Sans MS",15),pady=10)
ytdQuality.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("Comic Sans MS",15),pady=10)
ytdQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,font=("Comic Sans MS",15,"bold"),values=choices)
ytdchoices.grid()

#donwload btn
ytdQuality = Label(root,font=("Comic Sans MS",5,"bold"))
ytdQuality.grid()
downloadbtn = Button(root,width=15,bg=mycolor2,fg="white",text="Download",command=DownloadVideo,bd=5,relief=FLAT,font = ('courier', 10, 'bold'))
downloadbtn.grid()


root.mainloop()