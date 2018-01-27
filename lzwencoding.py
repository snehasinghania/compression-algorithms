print "Enter the input filename"
filename = raw_input()
ptr = open(filename, "r")
fptr = open("outputf.txt" , "w")
s = ptr.read()
previous_char = ''
dic = {}
for i in range(0,128):
	dic[i] = str(chr(i))
	#print dic[i]
pointer = 128
#for key in dic:
#	print dic[key]

counter = 0 
def getKey(val):
	for key, value in dic.items():
    		if value == val:
        		return key

for new_char in s:
	counter += 1
	if(pointer < 65536):
		combo = previous_char + new_char
		if combo in dic.values():
			previous_char  = combo
		else:
			dic[pointer] = combo
			pointer += 1
			#print previous_char , "at" , getKey(previous_char) 
			fptr.write(str(getKey(previous_char)))
			fptr.write("\n")
			previous_char = new_char
	else:
		print "The dictionary size has exceed limit of 2^16"		
#print new_char , "at" , getKey(previous_char)
#fptr.write(str(getKey(previous_char)))
	
infile = open("comen.txt","w")
infile.write(str(counter))
