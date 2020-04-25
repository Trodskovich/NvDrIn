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

print(blkColors.Blue + "\ncheck for Installed Nvidia Graphics Card and Driver...\n" + blkColors.EndC)
subprocess.call(["sudo lspci | grep VGA"], shell=True)
subprocess.call(["sudo lscpu | grep Arch"], shell=True)


patternchk=subprocess.getoutput(["sudo zypper se  python3-newt"])
print(blkColors.Blue + patternchk + blkColors.EndC)

if ("i " in patternchk or "i+ " in patternchk ):
    print(blkColors.Blue + "'python3-newt' Installed" + blkColors.EndC)
else:
    print(blkColors.Blue + "'python3-newt' Not Installed now Installing..." + blkColors.EndC)
    subprocess.call(["sudo zypper in python3-newt"], shell=True)

patternchk=subprocess.getoutput(["sudo zypper se -t pattern devel_C_C++"])
print(blkColors.Blue + patternchk + blkColors.EndC)

if ("i " in patternchk or "i+ " in patternchk ):
    print(blkColors.Blue + "'pattern devel_C_C++' Installed" + blkColors.EndC)
else:
    print(blkColors.Blue + "'pattern devel_C_C++' Not Installed now Installing..." + blkColors.EndC)
    subprocess.call(["sudo zypper in -t pattern devel_C_C++"], shell=True)
   

patternchk=subprocess.getoutput(["sudo zypper se -t pattern devel_kernel"])
print(blkColors.Blue + patternchk + blkColors.EndC)

if ("i " in patternchk or "i+ " in patternchk ):
    print(blkColors.Blue + "'pattern devel_kernel' Installed" + blkColors.EndC)
else:
    print(blkColors.Blue + "'pattern devel_Kernel' Not Installed now Installing..." + blkColors.EndC)
    subprocess.call(["sudo zypper in -t pattern devel_kernel"], shell=True)


patternchk=subprocess.getoutput(["sudo zypper se dkms"])
print(blkColors.Blue + patternchk + blkColors.EndC)

if ("i " in patternchk or "i+ " in patternchk ):
    print(blkColors.Blue + "'dkms' Installed" + blkColors.EndC)
else:
    print(blkColors.Blue + "'dkms' Not Installed now Installing..." + blkColors.EndC)
    subprocess.call(["sudo zypper in dkms"], shell=True)


print(blkColors.Blue + "\nDependency Check Complete.\n" + blkColors.EndC)
