
import tkinter as tk 
from tkinter import filedialog
import converter as CVT 

HEIGHT = 400
WIDTH = 400

maker = CVT.Converter()

def openFileDialog():
    filename = filedialog.askopenfile(initialdir="/",title="select a file",filetypes=[("All file","*.*")])
    
    try:
        labelFolder2.config(text=filename.name)
    except:
        labelFolder2.config(text="File is not chosen !")
    
    inputPath = getInputPath()
    
    fps =0
    duration=0
    size=[0,0]

    if inputPath != "" and inputPath != "File is not chosen !":
        metadata = maker.getMetadata(inputPath)
        fps = metadata["fps"]  
        duration = metadata["duration"] 
        size = metadata["size"]

    labelFps.config(text="FPS : {} fps".format(str(fps)))
    labelDuration.config(text="Duration : {} s".format(str(duration)))
    labelResolution.config(text="Size : {} x {}".format(str(size[0]),str(size[1])))


def createGif():
    inputPath = getInputPath()
    targetFormat = str(getTargetFormat())
    targetFormat = targetFormat.lower()

    if (inputPath == "" or inputPath == "File is not chosen !") and (targetFormat == "" or targetFormat !=".gif"):
        labelWarning.config(text="No video files selected and target file not set!!".upper(),fg="red")
    elif (inputPath == "" or inputPath == "File is not chosen !"):
        labelWarning.config(text="No video files selected!!".upper(),fg="red")
    elif targetFormat == "" or targetFormat !=".gif":
        labelWarning.config(text="Insert target format (only .gif support)".upper(),fg="red")
    else:
        try:
            maker.convertToTargetFormat(inputPath,targetFormat)
            labelWarning.config(text="Done!!",fg="green")
        except:
            labelWarning.config(text="ERROR!!",fg="red")

def getInputPath():
    path = labelFolder2.cget("text")
    return path

def getTargetFormat():
    targetFormat = entryTargetFile.get()
    return targetFormat


root = tk.Tk()

#title the window and prevent max/min size
root.title("PyMediaFileConverter")
root.resizable(0,0)

#create canvas
canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

#frame
frameBrowse = tk.Frame(root,height = 15,width = 15,bg="white")
frameBrowse.place(relx = 0.4,rely=0.1,relwidth= 0.2,relheight=0.1)

frameEntry = tk.Frame(root,height = 10,width =350 ,bg="white")
frameEntry.place(relx = 0.1,rely=0.7,relwidth= 0.8,relheight=0.05)

#frame1 = tk.Frame(root,height= 150,width=100, borderwidth =2,bg="red")
frame1 = tk.Frame(root,height= 150,width=100, borderwidth =2)
frame1.place(relx = 0.1,rely=0.2,relwidth= 0.8,relheight=0.4)

#frame2 = tk.Frame(frame1,height= 80,width=80, borderwidth =2,bg="green")
frame2 = tk.Frame(frame1,height= 80,width=80, borderwidth =2)
frame2.place(relx = 0,rely=0.2,relwidth= 1,relheight=0.8)

#frame3 = tk.Frame(frame2,height= 60,width=60, borderwidth =2,bg="blue")
frame3 = tk.Frame(frame2,height= 60,width=60, borderwidth =2)
frame3.place(relx = 0,rely=0.2,relwidth= 1,relheight=0.8)


frameCreate = tk.Frame(root,height = 30,width = 350,)
frameCreate.place(relx = 0.4,rely=0.79,relwidth= 0.2,relheight=0.1)

#create button
btnCreateGif = tk.Button(frameCreate,text="Create Gif",bg="white",fg="black",height="2",width="8",command=createGif)
btnCreateGif.pack(fill="both",side="left",expand=1)

btnBrowseFile = tk.Button(frameBrowse,text="Browse File",bg="white",fg="black",command=openFileDialog)
btnBrowseFile.pack(fill="both",side="left",expand=1)

# btnprintMetadata = tk.Button(root,text="print Metadata",bg="white",fg="black",height="2",width="8",command= lambda : printMetaData(maker))
# btnprintMetadata.pack()

#label
labelFolder1 = tk.Label(frame1,text = "Folder path: ")
labelFolder1.pack(side="left",anchor="nw")

labelFolder2 = tk.Label(frame1,text = "")
labelFolder2.pack(side="left",anchor="nw")

labelTargetFormat = tk.Label(root,text="Target File Format")
labelTargetFormat.place(relx = 0.1,rely=0.6,relwidth= 0.25,relheight=0.05)

labelWarning = tk.Label(root,text="")
labelWarning.pack(side="bottom")

labelDetails = tk.Label(frame2,text="Details:",font=("TkDefaultFont",16,"bold"))
labelDetails.pack(side="left",anchor="nw")

labelFps = tk.Label(frame3,text="FPS :")
labelFps.grid(row=0,column=0,sticky = "w")

labelDuration = tk.Label(frame3,text="Duration :")
labelDuration.grid(row=1,column=0,sticky = "w")

labelResolution = tk.Label(frame3,text="Size :")
labelResolution.grid(row=2,column=0,sticky = "w")

#entry
entryTargetFile = tk.Entry(frameEntry,width = 350,font=20)
entryTargetFile.pack(fill="both", expand=1)

root.mainloop()

