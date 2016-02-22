#!/usr/bin/python
# compare datetime with windows.com

import datetime
import ntplib
client = ntplib.NTPClient()
r_xkl = client.request('192.168.1.232')
r_win = client.request('time.windows.com')

time1 = datetime.datetime.fromtimestamp(r_xkl.tx_time)
time2 = datetime.datetime.fromtimestamp(r_win.tx_time)

loc1 = "xkl"
loc2 = "windows.com"

time_text = "{location} time is : {time}." 

print time_text.format(location=loc1,time=time1)
print time_text.format(location=loc2,time=time2)