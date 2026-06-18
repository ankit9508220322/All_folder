import numpy as np
import datetime
import time
date = np.datetime64('2026-07-01')
print(date)

# ///////////////////////////////
# current date print
# current_date = np.datetime64('today')
# print(current_date)

# //////////////////////////////////
# now = np.datetime64('now')
# print(now)
# ////////////////////////////////

# //////////////////////////////
# current date and time
# current_datetime = np.datetime64('now')
# print(current_datetime)
# ///////////////////////////////
# while True:
#     now = datetime.datetime.now()
#     print(now.strftime("%Y-%m-%d %H:%M:%S"))
#     time.sleep(3)

# create array Date and time
# dates = np.array(['2026-03-17', '2026-03-18', '2026-03-19'], dtype='datetime64')
# print(dates)

# dates = np.array(['2026-03-17', '2026-03-18', '2026-03-19'], dtype='datetime64')
# print(dates)
# //////////////////////////////////////
# dates = np.arange('2026-03-01', '2026-03-10', dtype='datetime64[D]')
# print(dates)
# ///////////////////////////////////
# date = np.datetime64('2026-03-17')
# new_date = date+np.timedelta64(5, 'D')
# print(new_date)
# //////////////////////////////////
# d1 = np.datetime64('2026-03-14')
# d2 = np.datetime64('2026-03-27')
# diff = d2-d1
# print(diff)

# ////////////////////////////////
# dates = np.array(['2024-01-01', '2024-01-02', '2024-01-03'], dtype='datetime64[D]')
# # Filter dates after the first day
# filtered_dates = dates[dates > np.datetime64('2024-01-01')]
# print(filtered_dates) # Output: ['2024-01-02' '2024-01-03']
