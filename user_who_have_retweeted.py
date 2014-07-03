import twitter
import json


ckey='bTt1LYXAn6SGMpBZwXlVEwbNa'
csecret='Xkns5QTECAgvYjOhHCjFCoihbiZavcrvU6sQF7U0RRHilgFbs3'
atoken='323025517-fMkCvhUt32BvCUPmr4pIoMtKyIVYCjdoyRnopKYa'
asecret='fnoOVQ5tcufBTK40p5o5tFnIaFnsBDT7qlMylKNEGvRdp'

auth=twitter.oauth.OAuth(atoken,asecret,ckey,csecret)

twitter_api=twitter.Twitter(auth=auth)

id=317127304981667841

_retweets=twitter_api.statuses.retweets(id=id)

print [rt['user']['name'] for rt in _retweets]
