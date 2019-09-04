import tkinter as tk 
from tkinter import filedialog
import converter as CVT 

HEIGHT = 400
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

#frame
frameBrowse = tk.Frame(root,heigh = 15,width = 15,bg="white")
frameBrowse.place(relx = 0.4,rely=0.1,relwidth= 0.2,relheight=0.1)

frameEntry = tk.Frame(root,heigh = 10,width =350 ,bg="white")
frameEntry.place(relx = 0.1,rely=0.7,relwidth= 0.8,relheight=0.05)

frameDetails = tk.Frame(root,height= 100,width=100,bg="blue")
frameDetails.place(relx = 0.1,rely=0.2,relwidth= 0.8,relheight=0.3)

frameCreate = tk.Frame(root,heigh = 15,width = 350,bg="white")
frameCreate.place(relx = 0.4,rely=0.79,relwidth= 0.2,relheight=0.1)

#create button
btnCreateGif = tk.Button(frameCreate,text="Create Gif",bg="white",fg="black",height="2",width="8",command= lambda : createGif(maker))
btnCreateGif.pack(fill="both",side="left",expand=1)

btnBrowseFile = tk.Button(frameBrowse,text="Browse File",bg="white",fg="black",command=openFileDialog)
btnBrowseFile.pack(fill="both",side="left",expand=1)

# btnprintMetadata = tk.Button(root,text="print Metadata",bg="white",fg="black",height="2",width="8",command= lambda : printMetaData(maker))
# btnprintMetadata.pack()

#label
labelFolder = tk.Label(frameDetails)
labelFolder.pack()

labelTargetFormat = tk.Label(root,text="Target File Format")
labelTargetFormat.place(relx = 0.1,rely=0.6,relwidth= 0.25,relheight=0.05)

'''
TO DO : add label for details(fps,duration,size,fileformat, inputpath)
'''

#entry
entryTargetFile = tk.Entry(frameEntry,width = 350,font=20)
entryTargetFile.pack(fill="both", expand=1)

#create label
root.mainloop()

