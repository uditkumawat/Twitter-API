import twitter
import json
# code for "#" is %23

ckey='bTt1LYXAn6SGMpBZwXlVEwbNa'
csecret='Xkns5QTECAgvYjOhHCjFCoihbiZavcrvU6sQF7U0RRHilgFbs3'
atoken='323025517-fMkCvhUt32BvCUPmr4pIoMtKyIVYCjdoyRnopKYa'
asecret='fnoOVQ5tcufBTK40p5o5tFnIaFnsBDT7qlMylKNEGvRdp'


auth=twitter.oauth.OAuth(atoken,asecret,ckey,csecret)

twitter_api=twitter.Twitter(auth=auth)
print twitter_api
wwid=1
uswid=23424977

world_trends=twitter_api.trends.place(_id=wwid)
us_trends=twitter_api.trends.place(_id=uswid)

print json.dumps(world_trends,indent=1)
print
print json.dumps(us_trends)
