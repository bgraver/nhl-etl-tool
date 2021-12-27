import requests
import pandas as pd
import database_connection
import credential_handler

credentials = credential_handler.read_credentials()


def load_player_bio(credentials):
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
    ## Connect to SQL
    connection = database_connection.connect_to_sql(credentials['sql'])

    database_connection.insert_df_to_sql(bio_df, connection)





# def load_shot_data():
    # TODO


# def load_goal_data():
    # TODO
