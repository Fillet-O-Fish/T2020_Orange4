# Create your views here.
from django.http import HttpResponse
from .main import init
import requests
import simplejson

def Data(request):
    response = requests.get('http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/marytan',
                            headers={"identity": "Group11", "token": "bf38d9ac-fade-40ef-b7d2-eabdb183acce"})

    data = response.json()
    response = requests.get('http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/' + data['customerId'] + '/details',
                            headers={"identity": "Group11", "token": "bf38d9ac-fade-40ef-b7d2-eabdb183acce"})
    data2 = response.json()

    #response = requests.get('http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/transactions/' + data['customerId'] + '?from=01-01-2018&to=02-01-2019',
     #                       headers={"identity": "Group11", "token": "bf38d9ac-fade-40ef-b7d2-eabdb183acce"})
    #data3 = response.json()

    data = simplejson.dumps( {
        'username': data['userName'],
        'id': data['customerId'],
        'gender': data2['gender'],
        'firstname': data2['firstName'],
        'lastname': data2['lastName'],
        'lastlogin': data2['lastLogIn'],
        'dateofbirth': data2['dateOfBirth']

    })
    return HttpResponse(data, content_type='application/json')