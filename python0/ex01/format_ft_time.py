import time
import calendar

seconds = time.time()
scientific_format = "{:e}".format(seconds)
local_time = time.localtime()
current_month = calendar.month_abbr[local_time.tm_mon]

print(f"Seconds since 1 January 1970: {seconds} or {scientific_format} in scientific notation")
print(f"{current_month} {local_time.tm_mday} {local_time.tm_year}")
