import pickle
from feature_format import featureFormat, targetFeatureSplit
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.externals import joblib

data_dict = pickle.load(open("features_pickle.pkl", "rb") )

features_list = ["label","mood","isques","isfeedback"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

train_feature,test_feature,train_label,test_label=train_test_split(features,labels,test_size=0.2,random_state=42)


clf=svm.SVC(kernel='rbf')
clf=clf.fit(train_feature,train_label)
joblib.dump(clf, 'classifier.pkl')
