import os

class KeyContainer:
    def __init__(self,string):
        self.string = string

cwdir = os.getcwd() #Current Working Directory
characters = " abcdefghijklmnopqrstuvwxyz" #character string 0-26 (input)
keysentence = KeyContainer("") #output
keylist = [] #converting number string into list

#options
wsci = " " #whitespace character input. Only applies to number to letter.
wsco = " " #whitespace character output. Only applies to letter to number.
cpl = 100 #characeters per line. Amount of characters before a new line is created in file. Recommended max values: Mobile = 30, Laptop = 100, Desktop = 200. Only applies to file modes.
#osc = False #output special characters? Characters that cannot be processed. REMOVED because of inconvenience.

#functions
def NumberToLetter(userinput):
	i = 0
	ii = 0
	lastkey = ""
	lastkeyError = False
	for keyletter in userinput: #input string to list
		if keyletter == wsci:
			if keyletter == lastkey or i == 0 or lastkeyError == True: #skipping a list entry causes issues.
				lastkeyError = False
			else:
				ii += 1
		else:
			pass
			try:
				keylist[ii] = (keylist[ii]*10) + int(keyletter)
				lastkeyError = False
			except:
				try:
					keylist.insert(ii, int(keyletter))
					lastkeyError = False
				except:
					if not keyletter == "\n":
						print("Error: " + "\"" + str(keyletter) + "\"" + " is not a number")
						lastkeyError = True
		lastkey = keyletter
		i += 1
	for keyletter in keylist: #list to output string
		try:
			keysentence.string += characters[keyletter]
		except:
			print("Error: " + str(keyletter) + " is out of range 0-26")
	keylist.clear()
def LetterToNumber(userinput):
	for keyletter in userinput.lower():
		i = 0
		while True:
			if keyletter == characters[i]:
				keysentence.string += (wsco + str(i))
				break
			i += 1
			if i > 26:
				if not keyletter == "\n":
					print("Error: " + "\"" + str(keyletter) + "\"" + " is not a letter")
				break
#start
while True:
	mode = input("\n1: Enter number to letter\n2: Enter letter to number\n3: File number to letter\n4: File letter to number\n5: Options\nSelection: ")
	
	while mode == "1": #enter number to letter
		print(keysentence.string)
		userinput = input("Enter a number: ")
		NumberToLetter(userinput)
	while mode == "2": #enter letter to number
		print(keysentence.string)
		userinput = str(input("Enter letter(s): "))
		LetterToNumber(userinput)
	while mode == "3": #file number to letter
		print("Current working directory: " + cwdir)
		userinput = input("\nEnter filename for number input, or enter \"dir\" to change directory\n")
		if userinput == "dir" or userinput == "\"dir\"":
			cwdir = input("Enter directory:\n")
		else:
			try:
				fileinput = open(cwdir + "/" + userinput, "rt")
				while True:
					print("Current working directory: " + cwdir)
					userinput = input("\nEnter filename for letter output, or enter \"dir\" to change directory\n")
					if userinput == "dir" or userinput == "\"dir\"":
						cwdir = input("Enter directory:\n")
					else:
						try:
							try:
								os.makedirs(cwdir)
								print("Creating directory")
							except:
								print("Not creating directory. Directory already exists or permissions denied.")
							fileoutput = open(cwdir + "/" + userinput, "wt")
							userinput = str(fileinput.read())
							NumberToLetter(userinput)
							i = 0
							for keyletter in keysentence.string:
								if i >= cpl and keyletter == wsco:
									fileoutput.write("\n")
									i = 0
								fileoutput.write(str(keyletter))
								i += 1
							fileoutput.close()
							fileinput.close()
							print("\nOperation complete\n")
							break
						except:
							print("Failed to create or open file")
							continue
			except:
				print("Error: file does not exist")
				continue
	while mode == "4": #file letter to number
		print("Current working directory: " + cwdir)
		userinput = input("\nEnter filename for letter input, or enter \"dir\" to change directory\n")
		if userinput == "dir" or userinput == "\"dir\"":
			cwdir = input("Enter directory:\n")
		else:
			try:
				fileinput = open(cwdir + "/" + userinput, "rt")
				while True:
					print("Current working directory: " + cwdir)
					userinput = input("\nEnter filename for number output, or enter \"dir\" to change directory\n")
					if userinput == "dir" or userinput == "\"dir\"":
						cwdir = input("Enter directory:\n")
					else:
						try:
							try:
								os.makedirs(cwdir)
								print("Creating directory")
							except:
								print("Not creating directory. Directory already exists or permissions denied.")
							fileoutput = open(cwdir + "/" + userinput, "wt")
							userinput = str(fileinput.read())
							LetterToNumber(userinput)
							i = 0
							for keyletter in keysentence.string:
								if i >= cpl and keyletter == wsco:
									fileoutput.write("\n")
									i = 0
								fileoutput.write(str(keyletter))
								i += 1
							fileoutput.close()
							fileinput.close()
							print("\nOperation complete\n")
							break
						except:
							print("Failed to create or open file")
							continue
			except:
				print("Error: file does not exist")
				continue
	while mode == "5": #options
		print("0: Back to menu")
		print("1: Input whitespace character: \"" + wsci + "\"")
		print("2: Output whitespace character: \"" + wsco + "\"")
		print("3: Characters per line: \"" + str(cpl) + "\"")
		userinput = input("Selection: ")
		if userinput == "0":
			break
		if userinput == "1":
			userinput = input("Input whitespace character:\n")
			wsci = str(userinput)
		if userinput == "2":
			userinput = input("Output whitespace character:\n")
			wsco = str(userinput)
		if userinput == "3":
			userinput = input("Recommended: Mobile = 20, Desktop = 100\nCharacters per line:\n")
			try:
				cpl = int(userinput)
			except:
				print("Error: input is not an integer")