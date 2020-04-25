# -----------------------------------------------------------------------------------------------------------------------------
# NvDrIN v1=0.1
# chkltdr
# Check Latest Driver
# To check for latest Nvidia Driver form NVIDIA Website and Download if Latest.
# Part of NvDrIn (Nvidia Driver Installer) Project
# Authour: Trodskovich
# requires python3-newt and newt preinstalled
# Run at your own Risk
# -----------------------------------------------------------------------------------------------------------------------------


import subprocess
import os
import urllib.request
from snack import SnackScreen, GridForm, ButtonBar, Textbox, CheckboxTree,Checkbox,snackArgs



# Clear the screen
subprocess.call("clear", shell=True)
NvLtTxtURL = "http://download.nvidia.com/XFree86/Linux-x86_64/latest.txt"
NvLtDrvURL = "http://download.nvidia.com/XFree86/Linux-x86_64/"
LatestFile=""
LatestHeader=""
DownloadFlag=1
SymlinkFlag=1
path=os.getcwd()
FList=[]

# class for the colors to use in printing messages
class blkColors:
    Header = "\033[95m"
    Blue = "\033[94m"
    Green = "\033[92m"
    Warning = "\033[93m"
    Error = "\033[91m"
    EndC = "\033[0m"
    Bold = "\033[1m"
    Undeline = "\033[4m"



# to show a welcome screen
def welcome():
    global NvLtDrvURL,LatestFile,LatestHeader,DownloadFlag,SymlinkFlag
    screen = SnackScreen()
    bb = ButtonBar(screen, (("Continue", "continue"), ("Cancel", "cancel")))
    tbTittle = Textbox(
        65,
        3,
        "To check for latest Nvidia Driver form NVIDIA Website, download and optionaly create a symlink to the latest File",0,1
    )
    for File in os.listdir(path):
        if File.find('.run')>0 and os.path.isfile(path+ "/" +File):
            FList.append(File)
            FList.sort()
    FileText = urllib.request.urlopen(NvLtTxtURL).read().decode('utf-8')
    for i in range(0, len(FileText)):
        if FileText[i]==' ':
            LatestHeader=FileText[0:i]
        
    for i in range(0, len(FileText)):
        if FileText[i]=='/':
            LatestFile=FileText[i+1:len(FileText)-1]
    
    NvLtDrvURL = NvLtDrvURL + LatestHeader + "/" + LatestFile  
    
  
    tbLatestL = Textbox(
        110,
        2,
        "Latest Local Version: " + FList[-1],0,1
    ) 
    tbLatestR = Textbox(
        110,
        4,
        "Latest Remote Version: " + LatestFile + "\nLatest Driver URL: "+ NvLtDrvURL,0,1
    )
    
    if LatestFile>FList[-1]:
        cbDowload= Checkbox("Download the Latest Driver",1,)
        cbSymlink= Checkbox("Create / Update Symlink",1,)
    else:
        cbDowload= Checkbox("Download the Latest Driver",0,)
        cbSymlink= Checkbox("Create / Update Symlink",0,)

    g = GridForm(screen, "chkltdr (NvDrIn) - by Trodskovich", 1, 8)

    g.add(tbTittle, 0, 2)
    g.add(tbLatestL, 0, 3, growx=1)
    g.add(tbLatestR, 0, 4, growx=1)
    g.add(cbDowload, 0, 5, growx=1)
    g.add(cbSymlink, 0, 6, growx=1)
    g.add(bb, 0, 7, growx=1)
    result = g.runOnce()
    
    
    screen.finish()
    DownloadFlag= cbDowload.value()
    SymlinkFlag= cbSymlink.value()
    return bb.buttonPressed(result)

def process():
    global NvLtDrvURL,LatestFile,LatestHeader,DownloadFlag,SymlinkFlag
    screen = SnackScreen()
    bb = ButtonBar(screen, (("End", "end"), ))
    tbTittle = Textbox(
        65,
        3,
        "Processing Input... ",0,1
    )
    
    tbDownload = Textbox(
    65,
    3,
    " ",0,1
    )
        
    
    tbSymlink = Textbox(
    65,
    3,
    " ",0,1
    ) 
    
    g = GridForm(screen, "chkltdr (NvDrIn) - by Trodskovich", 1, 6)
    g.add(tbTittle, 0, 2)
    g.add(tbDownload, 0, 3, growx=1)
    g.add(tbSymlink, 0, 4, growx=1)
    g.add(bb, 0, 5, growx=1)
    
    if DownloadFlag:
        tbDownload.setText( "Downloading Please Wait...")
        result = g.runOnce()
        screen.finish()
        urllib.request.urlretrieve(NvLtDrvURL , "./" + LatestFile)
    else:
        tbDownload.setText("Download Skipped")
         
    if SymlinkFlag:
        subprocess.call(["ln -nfs ./" + LatestFile +" NVIDIA-Linux-x86_64-Latest.run"], shell=True)
        tbSymlink.setText("Symlink Created")   
    else:
        tbSymlink.setText("Symlink Skipped")
    result = g.runOnce()
    screen.finish()
    return bb.buttonPressed(result)
    


# to run Program
def chk():
    chkwel = welcome()
    if chkwel == "cancel":
        print(blkColors.Error + "\nNvidia Latest Driver Check Cancelled\n" +  blkColors.EndC)
        quit()
    else:
        process()
            
