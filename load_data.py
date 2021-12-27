import requests
import pandas as pd
import database_connection
import pprint


def load_player_bio():
    complete_player_list = []
    for start in range(0, 9):
        headers = {}
        params = {
            "isAggregate": False,
            "isGame": False,
            "sort": '[{"property":"lastName","direction":"ASC_CI"},{"property":"skaterFullName","direction":"ASC_CI"},{"property":"playerId","direction":"ASC"}]',
            "start": start*100,
            "limit": (start+1)*100,
            "factCayenneExp": "gamesPlayed>=1",
            "cayenneExp": "gameTypeId=2 and seasonId<=20212022 and seasonId>=20212022"
        }
        r = requests.get('https://api.nhle.com/stats/rest/en/skater/bios', headers=headers, params=params)
        complete_player_list += r.json()['data']
    bio_df = pd.DataFrame.from_dict(complete_player_list)
    print(bio_df)
    # Insert DF into the table (however that gets done...)
    database_connection.insert_df_to_sql(bio_df, 'players')


def load_schedule():
    game_ids = []
    headers = {}
    params = {
        "startDate": "2021-07-21",
        "endDate": "2022-07-21",
        "hydrate": "team, linescore, game(content(media(epg)), seriesSummary), seriesSummary(series)",
        "site": "en_nhl"
    }
    r = requests.get("https://statsapi.web.nhl.com/api/v1/schedule", headers=headers, params=params)
    schedule = r.json()['dates']
    # pprint.pprint(schedule)
    for game_day in schedule:
        for game in game_day['games']:
            game_ids.append(game['gamePk'])
            # pprint.pprint(game['gamePk'])
    schedule_df = pd.DataFrame(data={'gamePk': game_ids})
    print(schedule_df)
    database_connection.insert_df_to_sql(schedule_df, 'games')




# def load_shot():
    # TODO


# def load_goal():
    # TODO
