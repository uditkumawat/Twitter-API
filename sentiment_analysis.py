import twitter
import json

ckey='bTt1LYXAn6SGMpBZwXlVEwbNa'
csecret='Xkns5QTECAgvYjOhHCjFCoihbiZavcrvU6sQF7U0RRHilgFbs3'
atoken='323025517-fMkCvhUt32BvCUPmr4pIoMtKyIVYCjdoyRnopKYa'
asecret='fnoOVQ5tcufBTK40p5o5tFnIaFnsBDT7qlMylKNEGvRdp'

auth=twitter.oauth.OAuth(atoken,asecret,ckey,csecret)

twitter_api=twitter.Twitter(auth=auth)

q="india"

count=100

search_results=twitter_api.search.tweets(q=q,count=count)

statuses=search_results['statuses']

#list of tweets

lt=[statuses[i]['text'] for i in range(len(statuses))]


#file containing sentiment score of each word
sentiment_file=open("AFINN-111.txt")
scores={}    #python dictionary

#storing all scores of words in python dictionary named "scores"
for line in sentiment_file:
    term,score=line.split("\t")
    scores[term]=int(score)



s_s=0

for l in lt:
    words=l.split(' ')
    for word in words:
        s_s=s_s+scores.get(word,0)
    print "Tweet = "+l
    print "Sentiment_score = "+str(s_s)
    s_s=0
        
    



