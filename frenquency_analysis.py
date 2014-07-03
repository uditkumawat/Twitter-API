import twitter
import json
from collections import Counter

ckey='bTt1LYXAn6SGMpBZwXlVEwbNa'
csecret='Xkns5QTECAgvYjOhHCjFCoihbiZavcrvU6sQF7U0RRHilgFbs3'
atoken='323025517-fMkCvhUt32BvCUPmr4pIoMtKyIVYCjdoyRnopKYa'
asecret='fnoOVQ5tcufBTK40p5o5tFnIaFnsBDT7qlMylKNEGvRdp'

auth=twitter.oauth.OAuth(atoken,asecret,ckey,csecret)

twitter_api=twitter.Twitter(auth=auth)

q="#india"

count=100

search_results=twitter_api.search.tweets(q=q,count=count)

statuses=search_results['statuses']

#getting all status text
statuses_text=[status['text'] for status in statuses]
"""
for i in range(len(statuses_text)):
    print i+1
    print statuses_text[i]
    print
"""
#getting all screen names
screen_names=[user_mention['screen_name'] for status in statuses
                                              for user_mention in status['entities']['user_mentions']]
"""
for i in range(len(screen_names)):
    print i+1
    print screen_names[i]
    print
"""

#getting all hash tags
hash_tags=[hashtag['text'] for status in statuses
                               for hashtag in status['entities']['hashtags']]
"""
for i in range(len(hash_tags)):
    print i+1
    print hash_tags[i]
    print
"""

#getting words from tweets

words=[w for stext in statuses_text
               for w in stext.split()]
"""
for i in range(len(words)):
    print i+1
    print words[i]
    print
"""

#this function will print the most common words,screen_names and hash_tags
for item in [words,screen_names,hash_tags]:
    c=Counter(item)
    print c.most_common()[:10]   #top 10
    print












"""
for _ in range(5):
    try:
        next_results=search_results['search_metadata']['next_results']
    except:
        break

    kwargs=dict([kv.split("=") for kv in next_results[1:].split("&")])

    search_results=twitter_api.search.tweets(**kwargs)

    statuses+=search_results['statuses']

print json.dumps(statuses[0],indent=1)
"""
