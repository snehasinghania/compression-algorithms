ptr = open("outputf.txt", "r")
fptr = open("decoded.txt" , "w")
dic = {}

for i in range(0,128):
	dic[i] = str(chr(i))

pointer = 128

code = ptr.readline()
code = int(code[:-1])
previous_char = dic[code]
#print previous_char
fptr.write(previous_char)

counter = 1 

for code in ptr:
	counter += 1
	code = int(code[:-1])
	#print "code received " , code , " " ,
	
	if code not in dic.keys():
		rcvd = previous_char + previous_char[0]
	else:
		rcvd = dic[code]
	#print rcvd
	fptr.write(rcvd)
	dic[pointer] = previous_char + rcvd[0]
	pointer += 1
	previous_char = rcvd	
	
#print '\n'
#for key , values in dic.items():
#	print key , "  " , values, "   "
infile = open("comde.txt","w")
infile.write(str(counter))


