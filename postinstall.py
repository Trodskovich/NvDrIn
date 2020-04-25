# -----------------------------------------------------------------------------------------------------------------------------
# NvDrIN v1=0.1
# PostInstall
# Check Latest Driver
# To run Post Install Commands-Install Nvidia Driver (The Hard Way).
# Part of NvDrIn (Nvidia Driver Installer) Project
# Authour: Trodskovich
# requires python3-newt and newt preinstalled
# Run at your own Risk
# -----------------------------------------------------------------------------------------------------------------------------

import subprocess
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

def post():

    print(blkColors.Blue + "\nUpdating Initramfs, Grub and rebooting...\n" + blkColors.EndC)
    #subprocess.call(["sudo mkinitrd ; grub2-mkconfig ; reboot"], shell=True)
    print(blkColors.Blue + "\nPost Install Script Complete.\n" + blkColors.EndC)
