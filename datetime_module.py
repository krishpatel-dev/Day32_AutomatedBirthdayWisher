import datetime as dt

current_dt = dt.datetime.now()
year = current_dt.year
month = current_dt.month
day_of_week = current_dt.weekday()

if year == 2024:
    print("enjoy")

print(year)
print(day_of_week)

date_of_birth = dt.datetime(year= 2004, month= 4, day= 24, hour= 16)
print(date_of_birth)