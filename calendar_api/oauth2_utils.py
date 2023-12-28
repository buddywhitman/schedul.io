# oauth2_utils.py

import requests

def get_access_token(client_id, client_secret, authorization_code, token_url):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'client_id': client_id,
        'client_secret': client_secret,
    }

    response = requests.post(token_url, headers=headers, data=data)
    return response.json().get('access_token')
