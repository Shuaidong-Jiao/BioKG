#coding=utf-8
import nltk
import json
import re
import numpy as np
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords # Import the stop word list
from nltk.stem.wordnet import WordNetLemmatizer

def question_features(q):
    print('你好！')
    #print(stopwords.words("english"))
    #stops = set(stopwords.words("english"))
    #print(len(stops))
    vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
    jsf = open('BioASQ-trainingDataset4b2.json', 'r')# BioASQ-trainingDataset4b_testset3.json
    res = json.load(jsf)
    clean_train_questions = []
    lmtzr = WordNetLemmatizer()
    beginWithDoOrBeTag = np.zeros(654 + 1)
    containTokenOrTag = np.zeros(654 + 1)
    containQuantityPhrase = np.zeros(654 + 1)
    # res=json.load(open(fls, 'r'))
    number = np.zeros(654 + 1)
    num = -1
    for i in range(0, 1307):
        questionType = res['questions'][i]['type']
        if questionType == 'factoid' or questionType == 'list':
            num = num + 1
            # rawQuestionBody=res['questions'][i]['body'].split()         #对原本的问题进行分词
            rawQuestionBody = re.split(r'[ "\t\n\?\.]+', res['questions'][i]['body'])  # \?
            lemmaQuestionBody = []
            number[num] = i + 1
            answerType = 'entity'
            choiceType = False
            j = 0
            word = lmtzr.lemmatize(rawQuestionBody[j])
            if word == 'Do' or word == 'Be':
                beginWithDoOrBeTag[num] = 1 #judge whether the question begins with Do or Be
            for j in range(0, len(rawQuestionBody)):
                word = lmtzr.lemmatize(rawQuestionBody[j])
                if word == 'or':
                    containTokenOrTag[num] = 1 #judge whether the question has the token 'or'
                lemmaQuestionBody.append(word)
                # print(lemmaQuestionBody[j])
            #meaningful_words = [w for w in lemmaQuestionBody if not w in stops]
            clean_question = " ".join(lemmaQuestionBody)
            clean_train_questions.append(clean_question)
            # if questionType=='yesno':

            # print('choiceType is',choiceType)
            # print('questionType is',questionType)
            # print(res['questions'][i]['body'])
            # print(res['questions'][i]['ideal_answer'])
    # print(clean_train_questions)
    test_question_body =  re.split(r'[ "\t\n\?\.]+',q)# the question q needs to be answered
    lemma_test_question_body = []
    first_word = lmtzr.lemmatize(test_question_body[0])
    num = num + 1
    if first_word == 'Do' or first_word == 'Be':
        beginWithDoOrBeTag[num] = 1;
    k = 0
    for k in range(0, len(test_question_body)):
        question_word = lmtzr.lemmatize(test_question_body[k])
        lemma_test_question_body.append(question_word)
        if question_word == 'or':
            containTokenOrTag[num] = 1
    clean_test_question = " ".join(lemma_test_question_body)
    clean_train_questions.append(clean_test_question)


    train_vocab_dictionary = vectorizer.fit(clean_train_questions) #include train questions and test questin q
    print(train_vocab_dictionary)
    train_question_features = vectorizer.fit_transform(clean_train_questions)
    print(train_question_features.shape)
    tfidf_value = np.zeros((654 + 1, 1691))
    # train_question_features = train_question_features.toarray()train_question_features.sum(axis=i)
    wordsCountInthisQuery = np.zeros(654 + 1)
    thisWordAppearInQuerysCount = np.zeros(1691)
    for i in range(0, 654 + 1):
        wordsCountInthisQuery[i] = train_question_features[i, 0:1691].sum()
    for j in range(0, 1691):
        thisWordAppearInQuerysCount[j] = train_question_features[0:655, j].sum()#654 + 1
    for i in range(0, 654 + 1):
        for j in range(0, 1691):
            tfidf_value[i, j] = (train_question_features[i, j] / wordsCountInthisQuery[i]) * np.log(
                655 / thisWordAppearInQuerysCount[j])
    # print(train_question_features)
    # print(tfidf_value)
    f = open('features4b_basicTfidf_trainSet_Delamanid.txt', 'w+')#r+
    for i in range(0, 654):
        lineCount = 0
        s0 = str(number[i])
        f.write(s0 + ' ')
        for j in range(0, 1691):#1691,比1691少会报错，多不会报错
            if tfidf_value[i, j] != 0:
                # if lineCount<5:
                # s=str(tfidf_value[i,j])
                # n=str(j+1)
                # f.write(n+':'+s+' ')
                # f.write(str(1691+3+lineCount)+':'+s+' ')
                # else:
                s = str(tfidf_value[i, j])
                n = str(j + 1)
                f.write(n + ':' + s + ' ')
            lineCount = lineCount + 1
            # s=str(tfidf_value[i,j])
            # f.write(s+' ')
        f.write('1692:')
        s1 = str(beginWithDoOrBeTag[i])
        f.write(s1 + ' ')
        f.write('1693:')
        s2 = str(containTokenOrTag[i])
        f.write(s2 + ' ')
        if i < 653:
            f.write('\n')
    f.close()
    print("i = " + str(i))
    f1 = open('phaseB_4b_features_basicTfidf_testSet_Delamanid.txt', 'w+')#r+
    for i in range(654, 654 + 1):
        # s0=str(number[i])
        # f1.write(' 1:')
        lineCount = 0
        s0 = str(number[i])
        f1.write(s0 + ' ')
        for j in range(0, 1691):
            if tfidf_value[i, j] != 0:
                # if lineCount<5:
                # s=str(tfidf_value[i,j]*1.2)
                # n=str(j+1)
                # f1.write(n+':'+s+' ')
                # f1.write(str(1784+3+lineCount)+':'+s+' ')
                # else:
                s = str(tfidf_value[i, j])
                n = str(j + 1)
                f1.write(n + ':' + s + ' ')
            lineCount = lineCount + 1
            # s=str(tfidf_value[i,j]) if tfidf_value[i,j]!=0:
            # n=str(j+1)
            # f1.write(n+':'+s+' ')

        f1.write('1692:')
        s1 = str(beginWithDoOrBeTag[i])
        f1.write(s1 + ' ')
        f1.write('1693:')
        s2 = str(containTokenOrTag[i])
        f1.write(s2 + ' ')
        f1.write('\n')
    f1.close()
    print(tfidf_value)

    # train_question_np_features = np.array(train_question_features)
    vocab = vectorizer.get_feature_names()
    # print (vocab)
    print(train_question_features.shape)
    # dist = np.sum(train_question_features, axis=0)
    # for tag, count in zip(vocab, dist):
    # print(count, tag)
    # print(res['db']['ip'])
    # print(res['db']['port'])
    jsf.close()

#if __name__ == "__main__":
#    question = "Which disease can be treated with Delamanid?"#What disease is the drug aducanumab targeting？
#    question_features(question)