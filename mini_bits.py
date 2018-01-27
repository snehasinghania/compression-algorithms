from decimal import *

#lower_bound = input()
#upper_bound = input()

#lower_bound = 0.7
#upper_bound = 0.8

def dec_to_bin(num):
	string = ""
	count = 0
	while True:
		num = (num * 2)
		#print type(num) , " num " , num
		if ((float(num) != 1) and (count <= 16)): 
			temp = str(num)
			string = string + temp[0]
			#print "        " ,string
			count += 1
			if (int(temp[0]) == 1):
				num -= 1
		else:
			string = string + '1'
			return string
	
def bin_to_dec(num):
	k = 1
	newnum = Decimal(0)
	for i in range(0,len(num)):
		newnum += Decimal((1.0/2)**k) * int(num[i])	
		k += 1
		#print "dg   " , newnum
	#retnum = "0." + str(newnum)
	#newnum = float("{0:10f}".format(newnum))
	return newnum
	
def cal_min(upper_bound , lower_bound):
	min_bit_num = ""
	upper_bin = dec_to_bin(upper_bound)
	lower_bin = dec_to_bin(lower_bound)
	#print lower_bin
	#print upper_bin
	i = 0
	while (i<len(lower_bin) and i<len(upper_bin)):
		#print "he           kmnk"
		if(lower_bin[i] == '1' and upper_bin[i] == '1'):
			min_bit_num += '1'
		elif(lower_bin[i] == '0' and upper_bin[i] == '0'):			
			min_bit_num += '0'
		elif(lower_bin[i] == '0' and upper_bin[i] == '1'):
			min_bit_num += '1'
			break
		i += 1
	
	number = bin_to_dec(min_bit_num)
	#print "The minimun number with its binary represention is " , number , "  0." + min_bit_num
	#print 'The mininum bits required are ' , len(min_bit_num)

	return number, min_bit_num
	
if __name__ == "__main__":
	lower_bound = input()
	upper_bound = input()
	cal_min(upper_bound , lower_bound)	
