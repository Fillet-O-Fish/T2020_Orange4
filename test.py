import requests

URL_STR = "http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com"
headers = {'identity': 'Group13', 'token' : '9d14bdf1-ffbe-48ef-b80a-99e9c85eaa22'}

def getCustIdUrl(userName):
    url = URL_STR + "/customers/" + userName
    r = requests.get(url, headers=headers)
    return r.json()

def getCustDetailsUrl(custId):
    url = URL_STR + "/customers/" + custId + "/details/"
    r = requests.get(url, headers=headers)
    return r.json()


def getTransactionDetailsUrl(accId, fromDate, toDate):
    url = URL_STR + "/transaction/" + accId + "?from=" + fromDate + "&to=" + toDate
    r = requests.get(url, headers=headers)
    return r.json()

def getPersonalMsg(custId):
    url = URL_STR + "/message/" + custId
    r = requests.get(url, headers=headers)
    return r.json()

def getMarketMsg(custId):
    url = URL_STR + "/marketing/" + custId
    r = requests.get(url, headers=headers)
    return r.json()

print(getCustIdUrl("limzeyang"))