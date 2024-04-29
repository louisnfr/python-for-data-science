import datetime

now = datetime.datetime.now()
utc = datetime.datetime(1970, 1, 1)

secondsElapsed = (now - utc).total_seconds()

print("Seconds since January 1, 1970:", f"{secondsElapsed:,.4f}", "or", f"{secondsElapsed:.3}", "in scientific notation")
print(now.strftime("%b %d %Y"))
