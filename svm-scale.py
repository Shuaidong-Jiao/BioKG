import sys
import os
os.chdir('C:\libsvm-3.21\windows')
#import myMultiBioasqTrain_tfidf_scaled_baseline_Task4b_CorrectAnonated
#from myMultiBioasqTrain_tfidf_scaled_baseline_Task4b_CorrectAnonated import svm_classifier

os.system('svm-scale -l 0 -u 1 E:\\BioKG_project_python\\src\\features4b_basicTfidf_trainSet_Delamanid_ano.txt > E:\\BioKG_project_python\\src\\features4b_basicTfidf_trainSet_Delamanid_ano_scaled.txt')
os.system('svm-scale -l 0 -u 1 E:\\BioKG_project_python\\src\\phaseB_4b_features_basicTfidf_testSet_Delamanid.txt > E:\\BioKG_project_python\\src\\phaseB_4b_features_basicTfidf_testSet_Delamanid_scaled.txt')
#svm_classifier()