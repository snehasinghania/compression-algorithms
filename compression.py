first = open("comen.txt","r")
first_no = first.readline()
first_no = float(first_no[:-1])

sec = open("comde.txt","r")
sec_no = sec.readline()

sec_no = float(sec_no[:-1]) 

compression_ratio = first_no/sec_no

print "The compression ratio is defined by Number_of_characters_earlier_in_binary_form divided by Number_of_total_bits_in_encoded_from_in_binary_code"
print compression_ratio
