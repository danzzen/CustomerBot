
import json
with open('dev-v1.1.json') as f:
    data = json.load(f)
import pickle
d = data['data']


dict={}

count=0

for p in d:
    r=p['paragraphs']
    for i in r:
        tt=i['qas']
        for j in tt:
            feed=j["answers"][0]["text"]
            ques=j["question"]
            feedarray= {}
            quesarray = {}
            feedarray['dd'] = feed
            feedarray['isques'] = '0'
            feedarray['isfeed']='10'
            dict[count]=feedarray
            quesarray['dd'] = ques
            quesarray['isques'] = '1'
            quesarray['isfeed'] = '0'
            count+=1
            dict[count] = quesarray
            count += 1

output=open('data_pickle.pkl','wb')
pickle.dump(dict,output)
output.close()


