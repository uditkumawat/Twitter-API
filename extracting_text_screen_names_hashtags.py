#Extracting text,scree_names and hashtags
import twitter
import json

#make an application on twitter.com and generate key and token
#setting credentials

ckey='bTt1LYXAn6SGMpBZwXlVEwbNa'            #API key
csecret='Xkns5QTECAgvYjOhHCjFCoihbiZavcrvU6sQF7U0RRHilgFbs3'    #API sceret
atoken='323025517-fMkCvhUt32BvCUPmr4pIoMtKyIVYCjdoyRnopKYa'     #Access Token
asecret='fnoOVQ5tcufBTK40p5o5tFnIaFnsBDT7qlMylKNEGvRdp'    #Access Token Secret


#setting Open Authorization to use twitter API
#order should be maintain of arguments given to OAuth

auth=twitter.oauth.OAuth(atoken,asecret,ckey,csecret)

#setting twitter API accessing object

twitter_api=twitter.Twitter(auth=auth)

#Enter the keyword
q=raw_input('Enter the word or hastag u want to search which is more trending : ')

#this variable is used to put the limit how much tweets u want to search,let's say=5
count=100

#search_results
search_results=twitter_api.search.tweets(q=q,count=count)

#each query is called stauses in search_results
statuses=search_results['statuses']

#Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    #print "Length of statuses",len(statuses)
    try:
        next_results=search_results['search_metadata']['next_results']
    except KeyError,e:
        break

    #creating a dictionary from next_results,which has the following form:
    # ?max_id=2121421421421424&q=NCAA&include_entities=1

    kwargs=dict([kv.split('=') for kv in next_results[1:].split("&")])

    #twitter_api.search.tweets(q=q,include_entities=1,max_id=241241242412)
    search_results=twitter_api.search.tweets(**kwargs)
    statuses+=search_results['statuses']

#storint information in list data structure of python
#getting all statuses text in statuses_Text LIST
status_text=[status['text'] for status in statuses]

#getting all statuses screen_names in statuses_name LIST
screen_names=[user_mention['screen_name'] for status in statuses
                                             for user_mention in status['entities']['user_mentions']]

#getting all statuses hashtags in hastags LIST
hashtags=[hashtag['text'] for status in statuses
                              for hashtag in status['entities']['hashtags']]

#printing only first 5 items for each
print "Status text"
print
print json.dumps(status_text[0:5],indent=1)
print
print "Screen names"
print
print json.dumps(screen_names[0:5],indent=1)
print
print "Hashtags"
print
print json.dumps(hashtags[0:5],indent=1)
print 
