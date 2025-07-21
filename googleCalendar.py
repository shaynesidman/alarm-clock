import datetime
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_events():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If no (valid) credentials, prompt login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' = UTC time
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=5, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    simplified = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        simplified.append({
            'summary': event['summary'],
            'start': start
        })

    return simplified
