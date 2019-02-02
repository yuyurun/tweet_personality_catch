import urllib.request as request
import re

def twitProf(usrId):
  res = request.urlopen('https://twitter.com/'+usrId)
  html = res.read().decode('utf-8')
  res.close()

  m = re.search(r'\<p\sclass="ProfileHeaderCard\-bio\su\-dir"\sdir="ltr"\>(.+?)\</p\>',html)

  return m.group(1)

if __name__ == '__main__':
  id = 'yuyurun'
  print('id :',id)
  print('profile :',twitProf(id))
