from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

def get_calendar_service():
    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/calendar"])
    service = build("calendar", "v3", credentials=creds)
    return service

def get_available_slots():
    service = get_calendar_service()
    now = datetime.utcnow()
    monday = now + timedelta(days=(7 - now.weekday()) % 7)
    end = monday + timedelta(days=5)

    start_time = monday.replace(hour=9, minute=0, second=0, microsecond=0).isoformat() + 'Z'
    end_time = end.replace(hour=17, minute=0, second=0, microsecond=0).isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary', timeMin=start_time, timeMax=end_time,
                                          singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    busy_slots = [(event['start']['dateTime'], event['end']['dateTime']) for event in events if 'dateTime' in event['start']]
    return busy_slots
