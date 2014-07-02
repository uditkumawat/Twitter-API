import twitter

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

print twitter_api
