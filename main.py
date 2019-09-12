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
        #labelWarning.config(text="No video files selected!!".upper(),fg="red")

def createGif(maker):
    inputPath = getInputPath()
    targetFormat = str(getTargetFormat())
    targetFormat = targetFormat.lower()

    if (inputPath == "" or inputPath == "File is not chosen !") and targetFormat == "":
        labelWarning.config(text="No video files selected and target file not set!!".upper(),fg="red")
    elif (inputPath == "" or inputPath == "File is not chosen !"):
        labelWarning.config(text="No video files selected!!".upper(),fg="red")
    elif targetFormat == "":
        labelWarning.config(text="Insert target format (only .gif support".upper(),fg="red")
    else:
        try:
            maker.convertToTargetFormat(inputPath,targetFormat)
        except FileNotFoundError:
            print("no file found!")

def getMetaDataDetails(maker):
    inputPath = getInputPath()
    if inputPath == "":
        print("No video files selected!!")
        #popup error message
    else:
        fps = maker.getFps(inputPath)
        duration = maker.getDuration(inputPath)
        sizex,sizey = maker.getSizeXY(inputPath)

    return fps,duration,sizex,sizey

def printMetaData(maker):
    try:
        fps,duration,sizex,sizey = getMetaDataDetails(maker)
        print(fps,duration,sizex,sizey)
    except UnboundLocalError:
        print("Error!!")

def getInputPath():
    path = labelFolder2.cget("text")
    return path

def getTargetFormat():
    targetFormat = entryTargetFile.get()
    return targetFormat

'''
GUI code
- canvas main frame for application 
- btn for create , load file 
- label for file path, file metadata
- entry for target file to convert 
-
'''

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

frameDetails = tk.Frame(root,height= 100,width=100, borderwidth =2)
frameDetails.place(relx = 0.1,rely=0.2,relwidth= 0.8,relheight=0.3)

frameCreate = tk.Frame(root,height = 30,width = 350,)
frameCreate.place(relx = 0.4,rely=0.79,relwidth= 0.2,relheight=0.1)

#create button
btnCreateGif = tk.Button(frameCreate,text="Create Gif",bg="white",fg="black",height="2",width="8",command= lambda : createGif(maker))
btnCreateGif.pack(fill="both",side="left",expand=1)

btnBrowseFile = tk.Button(frameBrowse,text="Browse File",bg="white",fg="black",command=openFileDialog)
btnBrowseFile.pack(fill="both",side="left",expand=1)

# btnprintMetadata = tk.Button(root,text="print Metadata",bg="white",fg="black",height="2",width="8",command= lambda : printMetaData(maker))
# btnprintMetadata.pack()

#label
labelFolder1 = tk.Label(frameDetails,text = "Folder path: ")
labelFolder1.pack(side="left",anchor="nw")

labelFolder2 = tk.Label(frameDetails,text = "")
labelFolder2.pack(side="left",anchor="nw")

labelTargetFormat = tk.Label(root,text="Target File Format")
labelTargetFormat.place(relx = 0.1,rely=0.6,relwidth= 0.25,relheight=0.05)

labelWarning = tk.Label(root,text="")
labelWarning.pack(side="bottom")

'''
TO DO : add label for details(fps,duration,size,fileformat, inputpath)
'''

#entry
entryTargetFile = tk.Entry(frameEntry,width = 350,font=20)
entryTargetFile.pack(fill="both", expand=1)

#create label
root.mainloop()

