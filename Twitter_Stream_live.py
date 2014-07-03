#Twitter Streaming API

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

twitter_stream=twitter.TwitterStream(auth=auth)


stream=twitter_stream.statuses.filter(track="microsoft")


for status in stream:
    print status
