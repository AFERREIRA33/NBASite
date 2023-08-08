import urllib.request
import json


def getAllPlayer():
    result = []
    url = "https://www.balldontlie.io/api/v1/players?per_page=100&page=0"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    for i in range(100):
        firstName = dict['data'][i]['first_name']
        lastName = dict['data'][i]['last_name']
        result.append({"firstName": firstName, "lastName": lastName})

    return result
