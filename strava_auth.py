import requests
import json
import time

token_file = 'strava_tokens.json'

def load_tokens():
    with open(token_file, 'r') as f:
        return json.load(f)

def save_tokens(tokens):
    with open(token_file, 'w') as f:
        json.dump(tokens, f, indent = 2)

def refresh_access_tokens(tokens):
    response = requests.post(
        'https://www.strava.com/api/v3/oauth/token',
        data = {
            'client_id': tokens['client_id'],
            'client_secret': tokens['client_secret'],
            'refresh_token': tokens['refresh_token'],
            'grant_type': 'refresh_token'
        }
    )

    if response.status_code != 200:
        raise Exception(f'Failed to refresh token: {response.text}')
    
    new_tokens = response.json()
    tokens['access_token'] = new_tokens['access_token']
    tokens['refresh_token'] = new_tokens['refresh_token']
    tokens['expires_at'] = new_tokens['expires_at']
    save_tokens(tokens)
    return tokens

def get_access_token():
    tokens = load_tokens()
    if time.time() > tokens['expires_at']:
        print('Access token expired. Refreshing...')
        tokens = refresh_access_tokens(tokens)
        print('Access tocken refreshed.')
    else:
        print(f'Access token is still valid: {tokens["access_token"]}')
    return tokens['access_token']