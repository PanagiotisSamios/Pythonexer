text = input('Wright a text ')
for chr in text:
	if chr.isalpha() == True:
		print (ord(chr) + 13,end='')
	else:
		print (chr, end='')

		
		


