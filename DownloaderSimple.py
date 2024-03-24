# YouTube Simple Downloader

# importing libraries
from tkinter import *
from pytube import YouTube

# creating a window
root = Tk()
root.geometry('800x300')
root.resizable(0,0)
root.title('YouTube Video Downloader. Karolina Koval, 2023')

#app name
Label(root, text = 'Youtube Video Downloader by Karolina Koval, 2023', font ='arial 20 bold').pack()

# field to enter a link
link = StringVar()

# download function
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()