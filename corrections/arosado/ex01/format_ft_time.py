import datetime as dt

now = dt.datetime.now()
utc = dt.datetime(1970, 1, 1)

secondsElapsed = (now - utc).total_seconds()

print(f"""\
Seconds since January 1, 1970:\
{secondsElapsed:,.4f}\
or, {secondsElapsed:.2e},\
in scientific notation""",
)
print(now.strftime("%b %d %Y"))
