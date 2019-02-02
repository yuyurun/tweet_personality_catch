import urllib.request as request
import re
import argparse

def twitProf(usrId):
  res = request.urlopen('https://twitter.com/'+usrId)
  html = res.read().decode('utf-8')
  res.close()

  m = re.search(r'\<p\sclass="ProfileHeaderCard\-bio\su\-dir"\sdir="ltr"\>(.+?)\</p\>',html)

  return m.group(1)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', '--user_name', action ='store')
  args = parser.parse_args()
  username = args.user_name
  id = username
  print('id :',id)
  print('profile :',twitProf(id))
