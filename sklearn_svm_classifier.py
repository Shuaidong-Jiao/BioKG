from sklearn import svm
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn import linear_model, datasets
from sklearn.datasets import load_iris
import numpy as np
from sklearn.svm import SVC
import csv
import sys
import os


def predict_class_number():
    FeatureFile = open('features4b_basicTfidf_trainSet_Delamanid_ano.txt',
                       'rt')  # features4b_basicTfidf_trainSet_ano_Corrected.txt#features_1b-4b_basicTfidf_AddPatternFeatures-scaled_ano.txt
    random_state = np.random.RandomState(13)  # 30 3 8
    totalNum = 654
    featureNumber = 1694  # 2666 ##4430 2629
    x = []
    y = np.zeros(totalNum)

    i = 0
    for line in FeatureFile:
        lineContent = line.split()
        y[i] = lineContent[0]  ##get label
        features = np.zeros(featureNumber + 1)
        for j in range(1, len(lineContent)):
            item = lineContent[j].rsplit(':')
            features[int(item[0]) - 1] = (item[1])
        # features[featureNumber] = ruleBasedLabel[i]    ##add rule-based classification label to correspond with splited-randomly testset
        print
        x.append(features)
        i = i + 1
        ##print(line)
    X_train = x
    y_train = y

    test_feature_file = open('phaseB_4b_features_basicTfidf_testSet_Delamanid.txt',
                             'rt')  # phaseB_4b_features_basicTfidf_testSet.txt#features_1b-4b_basicTfidf_AddPatternFeatures-scaled_ano.txt
    k = 0
    all_test_features = []
    for test_line in test_feature_file:
        test_line_content = test_line.split()
        test_features = np.zeros(featureNumber + 1)
        for m in range(1, len(test_line_content)):
            test_item = test_line_content[m].rsplit(':')
            test_features[int(test_item[0]) - 1] = (test_item[1])
        all_test_features.append(test_features)

    print(x)
    print(y)
    X_test = all_test_features
    y_test = [1]
    print(X_train)
    print('y_train:\n')
    print(y_train)
    clf = svm.SVC(kernel='linear', gamma=0.7, C=1.0).fit(X_train, y_train)
    y_SVM_predicted = clf.predict(X_test)
    # print (X_test.shape)
    print(X_test)
    print('y_svm_predicted is ' + str(y_SVM_predicted))
    return y_SVM_predicted[0]


