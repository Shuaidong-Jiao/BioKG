#coding:utf-8
import nltk
import json
import re
import numpy as np
import urllib
import http


from nltk import word_tokenize

def recognize_topic_entity(q):
    #post_data = urllib.urlencode(q)
    concept_list = []
    conventional_concept_list = ['TARGET','TARGETS','DISEASE','DISEASES','DRUG','TREATED WITH', 'TREATED', 'DRUGS','ENZYME','ENZYMES','GENE','GENES','LOCATION','LOCATIONS','MUTATION','MUTATIONS','PROTEIN','PROTEINS','RECEPTOR','RECEPTORS','SYMPTOM','SYMPTOMS','FAMILY','FAMILIES']
    quoted_question = urllib.parse.quote(q)
    url = "http://data.bioontology.org/annotator?text=%s" % quoted_question  #Annotator website
    req = urllib.request.Request(url)
    req.add_header("Authorization", "apikey token=a7480201-153b-4dd9-9d39-8a94fa30ce61")
    respJSONcontent = ""
    i = 0
    j = 0

    try:
        resp = urllib.request.urlopen(req)
        respJSON = ""
        while  True:
            try:
                respJSONpart = resp.read()
            except http.IncompleteRead as icread:
                respJSON = respJSON + icread.partial.decode('utf-8')
                continue
            else:
                respJSON = respJSON + respJSONpart.decode('utf-8')
                break
        respJSONcontent = json.loads(respJSON)
    except Exception as RESTex:
        print("Exception occurred making REST call: " + RESTex.__str__())


    print(respJSONcontent)
    print(len(respJSONcontent))
    for i in range(0, len(respJSONcontent)):
        respJSONannoatation = respJSONcontent[i]['annotations']
        respConcept = respJSONannoatation[0]['text']
        if (respConcept not in concept_list) and (respConcept not in conventional_concept_list):
            concept_list.append(respConcept)
    #print('concept is ' )
    print('concept_list length is '+str(len(concept_list)))
    for j in range(0, len(concept_list)):
        print(concept_list[j])

    return concept_list

if __name__ == "__main__":
    question = "Please list 3 diseases associated with the PIEZO2 gene."#What disease is the drug aducanumab targeting？Which enzyme is inhibited by niraparib?Which disease can be treated with Delamanid? What disease is the drug aducanumab targeting？What is the target of daratumumab?
    recognize_topic_entity(question)