
# -----------------------------------------------------------------------------------------------------------------------------
# NvDrIN v1=0.1
# NvInstall
# Check Latest Driver
# To Install Nvidia Driver (The Hard Way).
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

# Create snapshot just in case
subprocess.call(["sudo snapper create --type pre --print-number --description 'Before Nvidia Driver Install'"], shell=True)

print(blkColors.Blue + "\nChanging Directory...\n" + blkColors.EndC)
subprocess.call(["cd /root/bin"], shell=True)

print(blkColors.Blue + "\nStoping  Display Manager...\n" + blkColors.EndC)
subprocess.call(["sudo rcxdm stop"], shell=True)

print(blkColors.Blue + "\nRe-Installing Nvidia Driver...\n" + blkColors.EndC)
subprocess.call(["sudo NVIDIA-Linux-x86_64-Latest.run -Xq --dkms --ui=none"], shell=True)

print(blkColors.Blue + "\nInstalling Nvidia Drivern Complete.\n" + blkColors.EndC)
