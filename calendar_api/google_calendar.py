# calendar_api/google_calendar.py

import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

def get_google_calendar_service():
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

def create_google_calendar_event(event_details):
    service = get_google_calendar_service()

    event = {
        'summary': event_details['summary'],
        'location': event_details.get('location', ''),
        'description': event_details.get('description', ''),
        'start': {
            'dateTime': event_details['start_time'],
            'timeZone': 'YOUR_TIME_ZONE',
        },
        'end': {
            'dateTime': event_details['end_time'],
            'timeZone': 'YOUR_TIME_ZONE',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Google Calendar Event created: {event.get('htmlLink')}")
