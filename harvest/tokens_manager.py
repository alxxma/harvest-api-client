import requests
import json
import datetime
from dateutil import parser

class TokensManager(object):
    access_token_refresh_time = 18    #in hours
    refresh_token_refresh_time = 720  #in hours, 30 days
    last_refresh_time_key = 'last_refresh_time'
    value_key = 'value'
    seconds_per_hours = 3600
    client_secret = None
    client_id = None
    tokens_file_name = None

    @staticmethod
    def is_refresh_token_fresh():
        tokens = TokensManager.get_tokens()
        last_rd = parser.parse(tokens['refresh_token'][TokensManager.last_refresh_time_key])
        last_rd_diff = datetime.datetime.now() - last_rd
        res = last_rd_diff.total_seconds() / TokensManager.seconds_per_hours
        return res < TokensManager.refresh_token_refresh_time

    @staticmethod
    def refresh_access_token_by_demand():
        if not (TokensManager.is_access_token_fresh()):
            TokensManager.refresh_access_token() 

    @staticmethod
    def is_access_token_fresh():
        tokens = TokensManager.get_tokens()
        last_rd = parser.parse(tokens['access_token'][TokensManager.last_refresh_time_key])
        last_rd_diff = datetime.datetime.now() - last_rd
        res = last_rd_diff.total_seconds() / TokensManager.seconds_per_hours
        return res < TokensManager.access_token_refresh_time

    @staticmethod
    def refresh_access_token():
        json_data = TokensManager._refresh_access_token_impl()
        old_json_file_data = TokensManager.get_tokens()
        TokensManager.write_tokens({
            'access_token': {
                TokensManager.value_key: json_data['access_token'],
                TokensManager.last_refresh_time_key: datetime.datetime.now().isoformat()
            },
            'refresh_token': {
                TokensManager.value_key: json_data['refresh_token'],
                TokensManager.last_refresh_time_key: old_json_file_data['refresh_token'][TokensManager.last_refresh_time_key]
            }
        })

        print '\nThe access token has been refreshed.\n'
  
    @staticmethod
    def _refresh_access_token_impl():
        tokens = TokensManager.get_tokens()
        body = 'refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token'.format(
            refresh_token=tokens['refresh_token'][TokensManager.value_key], client_id=TokensManager.client_id, client_secret=TokensManager.client_secret
        )
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
        resp = requests.post('https://api.harvestapp.com/oauth2/token', headers=headers, data=body, verify=False)
        return json.loads(resp.content)

    @staticmethod
    def get_tokens():
        with open(TokensManager.tokens_file_name) as json_file:
            res = json.load(json_file)

        return res

    @staticmethod
    def write_tokens(data):
        with open(TokensManager.tokens_file_name, 'w') as json_file:
            json.dump(data, json_file)
