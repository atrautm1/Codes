#!//anaconda/bin/python3
#File permission reminder tool

permission = {
	'0' : "Nonexecutable, writable, or readable",
	'1' : "Execute",
	'2' : "Write",
	'3' : "Execute and Write",
	'4' : "Read",
	'5' : "Read and Execute",
	'6' : "Read and Write",
	'7' : "Read, Write, and Execute"
}

xyz = str(input("Input a 3 digit code: "))

print("User permissions: " + permission[xyz[0]])
print ("Group permissions: " + permission[xyz[1]])
print("Other permissions: " + permission[xyz[2]])
