import re
import pandas as pd
import datetime as dt

date = dt.datetime(2019, 4, 25)

strdate = date.strftime('%Y/%m\%d')

print(strdate)

