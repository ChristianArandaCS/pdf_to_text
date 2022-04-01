# This script turns all pdfs in a path into images to run through the barcode reader script

# import module
import os
import shutil
from pdf2image import convert_from_path
from os import path
from glob import glob

# tkinter libs
from tkinter import *
from tkinter import filedialog




##########################################################################

#creating main root
root = Tk()
root.title("Barcode reader")
script_path = os.path.abspath(os.curdir)


# swags up your code
# icon_replacement = PhotoImage(file="ying-yang.ico")
# root.iconphoto(False, icon_replacement)

##########################################################################



# have the code find its script path
script_path = os.path.abspath(os.curdir)

# prompts user to select pdf file
def selectingFromFolder():
    global file_name
    file_name = filedialog.askopenfilename()

    #copies file into script path
    shutil.copyfile(file_name, script_path)






def conver_from_pdf_to_jpg(file_name):

    images = convert_from_path(file_name)
 
    for i in range(len(images)):
        img_path = (script_path + "/imgs/")
        # Save pages as images in the pdf and renames them
        images[i].save(img_path + 'page'+ str(i) +'.jpg', 'JPEG')

        # moves images into isolated folder


############################################################################################

def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))



## gets all dir and sub dir file names
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles








##########################################################################
#creating GUI widgets
scriptDescript = Label(root, text="This script reads all images in a folder \n for barcodes and outputs them in a specified folder")
label_1 = Label(root, text="Folder: ", padx=10, pady=15)
folderSelect = Button(root, text="Select", width=10, borderwidth=3, command=selectingFromFolder)
runScript = Button(root, text="Run script", width=10, borderwidth=3, command=conver_from_pdf_to_jpg)

scriptDescript.grid(row=0, column=0, columnspan=2)
label_1.grid(row=1, column=0)
folderSelect.grid(row=1, column=1)
runScript.grid(row=2, column=1)


##########################################################################
root.mainloop()

quit()

### A DECISION FOR SOMETING IS A DECISION AGAINST SOMETHING ELSE
### 4.669