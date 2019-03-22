import sys
#file = open("E:\\Spring 2019\\NLP\\Assignment\\hw2\\HW2_F18_NLP6320_POSTaggedTrainingSet-Windows.txt")

path1 = sys.argv[1]

file = open(str(path1),"r")

read_file = file.read()

word_tag_list = read_file.split()  #List of word_tag [w[1]_t[1], w[2]_t[2]......]

#Creates a dictionary of word_tag:count {w[1]_t[1]:count, w[2]_t[2]:count}

word_tag_count = {}

for wtag in word_tag_list:
    if wtag in word_tag_count:
        word_tag_count[wtag] += 1
    else:
        word_tag_count[wtag] = 1


#Creates a list of bigrams [(tag[1],tag[2]),(tag[2],tag[3])...]
bigrams_tag_list = []

for i in range(len(word_tag_list)-1):
    pair = (word_tag_list[i].split('_')[1],word_tag_list[i+1].split('_')[1])
    bigrams_tag_list.append(pair)

#print(('NN','NN') in bigrams_tag_list)    
#print(('TO','VBP') in bigrams_tag_list)
#print(len(bigrams_tag_list))

#Creates a dictionary with bigrams of tag as a key and its count as a value {(tag[1],tag[2]):count, (tag[2],tag[3]):count}
bigrams_tag_count = {}

for bigram in bigrams_tag_list:
    if bigram in bigrams_tag_count:
        bigrams_tag_count[bigram] += 1
    else:
        bigrams_tag_count[bigram] = 1

#Calculates count of pair (word,tag) like {(word,tag):count, (otherword,tag):count} and occurence of each unique tag

word_tag_pair_count = {}
tag_count = {}

for word_tag in word_tag_list:
    temp = word_tag.split("_")
    pair = (temp[0],temp[1])
    
    if pair in word_tag_pair_count:
        word_tag_pair_count[pair] += 1
    else:
        word_tag_pair_count[pair] = 1
        
    if temp[1] in tag_count:
        tag_count[temp[1]] += 1
    else:
        tag_count[temp[1]] = 1

#Calculates probability of word given a tag {(word,tag):prob}

word_tag_prob = {}

f1 = open("Q3_word_tag_prob.txt","w")

for word_tag,count in word_tag_pair_count.items():
    tag = word_tag[1]
    count_of_tag = tag_count[tag]
    prob = count/count_of_tag                  # Count of (word,tag) / Count of tag
    word_tag_prob[word_tag] = prob
    f1.write(str(word_tag)+"\t\t\t"+str(prob)+"\n")
	
f1.close()
	
#Calculates probability of tag given a previous tag

tag_tag_prob = {}

f2 = open("Q3_tag_tag_prob.txt","w")

for tg1_tg2,count in bigrams_tag_count.items():
	count_tg1 = tag_count[tg1_tg2[0]]
	prob = count/count_tg1                    # Count of (tag1,tag2) / Count of tag1
	tag_tag_prob[tg1_tg2] = prob
	f2.write(str(tg1_tg2)+"\t\t\t"+str(prob)+"\n")
    
f2.close()

for w,c in word_tag_prob.items():
    if w[0] == "standard" or w[0] == "work":
        print(w," ",c)

for t,c in tag_tag_prob.items():
    if t[0] == "DT" and (t[1] == "JJ" or t[1] == "NN"):
        print(t," ",c)

for t,c in tag_tag_prob.items():
    if t[0] == "TO" and (t[1] == "VBP" or t[1] == "NN" or t[1] == "VB"):
        print(t," ",c)

