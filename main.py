import tkinter as tk 
from tkinter import filedialog
import converter as CVT 

HEIGHT = 250
WIDTH = 400

maker = CVT.Converter()

def openFileDialog():
    filename = filedialog.askopenfile(initialdir="/",title="select a file",filetypes=[("All file","*.*")])
    
    try:
        labelFolder.config(text=filename.name)
    except:
        print("Close file dialog without choosing file!!")

def createGif(maker):
    inputPath = getInputPath()
    targetFormat = getTargetFormat()

    if inputPath == "" :
        print("No video files selected!!")
        
        if targetFormat == "":
            print("Insert target format")

    else:
        maker.convertToTargetFormat(inputPath,targetFormat)

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
    path = labelFolder.cget("text")
    print(path)
    return path

def getTargetFormat():
    targetFormat = entryTargetFile.get()
    print(targetFormat)
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
#title the window
root.title("PyMediaFileConverter")
#create canvas
canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

frameBtn = tk.Frame(root,heigh = 15,width = 350,bg="white")
frameBtn.place(relx = 0.1,rely=0.1,relwidth= 0.8,relheight=0.1,)

frameEntry = tk.Frame(root,heigh = 10,width =350 ,bg="white")
frameEntry.place(relx = 0.1,rely=0.5,relwidth= 0.8,relheight=0.05)

#create button
btnCreateGif = tk.Button(frameBtn,text="Create Gif",bg="white",fg="black",height="2",width="8",command= lambda : createGif(maker))
btnCreateGif.pack(fill="y",side="left")

btnBrowseFile = tk.Button(frameBtn,text="Browse File",bg="white",fg="black",height="2",width="8",command=openFileDialog)
btnBrowseFile.pack(fill="y",side="left",padx=1)

labelFolder = tk.Label(root)
labelFolder.pack()

labelTargetFormat = tk.Label(root,text="Target File Format")
labelTargetFormat.place(relx = 0.1,rely=0.45,relwidth= 0.25,relheight=0.05)

btnprintMetadata = tk.Button(root,text="print Metadata",bg="white",fg="black",height="2",width="8",command= lambda : printMetaData(maker))
btnprintMetadata.pack()

entryTargetFile = tk.Entry(frameEntry,width = 350)
entryTargetFile.pack()

#create label
root.mainloop()

