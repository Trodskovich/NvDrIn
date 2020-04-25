# -----------------------------------------------------------------------------------------------------------------------------
# NvDrIN v1=0.1
# NvDrIn
# Check Latest Driver
# To Install Nvidia Driver (The Hard Way).
# Part of NvDrIn (Nvidia Driver Installer) Project
# Authour: Trodskovich
# requires python3-newt and newt preinstalled
# Run at your own Risk
# -----------------------------------------------------------------------------------------------------------------------------

import subprocess
import dpndchk
import chkltdr
import preinstall
import nvinstall
import postinstall

#from snack import SnackScreen, GridForm, ButtonBar, Textbox, CheckboxTree, snackArgs

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
    
# Clear the screen
#subprocess.call("clear", shell=True)
print(blkColors.Blue + "\nNvidia Driver Istallation begins...\n" + blkColors.EndC)
print(blkColors.Blue + "\nGetting Necessary Parameters...\n" + blkColors.EndC)

dpndchk.chk()
preinstall.pre()
chkltdr.chk()
nvinstall.ins()
postinstall.post()


subprocess.call(["sudo "], shell=True)
print(blkColors.Blue + "\nNvidia Install Script Complete.\n" + blkColors.EndC)
