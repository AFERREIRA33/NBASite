import urllib.request
import json
from datetime import datetime


def getAllMatch(pageNum):
    result = []
    url = "https://www.balldontlie.io/api/v1/games?per_page=100&page=" + pageNum
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    num = 0
    if dict['meta']['total_count'] - (int(pageNum)*100) > 0:
        num = 100
    else:
        num = dict['meta']['total_count'] - (int(pageNum)*100) + 100
    for i in range(num):
        idMatch = dict['data'][i]['id']
        home = dict['data'][i]['home_team']['abbreviation']
        visitor = dict['data'][i]['visitor_team']['abbreviation']
        date = dict['data'][i]['date'].split("T")
        date = date[0]
        result.append(
            {"home": home, "visitor": visitor, "idMatch": idMatch, "date": date})
    return result, dict['meta']['total_pages']
