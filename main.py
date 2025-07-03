from fastapi import FastAPI
from pydantic import BaseModel
from google.oauth2 import service_account
from googleapiclient.discovery import build


app = FastAPI()

CALENDAR_ID = '46ed56a3f5e8d37ccc70f0e471810b0175fe02b975679bd759cc4708114b19cc@group.calendar.google.com'
SERVICE_ACCOUNT_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build("calendar", "v3", credentials=credentials)

class Event(BaseModel):
    summary: str
    description: str
    start: str
    end: str

@app.post("/book")
def book_appointment(event: Event):
    try:
        event_body = {
            "summary": event.summary,
            "description": event.description,
            "start": {"dateTime": event.start, "timeZone": "UTC"},
            "end": {"dateTime": event.end, "timeZone": "UTC"}
        }
        created_event = service.events().insert(calendarId=CALENDAR_ID, body=event_body).execute()
        return {"status": "success", "event_link": created_event.get("htmlLink")}
    except Exception as e:
        return {"status": "error", "message": str(e)}


