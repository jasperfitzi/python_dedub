
#--------pythonscript to deduplicate images in certain directory-----------------------------------------------------------------------------------------

#--------libraries--------------------------------------------------------------------------------------------------------------------------------------

import os
from PIL import Image
import hashlib
from itertools import chain

#--------functions-----------------------------------------------------------------------------------------------------------------------------------------

#validate directory and the containing files:
def filcheck (files):
	print("Die Dateien werden geladen...")
	for f in files:
		path = workdir + "/" + f
		print(path)
		try:
			img = Image.open(path)
		except IOError:
			print(f + " kann nicht geoeffnet werden! Datei ist kein Bild oder beschaedigt.")
			files.remove(f)
			pass

	print("Die fehlerhaften Dateien werden nicht ueberprueft.")
	print("Nur die folgende Dateien werden ueberprueft:")
	for f in files:
		print(f)

	return files

#creating and saving hashes + printing for processcontrol:
def hashcreate(files):
	print("Hashes werden erstellt...")
	for f in files:
		hashedImg = hashlib.md5(Image.open(f).tobytes())
		hashedhex = hashedImg.hexdigest()
		hashes.append(hashedhex)

	return hashes

#creating Dict -> keys = files | values = hashes:
def dictcreate(files, hashes):
	for i in range(len(files)):
		hash_dict[files[i]] = hashes[i]

	return hash_dict

#--------main-----------------------------------------------------------------------------------------------------------------------------------

#working directory:
while True:
	workdir = input("Bitte geben Sie den Pfad zum zu ueberpruefenden Verzeichnis ein: ")
	isdir = os.path.isdir(workdir)
	if isdir is not True:
		print("Das von Ihnen gewaehlte Verzeichnis existiert nicht. Bitte versuchen Sie es erneut!")
	else:
		print("Folgender Pfad  wird geoeffnet: " + workdir)
		break

os.chdir(workdir)

#listing files:
files = os.listdir(workdir)
print("Folgende Dateien befinden sich in diesem Verzeichnis:")
for f in files:
	print(f)

filcheck(files)

#listing hashes:
hashes = []
hashcreate(files)
print(hashes)

#hash Dict:
hash_dict = {}
dictcreate(files, hashes)
print(hash_dict)

#finding dublicates:
rev_dict = {}

for key, value in hash_dict.items():
	rev_dict.setdefault(value, set()).add(key)

res = filter(lambda x: len(x) > 1, rev_dict.values())

dublist = list(res)

#listing dublicates:
for i in range(len(dublist)):
	print("Diese Dateien sind Dublikate:")
	print(dublist[i])

