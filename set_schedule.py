import datetime
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

creds = service_account.Credentials.from_service_account_file('/Users/takedashuuhei/credential')
service = build('calendar', 'v3', credentials=creds)

calendar_id = 'shuhei.takeda.net@gmail.com'  

def create_event(summary, start_time, end_time):
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Asia/Tokyo',
        },
        'end': {
            'dateTime': end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Asia/Tokyo',
        },
    }
    try:
        event = service.events().insert(calendarId=calendar_id, body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')
    except HttpError as error:
        print(f'An error occurred: {error}')
        event = None
    return event

start_time = datetime.datetime(2025, 4, 30, 9, 0, 0)
end_time = datetime.datetime(2025, 4, 30, 10, 0, 0)
create_event('Meeting with John', start_time, end_time)

