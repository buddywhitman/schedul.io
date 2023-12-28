# task_scheduler.py

from calendar_api.google_calendar import create_google_calendar_event, get_google_calendar_service
from calendar_api.outlook_calendar import create_outlook_calendar_event  # Add import for Outlook (if available)
from calendar_api.apple_calendar import create_apple_calendar_event  # Add import for Apple (if available)
from messaging_platforms.slack_api import get_slack_messages
from messaging_platforms.telegram_api import get_telegram_messages
from messaging_platforms.teams_api import get_teams_messages
from message_parser.nlp_parser import parse_message
import os

USER_ACCESS_TOKENS = {
    'slack': 'YOUR_SLACK_ACCESS_TOKEN',
    'telegram': 'YOUR_TELEGRAM_ACCESS_TOKEN',
    'teams': 'YOUR_TEAMS_ACCESS_TOKEN'
}

def fetch_messages(platform, access_token, team_id=None, channel_id=None):
    if platform == 'slack':
        messages = get_slack_messages(access_token, channel_id)
    elif platform == 'telegram':
        messages = get_telegram_messages(access_token)
    elif platform == 'teams':
        messages = get_teams_messages(access_token, team_id, channel_id)
    else:
        messages = []

    return messages

def schedule_events(platform, team_id=None, channel_id=None):
    messages = fetch_messages(platform, USER_ACCESS_TOKENS[platform], team_id, channel_id)
    for message in messages:
        event_details = parse_message(message['text'])
        if event_details:
            create_google_calendar_event(event_details)
            # Add calls to create events in Outlook and Apple calendars if available
            create_outlook_calendar_event(event_details)
            create_apple_calendar_event(event_details)
