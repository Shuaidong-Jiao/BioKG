#coding=utf-8
import nltk
import json
import re
import numpy as np
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords # Import the stop word list
from nltk.stem.wordnet import WordNetLemmatizer
import KBQA
from KBQA import answer_question

def answer_questions_json():
    print('你好！')
    #print(stopwords.words("english"))
    #stops = set(stopwords.words("english"))
    #print(len(stops))
    #vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
    jsf = open('BioASQ-task6bPhaseB-testset1.json', 'r')# BioASQ-trainingDataset4b_testset3.json BioASQ-task5bPhaseB-testset4
    res = json.load(jsf)

    for i in range(0, 100):#100 97
        questionType = res['questions'][i]['type']
        if questionType == 'factoid' or questionType == 'list':
            exact_answer_raw = answer_question(res['questions'][i]['body'])
            exact_answer_formal = []
            j = 0
            for j in range(0, len(exact_answer_raw)):  # adjust the formal of exact_answer
                temp = []
                temp.append(exact_answer_raw[j])
                exact_answer_formal.append(temp)
            if j == 0:
                exact_answer_formal = [[]]

            res['questions'][i]['exact_answer'] = exact_answer_formal
    with open ('BioASQ-task6bPhaseB-testset1-BioKG.json','w') as fw:
        json.dump(res,fw)

if __name__ == "__main__":
    #question = "Which disease can be treated with Delamanid?"#What disease is the drug aducanumab targeting？
    answer_questions_json()