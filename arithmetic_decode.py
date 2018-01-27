from arithmetic_encode import *
from decimal import *

ptr = open("ari_encode.txt" , "r")
fptr = open("output_ari.txt" , "w")

total_size , prob , upper_val , lower_val = encode()

final_dic = {}

for key , val in lower_val.items():
	final_dic[key] = (val , 0)
	
for key , val in final_dic.items():
	final_dic[key] = (val[0] , upper_val[key])

#for key , val in final_dic.items():
#	print key , "  ",val

	
#num = ptr.readline()
#num  = Decimal(num[:-1])
#print num
flag = 0
#print "The decoded answer is"
	
#print "total_zie" , total_size
if(total_size % 2 == 0):
	flag = 0  
else:
	total_size  -= 1
	flag =  1
	
while(total_size != 0):
	num = ptr.readline()
	num  = Decimal(num[:-1])
	#print num
	#print "The decoded answer is"
	lenn = 2 
	while(lenn != 0):
		#print num
		output_char = ''
		for key ,  value in final_dic.items():
			if( value[0] <= num and value[1] > num):
				output_char = key
				break
		#print output_char,
		fptr.write(output_char)
		rangegot = (final_dic[key][1] - final_dic[key][0])
		low = Decimal(final_dic[key][0])		
		num = Decimal(num-low)/Decimal(rangegot)
		lenn -= 1
	total_size -= 2
	
if(flag == 1):
	num = ptr.readline()
	num  = Decimal(num[:-1])
	#print num
	output_char = ''
	for key ,  value in final_dic.items():
		#print value[0] ,value[1]
		if( value[0] <= num and value[1] > num):
			#print key , value 	
			output_char = key
			break
	#print output_char
	fptr.write(output_char)
