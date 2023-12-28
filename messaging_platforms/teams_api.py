# messaging_platforms/teams_api.py

import requests

def get_teams_messages(access_token, team_id, channel_id):
    api_url = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(api_url, headers=headers)
    messages = response.json().get('value', [])
    return messages
