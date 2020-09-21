ref = [[0, 1], [-1, 0]]

#Function to add any input to the final summation
def add(result, adder, num_zeros):
        #print "Initial result", result
        try:
                num_zeros_before = len(result) - len(adder) - num_zeros
                adder = num_zeros_before * [adder[0]] +  adder + num_zeros * [0] #Making adder the same length as result
        except TypeError:
                print "Adder is 0"
                return result #This error occurs when the adder is 0, that is 0 is to be added

        adder.reverse()
        carry = 0
        
        for i in range(len(result)):
                result[i] += adder[i]

                if result[i] == 2:
                        result[i] = 0
                        carry = 1

                elif result[i] == 3:
                        result[i] = 1
                        carry = 1
                        
                if carry == 1 and i+1 < len(adder):
                        result[i+1] += carry
                        carry = 0

        return result

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

#Function to convert input binary list into decimal number
def convert_to_decimal(a):
        count = len(a) - 1
        ans = 0

        for digit in a:
                ans += (digit * pow(2, count))
                count -= 1

        return ans

#Function to perform booths multiplication
def booths(a, b, minus_a, minus_b):
        #a multiplicand, b multiplier, minus_a two's complement of multiplier
        b = [b[0]] + b
        b.append(0) #Changing multiplier
        
        #print b
        
        mul = []
        for i in range(len(b)):
                try:
                        mul.append(ref[b[i]][b[i+1]])
                except IndexError:
                        break
                
        print "Mul: ",mul
                
        mul.reverse() #Reversing for the multiplication
        
        toadd = [0, a, minus_a]
        
        summation = [0] * (2 * len(a))
        
        print "toadd: ", toadd
        print "summation", summation

        for i in range(len(mul)):
                print "Results for iteration: ", i
                adder = toadd[mul[i]]
                print "Adder : ", adder, i
                summation = add(summation, toadd[mul[i]], i)

        return summation
        
    
def booth_call(a, b):
        final_ans_mult = [1,-1] #Multiplier for the final answer
        print "Enter multiplicand and multiplier upto 16"
        #a,b = map(int, raw_input().split())

        #Gets list of multiplier and multiplicand in binary
        multiplicand = bin(a).split('b')[1]
        multiplier = bin(b).split('b')[1]

        length = max(len(multiplicand), len(multiplier)) + 1
        multiplicand = map(int, list((length - len(multiplicand)) * '0' + multiplicand))
        multiplier = map(int, list((length - len(multiplier)) * '0' + multiplier))
        minus_multiplicand = make_negative(multiplicand)
        minus_multiplier = make_negative(multiplier)

        if(a < 0):
            multiplicand, minus_multiplicand = minus_multiplicand, multiplicand
        if(b < 0):
            multiplier, minus_multiplier = minus_multiplier, multiplier

        print multiplicand, multiplier, minus_multiplicand, minus_multiplier

        ans = booths(multiplicand, multiplier, minus_multiplicand, minus_multiplier)
        ans.reverse()
        print ans

        answers_binary = [ans, make_negative(ans)]
        answer = final_ans_mult[ans[0]] * convert_to_decimal(answers_binary[ans[0]])

        print "Final ans", answer
        return answer
