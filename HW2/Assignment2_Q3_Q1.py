import sys
from collections import Counter
#file = open("E:\\Spring 2019\\NLP\\Assignment\\hw2\\HW2_F18_NLP6320_POSTaggedTrainingSet-Windows.txt")

path1 = sys.argv[1]

file = open(str(path1),"r")

read_file = file.read()


words = []
tags = []
lines = read_file.split("\n")

for line in lines:
    for word in line.split():
        wtag = word.split("_")
        words.append(wtag[0])
        tags.append(wtag[1])
        
unique_tags = set(tags)


# Creates dictionary with word as key and all tags occured with it as list of tags as values

word_allTags = {}

for i in range(len(words)):
    if words[i] not in word_allTags:
        word_allTags[words[i]] = [tags[i]]
    else:
        word_allTags[words[i]].append(tags[i])
    

word_mostCommonTag = {}

for x,y in word_allTags.items():
    counter = Counter(y)
    mostOccuringTag = counter.most_common()[0]    # [0] So that we get just the most common tag and not its count
    word_mostCommonTag[x] = mostOccuringTag[0]
    
#print(word_mostCommonTag)


updatedTags = []

for word in words:
    updatedTags.append(word_mostCommonTag[word])


def brillsRuleGenerator(rulesFor = []):
    brillsRules = {}
    tpl = []
    allR = []
    bestScore = 0

    for fromTag in rulesFor:
        for toTag in rulesFor:

            ruleDictionary = {}
            best_val = 0
            
            if fromTag == toTag:
                continue

            for pos in range(1,len(updatedTags)):
                if tags[pos] == toTag and updatedTags[pos] == fromTag:
                    rule = (updatedTags[pos-1],fromTag,toTag)
                    if rule in ruleDictionary:
                        ruleDictionary[rule] += 1
                    else:
                        ruleDictionary[rule] = 1
                elif tags[pos] == fromTag and updatedTags[pos] == fromTag:
                    rule = (updatedTags[pos-1],fromTag,toTag)
                    if rule in ruleDictionary:
                        ruleDictionary[rule] -= 1
                    else:
                        ruleDictionary[rule] = -1
            
            for rul,val in ruleDictionary.items():
                if rul in brillsRules:
                    if val > brillsRules[rul]:
                        brillsRules[rul] = val
                else:
                    brillsRules[rul] = val
                    
                if val > 0:
                    best_val = val
                    best_z = rul[0]
                    tpl.append((rul,val))
                    
            #for rul,val in ruleDictionary.items():
                #if rul[0] == best_z and val > bestScore:
                    #bestScore = val
                    #bestRule = rul
                    
    return tpl,brillsRules


rulesfor = ['NN','JJ','VB']
bestR = brillsRuleGenerator(rulesfor)

print("\nMost common tag for standard: ",word_mostCommonTag['standard'])
print("Most common tag for work: ",word_mostCommonTag['work'])

f1 = False
f2 = False

print("\nBest Rules Generated: ")

rules_sorted = sorted(bestR[1].items(), key=lambda x: x[1], reverse=True) 
print ("\nFROM \t\t TO \t\t IF(PREV_TAG=) \t COUNT")

for i in range(len(rules_sorted)):

	if f1 and f2:
		break
		
	if rules_sorted[i][0][1] == "NN" and rules_sorted[i][0][2] == "VB" and not f1:
		print(rules_sorted[i][0][1] , "\t\t" , rules_sorted[i][0][2] ,"\t\t", rules_sorted[i][0][0],"\t\t",rules_sorted[i][1] , "\n" )
		f1 = True

	if  rules_sorted[i][0][1] == "NN" and rules_sorted[i][0][2] == "JJ" and not f2: 
		print(rules_sorted[i][0][1] , "\t\t" , rules_sorted[i][0][2] ,"\t\t", rules_sorted[i][0][0],"\t\t",rules_sorted[i][1] , "\n" )
		f2 = True