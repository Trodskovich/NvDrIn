# -----------------------------------------------------------------------------------------------------------------------------
# NvDrIN v1=0.1
# dpndchk
# Dependency Checker
# To check for Necessary Dependencies before  Install Commands-Install Nvidia Driver (The Hard Way).
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



print(blkColors.Blue + "\ncheck for Necessary Dependencies...\n" + blkColors.EndC)
subprocess.call(["sudo zypper in -t pattern devel_C_C++ devel_kernel"], shell=True)
print(blkColors.Blue + "\nDependency Check Complete.\n" + blkColors.EndC)
