import requests
from bs4 import BeautifulSoup as bs

github_user=input('Input Github User: ')
url='https://github.com/'+github_user
r=requests.get(url) #Sends a request to the url
soup=bs(r.content,'html.parser') #r is response of the request, so r.content is then converted to html
# print(soup)
# profile_img=soup.find('img',{'alt':'Avatar'}) # Finds img tag with alt='Avatar'
profile_img=soup.find('img',{'alt':'Avatar'})['src'] #Gets only the src from that img tag

print(profile_img)