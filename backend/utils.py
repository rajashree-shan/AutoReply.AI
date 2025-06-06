from datetime import datetime, timedelta

def find_available_slot(busy_slots):
    monday = datetime.now() + timedelta(days=(7 - datetime.now().weekday()) % 7)
    for day in range(5):
        date = monday + timedelta(days=day)
        for hour in range(9, 17):
            slot_start = date.replace(hour=hour, minute=0, second=0, microsecond=0)
            slot_end = slot_start + timedelta(minutes=30)
            conflict = any(datetime.fromisoformat(start) < slot_end and slot_start < datetime.fromisoformat(end)
                           for start, end in busy_slots)
            if not conflict:
                return slot_start.strftime("%Y-%m-%d %H:%M")
    return None
