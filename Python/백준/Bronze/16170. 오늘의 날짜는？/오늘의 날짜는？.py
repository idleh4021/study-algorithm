from datetime import datetime,timezone
dt = datetime.now(timezone.utc)
print(dt.year)
print(dt.month)
print(dt.day)