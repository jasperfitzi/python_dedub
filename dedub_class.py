# --------pythonscript to deduplicate images in certain directory-----------------------------------------------------------------------------------------

# coding paradigma: object-oriented
# Version: 1.3.2
# Author: Jasper Fitzi

# --------libraries--------------------------------------------------------------------------------------------------------------------------------------

import os
import os.path
import sys
from PIL import Image
import hashlib

#---------classes------------------------------------------------------------------------------------------------------------------------------------------

class Voiders:
    def restart():
        os.chdir("/home/benutzer/python/dedub_application")
        print("argv was", sys.argv)
        print("sys.executable was", sys.executable)
        print("Restarting Application...")
        os.execv(sys.executable, ['python3'] + sys.argv)

    def byebye():
        while True:
            yesno = input("Do you want to shut down the application? (Y/N): ")
            if yesno is answy:
                print(shutdown)
                exit(0)
            elif yesno is answn:
                while True:
                    yesno = input("Do you want to restart the application to check other directories? (Y/N): ")
                    if yesno is answy:
                        break
                    elif yesno is answn:
                        print(shutdown)
                        exit(0)
                    else:
                        print(inputerror)
                break
            else:
                print(inputerror)
        Voiders.restart()

class Files:
    def __init__(self, files, hashes):
        self.files = files
        self.hashes = hashes

    def filfilter(files):
        print("Checking files.")
        for f in files:
            path = workdir + "/" + f
            name, extension = os.path.splitext(path)
            supported_ext = [".jpg", ".jpeg", ".png", ".gif", ".tiff"]
            if extension not in supported_ext:
                print("File: " + f + " is not supported and won't be checked.")
                files.remove(f)
        return files

    def filcheck(files):
        print("Loading files...")
        for f in files:
            path = workdir + "/" + f
            print(path)
            try:
                img = Image.open(path)
            except IOError:
                print("Can't open file: " + f)
                files.remove(f)
                pass
        print("The following files will be checked:")
        for f in files:
            print(f)
        return files

    def hashcreate(files, hashes):
        print("Creating hashes...")
        for f in files:
            hashedImg = hashlib.md5(Image.open(f).tobytes())
            hashedhex = hashedImg.hexdigest()
            print(f + ": " + str(hashedhex))
            hashes.append(hashedhex)
        return hashes

class Dedub:
    def __init__(self, files, hashes):
        self.files = files
        self.hashes = hashes

    def dubfinder(files, hashes):
        for i in range(len(files)):
            if hashes[i] in hash_dict.values():
                dublist.append(files[i])
            else:
                hash_dict[files[i]] = hashes[i]
        return hash_dict, dublist

    def dubdelete(files, dublist):
        while True:
            print("The following files are dublicates:")
            print(dublist)
            yesno = input("Do you want to delete certain dublicates? (Y/N): ")
            if yesno is answn:
                Voiders.byebye()
            elif yesno is answy:
                while True:
                    namedelete = input("Please enter the filename of the file you want to delete: ")
                    if namedelete in dublist:
                        todelete = (workdir + "/" + namedelete)
                        if os.path.isfile(todelete):
                            print("Deleting the following file...")
                            print(todelete)
                            os.remove(todelete)
                            dublist.remove(namedelete)
                            files.remove(namedelete)
                            break
                    else:
                        print(inputerror)
                break
            else:
                print(inputerror)

        if len(dublist) != 0:
            Dedub.dubdelete(files, dublist)
        elif len(dublist) == 0:
            print("There are no more dublicates in this directory anymore.")
            while True:
                yesno = input("Do you want to check other directories for dublicates? (Y/N): ")
                if yesno is answy or answn:
                    break
                else:
                    print(inputerror)
            if yesno is answy:
                Voiders.restart()
            elif yesno is answn:
                Voiders.byebye()
        return files, dublist

# --------main-----------------------------------------------------------------------------------------------------------------------------------

# global variables:
answy = "Y"
answn = "N"
inputerror = "Input error! Please try again: "
shutdown = f"Shuting down...\nexit(0)"

# globale lists:
files = []
hashes = []
dublist = []

# globale dictonairies:
hash_dict = {}

# working directory, cd to working directory:
while True:
    workdir = input("Please enter path of the directory you want to check: ")
    isdir = os.path.isdir(workdir)
    if isdir is not True:
        print("Error: Directory doen't exist. Pleas try again: ")
    else:
        print("Opening following path: " + workdir)
        break

os.chdir(workdir)

# listing files:
files = os.listdir(workdir)
print("The following files are in the chosen directory:")
for f in files:
    print(f)

# filtering ext, validate to open img and creating hashes:
Files.filfilter(files)
Files.filcheck(files)
Files.hashcreate(files, hashes)

# calling class Dedub to find dublicates and deleting them if wished so:
Dedub.dubfinder(files, hashes)
Dedub.dubdelete(files, dublist)
