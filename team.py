
import urllib.request
import json


def getAllTeam(pageNum):
    result = []
    url = "https://www.balldontlie.io/api/v1/teams?page=" + pageNum
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    num = 0
    if dict['meta']['total_count'] - (int(pageNum)*30) > 0:
        num = 30
    else:
        num = dict['meta']['total_count'] - (int(pageNum)*30) + 30
    for i in range(num):
        name = dict['data'][i]['name']
        id = dict['data'][i]['id']
        result.append(
            {"name": name, "idTeam": id})
    return result


def getATeam():

    return "toto"
