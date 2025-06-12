import datetime
# 1
# five days ago from today's date
today = datetime.datetime.now()
print(today - datetime.timedelta(days=5))

# 2
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)


# 3
today = datetime.datetime.now()
print("Original:", today)
# remove microseconds
cleaned = today.replace(microsecond=0)
print("Cleaned:", cleaned)


# 4
date1 = datetime.datetime(2025, 6, 12, 12, 0, 0)  # June 12, 2025 at 12:00:00
date2 = datetime.datetime(2025, 6, 12, 12, 5, 30)  # June 12, 2025 at 12:05:30

difference = abs(date1 - date2)
seconds = difference.total_seconds()
print("Difference in seconds:", seconds)
