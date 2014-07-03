import twitter
import json

ckey='bTt1LYXAn6SGMpBZwXlVEwbNa'
csecret='Xkns5QTECAgvYjOhHCjFCoihbiZavcrvU6sQF7U0RRHilgFbs3'
atoken='323025517-fMkCvhUt32BvCUPmr4pIoMtKyIVYCjdoyRnopKYa'
asecret='fnoOVQ5tcufBTK40p5o5tFnIaFnsBDT7qlMylKNEGvRdp'

auth=twitter.oauth.OAuth(atoken,asecret,ckey,csecret)

twitter_api=twitter.Twitter(auth=auth)

q="#india"

count=100

search_results=twitter_api.search.tweets(q=q,count=count)

#print search_results['statuses'][0]['text']     tweet founded,it is just by crawling 
#print json.dumps(search_results)

for i in range(99):
    print i+1
    print search_results['statuses'][i]['text']
    print 
