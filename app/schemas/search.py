import json

def match_info(match)->json:
    return{
        "Id": str(match['_id']),
        "gameMode": match['gameMode'],
        "matchId": match['matchId'],
        "gameDuration": match['gameDuration'],
        "gameCreation": match['gameCreation'],

        "summonerOnePuuid": match['summonerOnePuuid'],
        "summonerTwoPuuid": match['summonerTwoPuuid'],
        "summonerThreePuuid": match['summonerThreePuuid'],
        "summonerFourPuuid": match['summonerFourPuuid'],
        "summonerFivePuuid": match['summonerFivePuuid'],
        "summonerSixPuuid": match['summonerSixPuuid'],
        "summonerSevenPuuid": match['summonerSevenPuuid'],
        "summonerEightPuuid": match['summonerEightPuuid'],
        "summonerNinePuuid": match['summonerNinePuuid'],
        "summonerTenPuuid": match['summonerTenPuuid'],

        'summonerOneriotIdGameName': match['info']['participants'][0]['riotIdGameName'],
        'summonerTworiotIdGameName': match['info']['participants'][1]['riotIdGameName'],
        'summonerThreeriotIdGameName': match['info']['participants'][2]['riotIdGameName'],
        'summonerFourriotIdGameName': match['info']['participants'][3]['riotIdGameName'],
        'summonerFiveriotIdGameName': match['info']['participants'][4]['riotIdGameName'],
        'summonerSixriotIdGameName': match['info']['participants'][5]['riotIdGameName'],
        'summonerSevenriotIdGameName': match['info']['participants'][6]['riotIdGameName'],
        'summonerEightriotIdGameName': match['info']['participants'][7]['riotIdGameName'],
        'summonerNineriotIdGameName': match['info']['participants'][8]['riotIdGameName'],
        'summonerTenriotIdGameName': match['info']['participants'][9]['riotIdGameName'],

        'summonerOneriotIdTagline': match['info']['participants'][0]['riotIdTagline'],
        'summonerTworiotIdTagline': match['info']['participants'][1]['riotIdTagline'],
        'summonerThreeriotIdTagline':match['info']['participants'][2]['riotIdTagline'],
        'summonerFourriotIdTagline':match['info']['participants'][3]['riotIdTagline'],
        'summonerFiveriotIdTagline': match['info']['participants'][4]['riotIdTagline'],
        'summonerSixriotIdTagline': match['info']['participants'][5]['riotIdTagline'],
        'summonerSevenriotIdTagline': match['info']['participants'][6]['riotIdTagline'],
        'summonerEightriotIdTagline': match['info']['participants'][7]['riotIdTagline'],
        'summonerNineriotIdTagline': match['info']['participants'][8]['riotIdTagline'],
        'summonerTenriotIdTagline': match['info']['participants'][9]['riotIdTagline'],

        'summonerOneChampionName': match['info']['participants'][0]['championName'],
        'summonerTwoChampionName': match['info']['participants'][1]['championName'],
        'summonerThreeChampionName':match['info']['participants'][2]['championName'],
        'summonerFourChampionName':match['info']['participants'][3]['championName'],
        'summonerFiveChampionName': match['info']['participants'][4]['championName'],
        'summonerSixChampionName': match['info']['participants'][5]['championName'],
        'summonerSevenChampionName': match['info']['participants'][6]['championName'],
        'summonerEightChampionName': match['info']['participants'][7]['championName'],
        'summonerNineChampionName': match['info']['participants'][8]['championName'],
        'summonerTenChampionName': match['info']['participants'][9]['championName'],

        "teamBlueId": match['teamBlueId'],
        "teamBlueBan": list(match[i]['championId'] for i in range(5)),
        "teamBluePick": list(match['teamBluePick']),
        "teamBlueWin": match['teamBlueWin'],
        "teamBlueGold": match['teamBlueGold'],
        "teamBlueBaronKills": match['teamBlueBaronKills'],
        "teamBlueChampionKills": match['teamBlueChampionKills'],
        "teamBlueDragonKills": match['teamBlueDragonKills'],
        "teamBlueHordeKills": match['teamBlueHordekilss'],
        "teamBlueInhibitorKills": match['teamBlueInhibitorKills'],
        "teamBlueRiftheraldKills": match['teamBlueRiftheraldKills'],
        "teamBlueTowerKills": match['teamBlueTowerKills'],

        "teamRedId": match['teamRedId'],
        "teamRedBan": list(match[i]['championId'] for i in range(5)),
        "teamRedPick": list(match['teamRedPick']),
        "teamRedWin": match['teamRedWin'],
        "teamRedGold": match['teamRedGold'],
        "teamRedBaronKills": match['teamRedBaronKills'],
        "teamRedChampionKills": match['teamRedChampionKills'],
        "teamRedDragonKills": match['teamRedDragonKills'],
        "teamRedHordeKills": match['teamRedHordekilss'],
        "teamRedInhibitorKills": match['teamRedInhibitorKills'],
        "teamRedRiftheraldKills": match['teamRedRiftheraldKills'],
        "teamRedTowerKills": match['teamRedTowerKills']
    }

def summoner_info(summoner) -> json:
    return{
        "Id": str(summoner['_id']),
        "matchId": summoner['matchId'],
        "assists": summoner['assists'],
        "champLevel": summoner['champLevel'],
        "championId": summoner['championId'],
        "championName": summoner['championName'],
        "deaths": summoner['deaths'],
        "goldEarned": summoner['goldEarned'],
        "goldSpent": summoner['goldSpent'],
        "kills": summoner['kills'],
        "lane": summoner['lane'],
        "summonerName": summoner['summonerName'],
        "riotIdGameName": summoner['riotIdGameName'],
        "riotIdTagline": summoner['riotIdTagline'],
        "role": summoner['role'],
        "teamId": summoner['teamId'],
        "totalDamageDealtToChampions": summoner['totalDamageDealtToChampions'],
        "totalDamageTaken": summoner['totalDamageTaken'],
        "totalHeal": summoner['totalHeal'],
        "totalTimeCCDealt": summoner['totalTimeCCDealt'],
        "win": summoner['win'],
        "visionScore": summoner['visionScore'],
        "versusassists": summoner['versusassists'],
        "versuschampionLevel" :summoner['versuschampionLevel'],
        "versusdeaths":summoner['versusdeaths'],
        "versusgoldEarned":summoner['versusgoldEarned'],
        "versuskills":summoner['versuskills'],
        "versusTDDTC":summoner['versusTDDTC'],
        "versusTDT": summoner['versusTDT'],
        "versusTH":summoner['versusTH'],
        "versusTTCCD":summoner['versusTTCCD'],
        "versusVS": summoner['versusVS'],
    }