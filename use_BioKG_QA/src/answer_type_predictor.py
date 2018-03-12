import nltk
import json
import re
import numpy as np
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords # Import the stop word list
from nltk.stem.wordnet import WordNetLemmatizer
import question_feature_generator
from question_feature_generator import question_features
import do_4b_Trainset_Anotation
from do_4b_Trainset_Anotation import do_annotatiom_for_training_questions
import sklearn_svm_classifier
from sklearn_svm_classifier import predict_class_number


def predict_answer_type(q):
    class_numer_list = ['other', 'chemical', 'choice', 'disease', 'drug', 'enzyme', 'function', 'gene', 'inheritance', 'location', 'mutation', 'cell', 'number', 'protein', 'receptor', 'symptom', 'biomedical_techniques', 'computational_methods_tools', 'virus', 'histone_modification', 'cause', 'RNA', 'target', 'family', 'definition', 'bacterium', 'database', 'component', 'trial', 'test', 'application', 'judgement', 'sequence', 'enzymatic_activity', 'hormone', 'tissue', 'tumor', 'relationship', 'side_effect', 'species']
    features = question_features(q)
    do_annotatiom_for_training_questions()
    class_numer = predict_class_number()
    answer_type = class_numer_list[int(class_numer)]
    print ('the question type of ' + q + ' is ' + answer_type )



    #answer_type = 1

    return answer_type

def judge_answer_type_by_rule(q):
    lmtzr = WordNetLemmatizer()
    raw_question_words = re.split(r'[ "\t\n\?\.]+',q)
    lemma_question_words = []
    rule_type_number = 0 #the answer type number judged by rules
    for i in range(0,len(raw_question_words)):
        word = lmtzr.lemmatize(raw_question_words[i])
        print(word)
        lemma_question_words.append(word)

    if(lemma_question_words[0]=='Which'):
        if(lemma_question_words[1]=='disease'):
            rule_type_number = 3
        elif(lemma_question_words[1]=='gene'):
            rule_type_number = 7

    return rule_type_number


if __name__ == "__main__":
    question = "Which genes can be treated with Delamanid?"  # What disease is the drug aducanumab targeting？Which disease can be treated with Delamanid?
    print(judge_answer_type_by_rule(question))
    #answer_question(question)



