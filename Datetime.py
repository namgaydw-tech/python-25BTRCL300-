from datetime import date, datetime, timedelta

today = date.today()
now = datetime.now()

bd = date(2036, 1, 1)

temp = now.strftime("%d-%m-%y %H:%M:%S")

future = today + timedelta(days=7)

print("Today:", today)
print("Current time:", now)
print("BD:", bd)
print("Formatted time:", temp)
print("7 days later:", future)