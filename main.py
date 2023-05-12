#This is a comment!

#Variables
	#Syntax
		aVariable = "thing"		#String
		aVariable = 69		#Integer
		aVariable = True	#Boolean
		aVariable = {}		#List
		aVariable = anotherVariable		#The type of [anotherVariable]
	#Strings
		string1 = "aaa"
		string2 = "bbb"
		string3 = "ccc"
		integer = 1234
		
		print(string1 + string2)	#Prints aaabbb
		print(string2 + string3)	#Prints bbbccc
		print(string1 + string3)	#Prints aaaccc
		print(string1 + integer)	#RETURNS ERROR. You cannot add an integer (or any non-string type) to a string
		print(string1 + str(integer))	#Does work. See following section for explanation of str() function
		#str()
			str(1234)	#Outputs "1234"
			str(True)	#Outputs "True"
			
			alist = {}
			alist['20'] = "thing1"
			alist[20] = "thing2"
			str(alist)	#Outputs {['20', "thing1"], [20, "thing2"]} (TODO: Don't remember exact output)
			
