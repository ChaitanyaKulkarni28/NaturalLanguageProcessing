Steps to run program:

1. Bigram probabilities:

==>python Assignment2_Q2.py HW2_F18_NLP6320-NLPCorpusTreebank2Parts-CorpusA-Windows.txt

   This is basically python Assignment2_Q2.py pathToCorpus

   In the output it will show no smoothing, add one smoothing and good turing smoothing      probability for input sentence (The Fed chairman warned that the board 's decision is     bad) and will create three files in the directory from which you are running this       code. Q2_noSmoothing.txt, Q2_oneSmoothing.txt, Q2_goodTuringSmoothing.txt these are       three files with bigram probability for each model.

2. Transformation Based POS Tagging:

==>python Assignment2_Q3_Q1.py HW2_F18_NLP6320_POSTaggedTrainingSet-Windows.txt

   This is same as python Assignment2_Q3_Q1.py pathToCorpus.py

   In output it will show best two transformation rules generated for “NN” to “JJ”    and “NN” to “VB” using brills algorithm

3. Naive bayes based POS Tagging:

==>python Assignment2_Q3_Q2.py HW2_F18_NLP6320_POSTaggedTrainingSet-Windows.txt

   This is same as python Assignment2_Q3_Q2.py pathToCorpus.py

   It will create two files Q3_tag_tag_prob.txt and Q3_word_tag_prob.txt having (tag,tag)    probability and (word,tag) probability respectively.