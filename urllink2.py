import urllib.request
from bs4 import BeautifulSoup

outfile = open('bs4_output.txt','w')

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   outfile.write('TAG:'+str(tag))
   print('TAG:',tag)
   print('URL:',tag.get('href', None))
   print('Contents:',tag.contents[0])
   print('Attrs:',tag.attrs)
