
import pickle
data_dict = pickle.load(open("data_pickle.pkl", "rb") )
key=data_dict.keys()


whWords={'who','whom','what','why','how','whose','when','which','why don\'t','how long','how many','how much','which'}
hVerbs={'is','am','are','was','were','will','shall','should','can','could','has','have','had','did','do','does','didn\'t','don\'t','doesn\'t'}
isques0,isques1,isques2,isfeedback=0,0,0,0
moodh={'please','happy','good','excellent','nice','cool','like it','amazing','outstanding','should','may'}
mooodb={'fucked up','disappointed','bad','why not','don\'t like','didn\'t like','not good','not cool'}
features_dict={}
for i in key:
    stgr=data_dict[i]['dd']
    arr=stgr.split(' ')
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
    for l in arr:
        if l in moodh:
            moodhp=500
        if l in mooodb:
            moodbd=1000
    tmp={}
    tmp['isques']=(max(isques0,isques1,isques2))
    tmp['isfeedback']=(isfeedback)
    tmp['mood']=(max(moodbd,moodhp))
    tmp['label']=((max(isques0,isques1,isques2)+int(isfeedback)+max(moodhp,moodbd)))
    print(tmp['label'])
    features_dict[stgr]=tmp

output=open('features_pickle.pkl','wb')
pickle.dump(features_dict,output)
output.close()
