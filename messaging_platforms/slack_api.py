# messaging_platforms/slack_api.py

import requests

def get_slack_messages(token, channel_id):
    api_url = 'https://slack.com/api/conversations.history'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'channel': channel_id}
    response = requests.get(api_url, headers=headers, params=params)
    messages = response.json().get('messages', [])
    return messages
