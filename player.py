import urllib.request
import json


def getAllPlayer(pageNum):
    result = []
    url = "https://www.balldontlie.io/api/v1/players?per_page=100&page=" + pageNum
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    num = 0
    if dict['meta']['total_count'] - (int(pageNum)*100) > 100:
        num = 100
    else:
        num = dict['meta']['total_count'] - (int(pageNum)*100) + 100
    print("////////////////////////////////////////////////////" +
          str(num) + " / " + pageNum + " / " + str(dict['meta']['total_count']))
    for i in range(num):
        firstName = dict['data'][i]['first_name']
        lastName = dict['data'][i]['last_name']
        idPlayer = dict['data'][i]['id']
        result.append(
            {"firstName": firstName, "lastName": lastName, "idPlayer": idPlayer})
    return result


def getAPlayer(idPlayer):
    result = []
    url = "https://www.balldontlie.io/api/v1/players/" + idPlayer
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict
