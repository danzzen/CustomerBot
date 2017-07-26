import pickle
from sklearn.externals import joblib
clf=joblib.load("classifier.pkl")
whWords={'who','whom','what','why','how','whose','when','which','why don\'t','how long','how many','how much','which'}
hVerbs={'is','am','are','was','were','will','shall','should','can','could','has','have','had','did','do','does','didn\'t','don\'t','doesn\'t'}
moodh={'please','happy','good','excellent','nice','cool','like it','amazing','outstanding','should','may'}
mooodb={'fucked up','disappointed','bad','why not','don\'t like','didn\'t like','not good','not cool'}
def checkQues(str):
    arr=str.split(' ')
    isques0,isques1,isques2,isfeedback,moodhp,moodbd=0,0,0,0,0,0
    f=arr[0].lower()
    if f  in whWords:
        isques0=1
    else:
        if f in hVerbs:
            isques1=1
        else:
            if(arr[len(arr)-1]=='?'):
                isques2=1
    if isques2==1 or isques1==1 or isques0==1:
        isfeedback=0
    else:
        isfeedback=10
    for l in str:
        if l in moodh:
            moodhp=500
        if l in mooodb:
            moodbd=1000
    result=clf.predict([max(moodbd,moodhp),max(isques0,isques2,isques1),isfeedback])

    return result
# checkQues("what a amazing product is this!!")
