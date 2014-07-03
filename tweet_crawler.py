#twitter crawler
import urllib2
from bs4 import BeautifulSoup
import pprint
from PIL import Image

def make_request():
     topic=raw_input()
     url='https://twitter.com/search?q='+topic+'&src=typd&mode=news'
     response = urllib2.urlopen(url)
     html = response.read()
     soup = BeautifulSoup(html)
     print "Importing done"
     
     results=soup.find(id='stream-items-id')
     results=soup.find_all(attrs={'class':'content'})
     for result in results:
         res_name=result.find(attrs={'class':'fullname js-action-profile-name show-popup-with-id'} ).text
         #res_time=result.find(attrs={'class':'time'} ).text
         res_bio=result.find(attrs={'class':'js-tweet-text tweet-text'} ).text
         #img = (result.find(attrs={'class':'avatar js-action-profile-avatar'} )['src'])
         #print img
         #img.show()
         #print res_name
         #print res_time
         print res_bio
         print"******************************************************************************************"
         print
     #res_name=results.find('strong').text()
     #pprint.pprint(results)
         
make_request()
