import dbsApi
# import pandas as pd
from rest_framework import serializers
# from .models import user

userInfo = {}


def init(user):
    userInfo = {}
    userInfo['id'] = dbsApi.getCustIdUrl(user)['customerId']
    userInfo['details'] = dbsApi.getCustDetailsUrl(userInfo['id'])
    userInfo['deposit'] = ""
    for i in dbsApi.getDepositAccountDetails(userInfo['id']):
        userInfo['deposit'] += (str(i['accountId']) + ",")
    userInfo['credit'] = ""
    for i in dbsApi.getCreditAcc(userInfo['id']):
        userInfo['credit']+=(str(i['accountId']) + ",")
    return userInfo

# init("limzeyang")


userInfo = init("marytan")
print(userInfo)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('name', 'userid', 'creditAccList','depositAccList')
