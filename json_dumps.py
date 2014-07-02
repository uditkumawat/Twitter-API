#URL encoding for hastag is "%23"
#Displaying API resources as pretty-printed JSON
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
india=23424848            # for India WOE id is 23424848

world_trends=twitter_api.trends.place(_id=world_woe_id)
india_trends=twitter_api.trends.place(_id=india)

print json.dumps(world_trends,indent=1)
print
print json.dumps(india_trends,indent=1)
