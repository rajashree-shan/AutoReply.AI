from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.message import EmailMessage
import base64

def get_gmail_service():
    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/gmail.modify"])
    service = build("gmail", "v1", credentials=creds)
    return service

def get_recent_emails():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', maxResults=10, q="is:unread").execute()
    messages = results.get('messages', [])
    email_bodies = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        body = ""
        for part in msg_data['payload'].get('parts', []):
            if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')

        headers = msg_data['payload']['headers']
        from_email = next((h['value'] for h in headers if h['name'].lower() == 'from'), None)
        email_bodies.append((msg['id'], body, from_email))
    return email_bodies

def send_email(to, subject, body):
    service = get_gmail_service()
    message = EmailMessage()
    message.set_content(body)
    message['To'] = to
    message['From'] = "me"
    message['Subject'] = subject

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    create_message = {'raw': encoded_message}
    service.users().messages().send(userId="me", body=create_message).execute()
