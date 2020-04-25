# -----------------------------------------------------------------------------------------------------------------------------
# NvDrIN v1=0.1
# PreInstall
# Check Latest Driver
# To run PreInstall Commands-Install Nvidia Driver (The Hard Way).
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

print(blkColors.Blue + "\nChanging Directory...\n" + blkColors.EndC)
subprocess.call(["cd /root/bin"], shell=True)

print(blkColors.Blue + "\nStoping  Display Manager...\n" + blkColors.EndC)
subprocess.call(["sudo rcxdm stop"], shell=True)


servicechk=subprocess.getoutput(["sudo systemctl status dkms"])
print(blkColors.Blue + servicechk + blkColors.EndC)

if ("dkms.service; enabled;" in servicechk):
    print(blkColors.Blue + "'dkms' enabled" + blkColors.EndC)
else:
    print(blkColors.Blue + "'dkms' Not enabled now enabling and starting..." + blkColors.EndC)
    subprocess.call(["sudo systemctl enable dkms"], shell=True)
    subprocess.call(["sudo systemctl start dkms"], shell=True)

print(blkColors.Blue + "\nPre-Install Script Complete...\n" + blkColors.EndC)
