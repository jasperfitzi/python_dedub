
#--------pythonscript to deduplicate images in certain directory-----------------------------------------------------------------------------------------

#--------libraries--------------------------------------------------------------------------------------------------------------------------------------

import os
import os.path
import sys
from PIL import Image
import hashlib
from itertools import chain

#--------functions-----------------------------------------------------------------------------------------------------------------------------------------

#validate directory and the containing files:
def filcheck (files):
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

	print("The inaccessible files won't be considered.")
	print("The following files will be checked:")
	for f in files:
		print(f)

	return files

#creating and saving hashes + printing for processcontrol:
def hashcreate(files):
	print("Creating hashes...")
	for f in files:
		hashedImg = hashlib.md5(Image.open(f).tobytes())
		hashedhex = hashedImg.hexdigest()
		hashes.append(hashedhex)

	return hashes

#creating Dict -> keys = files | values = hashes:
def dictcreate(files, hashes):
	for i in range(len(files)):
		if hashes[i] in hash_dict.values():
			dublist.append(files[i])
		else:
			hash_dict[files[i]] = hashes[i]

	if len(dublist) == len(files):
		print("There are no dublicates in this directory anymore.")
		reyesno = input("Do you want to restart the application to check other directories? (Y/N): ")
		if reyesno is answy:
			restart()
		if reyesno is answn:
			byebye()
	else:
		print("The following files are dublicates:")
		print(dublist)

	return hash_dict, dublist

#deleting dublicates:
def dubdelete(files):
	while True:
		yesno = input("Do you want to delete certain dublicates? (Y/N): ")
		if yesno is answn:
			byebye()
		elif yesno is answy:
			while True:
				namedelete = input("Please enter the filename of th file you want to delete: ")
				todelete = (workdir + "/" + namedelete)
				if os.path.isfile(todelete):
					print("Deleting the following file:")
					print(todelete)
					os.remove(todelete)
					dublist.remove(namedelete)
					break
				else:
					print(inputerror)
			if  len(dublist) == len(files):
				print("There are no dublicates in this directory anymore.")
				break
			else:
				dictcreate(files, hashes)

		else:
			print(inputerror)

#function bye:
def byebye():
	while True:
		dowyesno = input("Do you want to shut down the application? (Y/N): ")
		if dowyesno is answy:
			print(shutdown)
			exit(0)
		elif dowyesno is answn:
			reyesno = input("Do you want to restart the application to check other directories? (Y/N): ") 
			if reyesno is answy:
				break
			elif reyesno is answn:
				print(shutdown)
				exit(0)
	restart()

#function restart:
def restart():
	print("argv was", sys.argv)
	print("sys.executable was", sys.executable)
	print("Restarting Application...")
	os.chdir("/home/benutzer")
	os.execv(sys.executable, ['python3'] + sys.argv)

#--------main-----------------------------------------------------------------------------------------------------------------------------------

#global variables:
answy = "Y"
answn = "N"
inputerror = "Input error! Please try again: "
shutdown = f"Shuting down...\nexit(0)"

#working directory:
while True:
	workdir = input("Please enter path of the directory you want to check: ")
	isdir = os.path.isdir(workdir)
	if isdir is not True:
		print("Error: Directory doen't exist. Pleas try again: ")
	else:
		print("Opening following path: " + workdir)
		break

os.chdir(workdir)

#listing files:
files = os.listdir(workdir)
print("The following files are in the chosen directory:")
for f in files:
	print(f)

filcheck(files)

#listing hashes:
hashes = []
hashcreate(files)
print(hashes)

#hash Dict:
hash_dict = {}
dublist = []

dictcreate(files, hashes)

dubdelete(files)
