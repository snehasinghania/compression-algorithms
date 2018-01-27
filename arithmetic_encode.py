from mini_bits import *
from decimal import *

def convert(num):
	if(len(num) < 16):
		size = 16 - len(num)
		num = num + "0"*size
	return num

def encode():
	
	fptr = open("ari_encode.txt", "w")
	ff = open("binary_file.txt" , "w")
	print "enter the file name for input"
	filename = raw_input()
	ptr = open(filename, "r")
	s = ptr.read()

	#ptr.close()
	dic = {}
	prob_dic = {}
	for i in range(0,128):
		dic[i] = str(chr(i))
		#prob_dic[str(chr(i))] = (1.0/128)

	total_size = 0 
	for new_char in s[:-1]:
		total_size += 1

	count = 0
	prob_dic = {}
	for new_char in s[:-1]:
		 prob_dic[new_char] = 0
		 count += 1

	for new_char in s[:-1]:
		 prob_dic[new_char] += 1

	for key,values in prob_dic.items():
		prob_dic[key] = Decimal(values)/Decimal(count)

	#total = 0
	#for key,values in prob_dic.items():
	#	print key , "   ",values
	#	total += values

	#print total
	
	upper_dict = {}
	lower_dict = {}

	previous_val  = 0 
	flag  = 1
	value = 0.0
	index = 0
	
	'''while index < 128:
		value = prob_dic[str(chr(index))]
		if(flag == 1):
			upper_dict[str(chr(index))] = value
			lower_dict[str(chr(index))] = 0
			flag = 0
			previous_val = value
		else:
			lower_dict[str(chr(index))] = previous_val
			upper_dict[str(chr(index))] = value + previous_val
			previous_val += value
		index += 1
		
	for key, values in lower_dict.items() :
		print key , "  " , lower_dict[key] , "  " , upper_dict[key]
'''

	for key , value in prob_dic.items():
		if(flag == 1):
			upper_dict[key] = value
			lower_dict[key] = 0
			flag = 0
			previous_val = value
		else:
			lower_dict[key] = previous_val
			upper_dict[key] = value + previous_val
			previous_val += value
	s = s[:-1]
	arr = []
	i = 0
	while(i<len(s)):
		#print arr
		if(i == (len(s)-1)):
			arr.append(s[i])
		else:
			temp = s[i] + s[i+1]
			arr.append(temp)
		i += 2
	

	#print "the total size issssssssssssssssssssssssssssss : " , total_size
	for ele in arr:
		#print ele
		low , high = 0 , 1
		for new_char in ele:
			#print 'he'
			rangegot = high - low
			high = low + rangegot*upper_dict[new_char]
			low = low + rangegot*lower_dict[new_char]

		#print "The high value is : " , high 
		#print "The low value is : ", low 

		min_num , binary_form = cal_min(high, low)
		if(len(binary_form) == 16):
			ff.write(binary_form)
		else:
			ans = convert(binary_form)
			ff.write(ans)
		#ptr = open("output.txt" , "w")
		fptr.write(str(min_num))
		fptr.write("\n")
		#print min_num

	return  total_size , prob_dic , upper_dict , lower_dict
	
	
if __name__ == "__main__":
	encode()
