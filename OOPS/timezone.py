import datetime as dt
import pytz

naive_time=dt.datetime.now()
utc_naive_time=dt.datetime.utcnow()
print(naive_time)
print(utc_naive_time)
kolkata=pytz.timezone('Asia/Kolkata')
pacific=pytz.timezone('US/Pacific')

pst=pacific.localize(utc_naive_time)
print(pst)
ist=kolkata.localize(naive_time)
print(ist)