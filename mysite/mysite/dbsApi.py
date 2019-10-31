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

def getDepositAccountDetails(custId):
    url = URL_STR + "/accounts/deposit/" + custId
    r = requests.get(url, headers=headers)
    return r.json()

def getDepositBal(accId, year = None, month = None):
    url = URL_STR + "/accounts/deposit/" + accId
    if year is not None and month is not None:
        url += "/balance?month=" + month + '&year=' + year
    else:
        url += "/balance?month&year"
    r = requests.get(url, headers=headers)
    return r.json()

def getTransactionDetailsUrl(accId, fromDate='01-01-2018', toDate='01-31-2019'):
    url = URL_STR + "/transactions/" + accId + "?from=" + fromDate + "&to=" + toDate
    r = requests.get(url, headers=headers)
    return r.json()

def getPersonalMsg(custId):
    url = URL_STR + "/message/" + custId
    r = requests.get(url, headers=headers)
    return r.json()

def getMarketMsgList():
    url = URL_STR + "/marketing"
    r = requests.get(url, headers=headers)
    return r.json()

def getMarketMsg(msgId):
    url = URL_STR + "/marketing/" + msgId
    r = requests.get(url, headers=headers)
    return r.json()

def getCreditAcc(custId):
    url = URL_STR + "/accounts/credit/" + custId
    r = requests.get(url, headers=headers)
    return r.json()
    
def getCreditAccOutstandingBalance(accId):
    url = URL_STR + "/accounts/credit/" + accId + "/balance"
    r = requests.get(url, headers=headers)
    return r.json()

