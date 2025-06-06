from fastapi import FastAPI, Header, HTTPException
from gmail import get_recent_emails, send_email
from classifier import classify_email
from calendar import get_available_slots
from utils import find_available_slot
import os

# Load token.json from environment variable if hosted (e.g., Render)
if not os.path.exists("token.json") and os.getenv("GOOGLE_TOKEN_JSON"):
    with open("token.json", "w") as f:
        f.write(os.environ["GOOGLE_TOKEN_JSON"])

app = FastAPI()

@app.get("/process-emails")
def process_emails(x_token: str = Header(...)):
    SECRET = "your-secret-token"
    if x_token != SECRET:
        raise HTTPException(status_code=403, detail="Unauthorized")

    emails = get_recent_emails()
    busy_slots = get_available_slots()

    for msg_id, body, from_email in emails:
        classification = classify_email(body)
        if classification == "rejection":
            continue
        elif classification == "interview":
            available_slot = find_available_slot(busy_slots)
            if available_slot and from_email:
                response = f"Thank you for reaching out. I'm available for a interview on {available_slot}."
                send_email(to=from_email, subject="Interview Availability", body=response)

    return {"status": "Processed"}
