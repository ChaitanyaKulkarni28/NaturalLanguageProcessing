import sys
    
# No smoothing

def noSmoothing():

	f1 = open("Q2_noSmoothing.txt","w")
	
	f1.write("Bigram \t\t\t Probability \n")
	
	for bigram in bigrams_list:
		word1 = bigram[0]
		word2 = bigram[1]
		noSmoothing_prob[bigram] = bigram_count[bigram]/unigram_count[word1]
		#print(bigram," --> ",bigram_count[bigram]/unigram_count[word1])
		f1.write(str(bigram)+" --> "+str(noSmoothing_prob[bigram])+"\n")

	f1.close()       


# Add One smoothing

def oneSmoothing():
    
	f2 = open("Q2_oneSmoothing.txt","w")
	
	f2.write("Bigram \t\t\t cStar \t\t\t Probability \n")
	
	for bigram in bigrams_list:
		word1 = bigram[0]
		word2 = bigram[1]
		
		cStar = ((bigram_count[bigram]+1)*unigram_count[word1])/(unigram_count[word1]+len(unigram_count))
		probability = (bigram_count[bigram]+1)/(unigram_count[word1]+len(unigram_count))
		addOneSmoothing_prob[bigram] = probability
		#print(bigram, " \t\t ",cStar, " \t\t ",probability)
		f2.write(str(bigram)+ " \t\t "+ str(cStar)+ " \t\t "+ str(probability)+"\n")
        
	f2.close()

	
# Good turing smoothing
def goodTuring():
    
	f3 = open("Q2_goodTuringSmoothing.txt","w")
	
	f3.write("Bigram \t\t\t Probability \n")
	
    #Creates a dictionary to store Nc(Number of bigrams that occurs c times)
	for x,y in bigram_count.items():
		
		pair = x
		count = y
		
		if count in freq_dict:
			freq_dict[count] += 1
		else:
			freq_dict[count] = 1
			
	for x,y in bigram_count.items():
		
		val1 = y
		val2 = val1+1
		
		Nc1 = freq_dict[val1]
		
		if val2 in freq_dict:
			Nc2 = freq_dict[val2]
		else:
			Nc2 = 0
			
		cStar = (val2*Nc2)/Nc1
		pStar = cStar/len(bigram_count)
		goodTuringSmoothing_prob[x] = pStar
		#print(x,"\t\t","\t\t",pStar)
		f3.write(str(x)+" \t\t "+str(pStar)+"\n")
		
	f3.close()
	

if __name__ == "__main__":
	path1 = sys.argv[1]
	#print(path1)
	#file = open("HW2_F18_NLP6320-NLPCorpusTreebank2Parts-CorpusA-Windows.txt","r")
	
	file = open(str(path1),"r")
	
	read_file = file.read()

	array_lines = read_file.split(" . ")

	unigram_count = {}
	bigrams_list = []
	bigram_count = {}
	noSmoothing_prob = {}
	addOneSmoothing_prob = {}
	goodTuringSmoothing_prob = {}
	freq_dict = {}

	# Creates Dictionary of word and its count 
	for line in array_lines:
		words_in_line = line.split()

		for word in words_in_line:
			if word in unigram_count:
				unigram_count[word] += 1
			else:
				unigram_count[word] = 1
	
	# Creates list of bigrams from corpus
	for line in array_lines:
		words_in_line = line.split()

		for i in range(len(words_in_line)-1):
			pairs = (words_in_line[i],words_in_line[i+1])
			bigrams_list.append(pairs)

	# Dictionary of bigram and its count in particular bigrams_list
	for pair in bigrams_list:
		if pair in bigram_count:
			bigram_count[pair] += 1
		else:
			bigram_count[pair] = 1
			
	
	noSmoothing()
	oneSmoothing()
	goodTuring()
	
	line = "The Fed chairman warned that the board 's decision is bad"
	print(line)
	handW = []
	words_in_line = line.split()
	noSmoothing_prob_handW = {}
	addOneSmoothing_prob_handW = {}
	goodTuringSmoothing_prob_handW = {}

	for i in range(len(words_in_line)-1):
		pairs = (words_in_line[i],words_in_line[i+1])
		handW.append(pairs)
		
	#print(handW)

	for bigram in handW:
		word1 = bigram[0]

		if bigram in bigram_count:
			probability = bigram_count[bigram]/unigram_count[word1]
		else:
			probability = 0
			
		noSmoothing_prob_handW[bigram] = probability
		
	#print(noSmoothing_prob_handW)

	noSmoothRes = 1
	for x,y in noSmoothing_prob_handW.items():
		noSmoothRes *= y
		
	print("No smoothing probability: ",noSmoothRes)

	for bigram in handW:
		word1 = bigram[0]
		
		if bigram in bigram_count: 
			probability = (bigram_count[bigram]+1)/(unigram_count[word1]+len(unigram_count))
		else:
			probability = 1/(unigram_count[word1]+len(unigram_count))
		
		addOneSmoothing_prob_handW[bigram] = probability
		
	addOneSmoothRes = 1
	for x,y in addOneSmoothing_prob_handW.items():
		addOneSmoothRes *= y
		
	print("Add one smoothing probability: ",addOneSmoothRes)

	#for x,y in bigram_count.items():
	for bigram in handW:
		
		if bigram in bigram_count:
			val1 = bigram_count[bigram]
		else:
			val1 = 0
		val2 = val1+1

		if val1 in freq_dict:
			Nc1 = freq_dict[val1]
		else:
			Nc1 = 0

		if val2 in freq_dict:
			Nc2 = freq_dict[val2]
		else:
			Nc2 = 0

		if Nc1 != 0:
			cStar = (val2*Nc2)/Nc1
			pStar = cStar/len(bigram_count)
			goodTuringSmoothing_prob_handW[bigram] = pStar
		else:
			goodTuringSmoothing_prob_handW[bigram] = 0
			
	goodTuringSmoothRes = 1
	for x,y in goodTuringSmoothing_prob_handW.items():
		goodTuringSmoothRes *= y
		
	print("Good turing smoothing probability: ",goodTuringSmoothRes)
	
	

# Hand written 
#The Fed chairman warned that the board 's decision is bad
'''
print("The ",unigram_count['The'])
print("Fed ",unigram_count['Fed'])
print("chairman ",unigram_count['chairman'])
print("warned ",unigram_count['warned'])
print("that ",unigram_count['that'])
print("the ",unigram_count['the'])
print("board ",unigram_count['board'])
print("'s ",unigram_count['\'s'])
print("decision ",unigram_count['decision'])
print("is ",unigram_count['is'])
print("bad ",unigram_count['bad'])
'''
	

