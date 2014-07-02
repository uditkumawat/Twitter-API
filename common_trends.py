#"Set" in python refers to mathematical notion of data structure that stores an unordered collection of unique items.
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


#this WOE id I get from Yahoo Where on Earth
world_woe_id=1            # for entrie world WOE id is 1
india_woe_id=23424848            # for India WOE id is 23424848

world_trends=twitter_api.trends.place(_id=world_woe_id)
india_trends=twitter_api.trends.place(_id=india_woe_id)

#getting the name of trends from these two trends in different set

world_trends_set=set([trend['name'] for trend in world_trends[0]['trends']])
india_trends_set=set([trend['name'] for trend in india_trends[0]['trends']])

#checking for common trend in both the sets
common_trends_set=world_trends_set.intersection(india_trends_set)
#common_trends_set can be empty also because it depends on your query 
print common_trends_set

