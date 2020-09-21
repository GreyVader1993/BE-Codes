#Function to get 2's complement form of the input number
def make_negative(b):
	a = list(b)
	a.reverse()

	invert = False
	
	for i in range(len(a)):
		if invert == True:
			a[i] = int(not a[i])
		elif a[i] == 1:
			invert = True
			
	a.reverse()
	return a
	
#Function to convert multiplier and multiplicand
def convert_to_binary(a):
        negative = False
        if(a < 0):
                a *= -1
                negative = True

        binary = []
        
        while(a >= 1):
                binary.append(a%2)
                a /= 2
                
        binary.reverse()
        if(negative):
                binary = make_negative(binary)

        print binary
        return binary #Returns reverse of the list

#Function to +/- multiplicand to multiplier
#def addsubtract(a, b):
        

#Function to perform booths multiplication
def booths(a, b, minus_a):
	#a multiplicand, b multiplier, minus_a two's complement of multiplier
	previousLSB = 0
	
	for i in range(len(a)):
		if(b[-1] != previousLSB):
			multiplier_part = list(b[:len(b) / 2]) #Removes first half of the multiplier for +/- of multiplicand
                        b = b[len(b)/2:] #Second part on removing the first part
                        multiplier_part.reverse()

                        if(b[-1] == 0): #Combination is 01, thus add multiplicand
                                carry = 0
                                a.reverse()
                                for i in range(len(multiplier_part)):
                                        multiplier_part[i] += a[i]
                                        if multiplier_part[i] == 2:
                                                multiplier_part[i] = 0
                                                carry = 1
                                        elif multiplier_part[i] == 3:
                                                multiplier_part[i] = 1
                                                carry = 1
                                        
                                        if carry == 1 and i+1 < len(a):
                                                multiplier_part[i+1] += carry
                                                carry = 0
                                a.reverse()
                        
			else: #Combination is 10, thus subtract multiplicand
                                carry = 0
                                minus_a.reverse()
                                for i in range(len(multiplier_part)):
                                        multiplier_part[i] += minus_a[i]
                                        if multiplier_part[i] == 2:
                                                multiplier_part[i] = 0
                                                carry = 1
                                        elif multiplier_part[i] == 3:
                                                multiplier_part[i] = 1
                                                carry = 1
                                        
                                        if carry == 1 and i+1 < len(a):
                                                multiplier_part[i+1] += carry
                                                carry = 0

                                minus_a.reverse()

                        multiplier_part.reverse()
                        b = multiplier_part + b 	


                #Code for arithmetic right shift of multiplier
                previousLSB = b[-1]
                b = b[:-1]
                b = [b[0]] + b
                
        return b

def main():
    print "Enter multiplier and multiplicand upto 16"
    a, b = map(int, raw_input().split())

    #Gets list of multiplier and multiplicand in binary
    multiplier = convert_to_binary(a)
    multiplicand = convert_to_binary(b)

    #Logic to make multiplier and multiplicand at least of length 5
    multiplier = (10 - len(multiplier)) * [0] + multiplier
    
    multiplicand = (5 - len(multiplicand)) * [0] + multiplicand
    
    minus_multiplicand = make_negative(multiplicand)
    minus_multiplier = make_negative(multiplier)

    #If either is negative, exchange original and negative values
    if(a < 0):
        multiplicand, minus_multiplicand = minus_multiplicand, multiplicand
    if(b < 0):
        multiplier, minus_multiplier = minus_multiplier, multiplier
    
    print minus_multiplicand

    print multiplicand, multiplier
    
    ans = booths(multiplicand, multiplier, minus_multiplicand)

    print ans
        
main()
