# This script turns all pdfs in a path into images to run through the barcode reader script


# import module
import os
import shutil
from pdf2image import convert_from_path
from os import path
from glob import glob  

# have the code find its script path
script_path = os.path.abspath(os.curdir)


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


## main function
def main():
    
    dirName = 'Y:\Jerry Ray\Adidas labels';
    
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    
    # Print the files
    for elem in listOfFiles:
        ## start parsing all pdf files here
        if elem.endswith(".pdf"):
            i = 0
            
            # copies a files from the img source to the script path
            # for fname in img_list:
            shutil.copy2(os.path.join(elem),script_path)

            onlyPDFs.append(elem)



            
            

            print(i)

            i = i +1
            
     # turn pdf's into imgs
    images = convert_from_path(elem, 500, poppler_path=r"C:\Users\chris\OneDrive\Desktop\scipts\python\resources\poppler-22.01.0\Library\bin")
    for i, image in enumerate(images):
                print(images(i))
                base = os.path.basename(os.path.normpath(images[i]))
                fname = base +str(i)+'.jpeg'
                image.save(fname, "JPEG")


    print ("****************")
    print("First Function")
    
    # Get the list of all files in directory tree at given path
    #listOfFiles = list()
    #for (dirpath, dirnames, filenames) in os.walk(dirName):
    #    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
        
    # Print the files    
    #for elem in listOfFiles:
    #    print(elem)    
        
        
        
        
## main function call
main()


### 4669
### A DECISION FOR SOMETHING IS A DECISION AGAINST SOMETHING ELSE


 
# Store Pdf with convert_from_path function
#images = convert_from_path('example.pdf')
 
#for i in range(len(images)):
   
#      # Save pages as images in the pdf
#    images[i].save('page'+ str(i) +'.jpg', 'JPEG')