import urllib2
from bs4 import BeautifulSoup
import subprocess
import sys

# Load content, get class 'vacancy which contains job posts'
response = urllib2.urlopen('https://uncareer.net')
site = response.read()
soup = BeautifulSoup(site, 'html.parser')
vacancyRaw = soup.find_all('div', class_ = 'vacancy') # Should return a list of 24 elements

vacancyClean = []
for element in vacancyRaw:
    getText = element.get_text()
    splitText = getText.split('\n')
    cleanText = [x.encode('utf-8').strip() for x in splitText] # Text orginially read as str. Explicitly decode str to unicode
    tup = cleanText[2], cleanText[4], cleanText[5], cleanText[6] # Put relevant info into a tuple
    vacancyClean.append(tup)

# Call applescript
apple_cmd = "osascript -e '{0}'"
for i in range(len(vacancyClean)):
    base_cmd = 'display notification "{0}\n{1}" with title "{2}"'.format(vacancyClean[i][1], vacancyClean[i][3], vacancyClean[i][0])
    cmd = apple_cmd.format(base_cmd)
    subprocess.Popen([cmd], shell=True)
