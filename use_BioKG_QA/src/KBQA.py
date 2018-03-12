#coding:utf-8
import sys
import nltk
import json
import re
import numpy as np
from nltk import word_tokenize
import topic_entity_recognizer
from topic_entity_recognizer import recognize_topic_entity
import answer_type_predictor
from answer_type_predictor import predict_answer_type
import retrieve_candidate_answer_from_mysql
from retrieve_candidate_answer_from_mysql import retieve_candidate_answer


def answer_question(q):
    topic_entities = recognize_topic_entity(q)# recognize topic entity in question q
    answer_type = predict_answer_type(q)# predict the answer type of question q
    print ('The topic entity is ')
    print (topic_entities)
    print('The answer type  is ')
    print(answer_type)
    results = retieve_candidate_answer(topic_entities, answer_type)
    #return results


if __name__ == "__main__":
    question = "Which disease can be treated with Delamanid?"#What disease is the drug aducanumab targeting？
    answer_question(question)


