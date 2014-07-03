import twitter
import json

ckey='bTt1LYXAn6SGMpBZwXlVEwbNa'
csecret='Xkns5QTECAgvYjOhHCjFCoihbiZavcrvU6sQF7U0RRHilgFbs3'
atoken='323025517-fMkCvhUt32BvCUPmr4pIoMtKyIVYCjdoyRnopKYa'
asecret='fnoOVQ5tcufBTK40p5o5tFnIaFnsBDT7qlMylKNEGvRdp'

auth=twitter.oauth.OAuth(atoken,asecret,ckey,csecret)

twitter_api=twitter.Twitter(auth=auth)

#just enter your keyword u want to search or hashtags
q="bollywood"

count=100

search_results=twitter_api.search.tweets(q=q,count=count)

statuses=search_results['statuses']

#list of hash_Tags

#print json.dumps(statuses,indent=1)

hash_tags=[hashtag['text'] for status in statuses
                               for hashtag in status['entities']['hashtags']]

scores={}

for hash_tag in hash_tags:
    if hash_tag in scores:
        scores[hash_tag]=scores[hash_tag]+1
    else:
        scores[hash_tag]=1
        
i=0
for key,value in sorted(scores.iteritems(),key=lambda (k,v):(v,k),reverse=True):
    print str(key)+" "+str(value)
    i=i+1
    if i==10:
        break
