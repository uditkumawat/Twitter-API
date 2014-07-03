import twitter
import json


ckey='bTt1LYXAn6SGMpBZwXlVEwbNa'
csecret='Xkns5QTECAgvYjOhHCjFCoihbiZavcrvU6sQF7U0RRHilgFbs3'
atoken='323025517-fMkCvhUt32BvCUPmr4pIoMtKyIVYCjdoyRnopKYa'
asecret='fnoOVQ5tcufBTK40p5o5tFnIaFnsBDT7qlMylKNEGvRdp'

auth=twitter.oauth.OAuth(atoken,asecret,ckey,csecret)

#instance of twitter.Twitter
twitter_api=twitter.Twitter(auth=auth)

q='India'

count=100

search_results=twitter_api.search.tweets(q=q,count=count)


for i in range(len(search_results)):
    print i+1
    print 'Text ',search_results['statuses'][i]['text']
    print 'Favourite Count ',search_results['statuses'][i]['favorite_count']
    print 'Screen Name ',search_results['statuses'][i]['entities']['user_mentions'][i]['screen_name']
    
