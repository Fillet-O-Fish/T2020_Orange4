import requests

URL_STR = "http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com"
USER = "limzeyang"
headers = {'identity': 'Group13', 'token' : '9d14bdf1-ffbe-48ef-b80a-99e9c85eaa22'}
url = URL_STR + "/customers/" + USER
r = requests.get(url,headers=headers)
print (r.text)