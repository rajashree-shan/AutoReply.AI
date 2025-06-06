import spacy
nlp = spacy.load("en_core_web_sm")

def classify_email(text):
    text_lower = text.lower()
    if "unfortunately" in text_lower or "we regret to inform" in text_lower:
        return "rejection"
    elif "30-minute" in text_lower or "30 min" in text_lower or "interview" in text_lower:
        return "interview"
    return "other"
