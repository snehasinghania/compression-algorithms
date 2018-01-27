ptr = open("infile.txt","r")
s  = ptr.read()
s = s[:-1]

fptr = open("binary_file.txt","r")
w  = fptr.read()
w = w[:-1]

comp_ratio = (7.0*len(s))/(float)(len(w))

print comp_ratio
