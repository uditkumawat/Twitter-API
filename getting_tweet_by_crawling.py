import urllib
import json

#getting the source code of the page
response=urllib.urlopen("https://twitter.com/search?q=udit&src=hash")

#converting the data into json format....now it will be in dictionary form in python
pyresponse=json.loads(response)

#print type(pyresponse)

#print pyresponse.keys()     #it will give the keys of query....we have to work on "result" key to have the tweet


#print pyresponse["results"]

#print type(pyresponse["results"])    #thsi will return "list" as type

results=pyresponse["results"]

#print results[0]     # printing first result

#print result[0].keys()          #finding key of the text in first result

#we get the as "text"

for i in range(10):
    print results[i]["text"]




