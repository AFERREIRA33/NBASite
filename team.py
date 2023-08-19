
import urllib.request
import json
import player


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


def getATeam(idTeam, teamFirst, teamLast, page):
    url = "https://www.balldontlie.io/api/v1/teams/" + idTeam
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    print(dict)
    result = []
    teamFirst = int(teamFirst)
    teamLast = int(teamLast)
    if page == "+":
        playerActualPage = str(teamLast)
        teamFirst = teamLast + 1
        while(len(result) < 6 and int(playerActualPage) < 51):
            playerActualPage = str(int(playerActualPage) + 1)
            allPlayer = player.getAllPlayer(playerActualPage)
            for i in range(len(allPlayer)):
                if allPlayer[i]['idTeam'] == int(idTeam):
                    result.append(allPlayer[i])
        teamLast = int(playerActualPage)
    else:
        playerActualPage = str(teamFirst)
        teamLast = teamFirst - 1
        while(len(result) < 6 and int(playerActualPage) > 1):
            playerActualPage = str(int(playerActualPage) - 1)
            allPlayer = player.getAllPlayer(playerActualPage)
            for i in range(len(allPlayer)):
                if allPlayer[i]['idTeam'] == int(idTeam):
                    result.append(allPlayer[i])
        teamFirst = int(playerActualPage)
    print(result)
    print(str(teamFirst) + "/" + str(teamLast))
    return dict, result, teamFirst, teamLast
