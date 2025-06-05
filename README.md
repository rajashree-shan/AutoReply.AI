# AutoReply.AI
Chrome Extension to Manage Recruiter Emails Automatically
# 📦 What It Does

Reads unread Gmail messages  
Uses AI (spaCy) to classify emails:
- ❌ Rejection
- 📅 Interview  
📆 For interviews:
- Checks your Google Calendar (Mon–Fri, 9AM–5PM)
- Finds your next free 30-minute slot  
📤 Replies to the recruiter with your availability

---

## 🧩 Project Structure
├── chrome_extension/ # Chrome Extension (Frontend)
│ ├── manifest.json
│ ├── popup.html
│ ├── popup.js
│ └── icon.png
└── ai_email_assistant_backend/ # FastAPI Backend
├── main.py
├── gmail.py
├── calendar.py
├── classifier.py
├── utils.py
├── requirements.txt
└── token.json (auto-generated)

---

## 🛠️ Setup Instructions

- Clone the repository  
-  Create a Google Cloud Project  
-  Enable Gmail and Calendar APIs  
-  Configure OAuth Consent Screen and download `credentials.json`  
-  Place `credentials.json` in `ai_email_assistant_backend/`  
-  Run `gmail.py` to authenticate and generate `token.json`  
-  Start FastAPI server using `uvicorn main:app --reload`  
-  Load `chrome_extension/` in Chrome as an unpacked extension  
-  Click “Process Emails” to trigger classification and response  

---

## 🌐 Deploying to Render

-  Push backend to GitHub  
-  Set up new Render Web Service  
-  Add env var `GOOGLE_TOKEN_JSON` with contents of `token.json`  
-  Set build command: `pip install -r requirements.txt`  
-  Set start command: `uvicorn main:app --host 0.0.0.0 --port 10000`  

---

##  Security Notes

-  Use `x-token` header for securing API access  
-  Keep `token.json` private  
-  Add user management for multi-user setups (optional)  

---

## 🧠 Future Improvements

- Replace spaCy with transformer-based classifier (BERT, etc.)  
- Let users customize working hours  
- Allow confirmation before sending replies  
- Support multiple users and accounts  

---

## 💻 Tech Stack

-  Python (FastAPI)  
-  spaCy for NLP classification  
-  Gmail API  
-  Google Calendar API  
-  Chrome Extensions (Manifest V3)  

---
