import datetime
from datetime import timedelta
from datetime import datetime
import math

date_format = '%m/%d/%y'
today = datetime.now()
''' cant do today before past date because it changes into a string'''
past_date = today - timedelta(days=8)
past_date_str = past_date.strftime(date_format)
past_date_str = past_date_str.replace("/10/", "/99/")
past_date_str = past_date_str.replace("10", "99")
past_date_str = past_date_str.replace("20/", "98")
past_date_str = past_date_str.replace("20", "")
past_date_str = past_date_str.replace("0", "")
past_date_str = past_date_str.replace("98", "20/")
past_date_str = past_date_str.replace("/99/", "/10/")
past_date_str = past_date_str.replace("99", "10")
past_object = datetime.strptime(past_date_str, date_format).date()

today = today.strftime(date_format)
today = today.replace("/10/", "/99/")
today = today.replace("10", "99")
today = today.replace("20/", "98")
today = today.replace("20", "")
today = today.replace("0", "")
today = today.replace("98", "20/")
today = today.replace("/99/", "/10/")
today = today.replace("99", "10")
today_date = datetime.strptime(today, date_format).date()


def times_equal(dates):
    i = 100
    if dates == '':
        return i
    dates = dates.replace(" ", "")
    dates = dates.replace("\n", "")
    date_object = datetime.strptime(dates, date_format).date()

    if past_object <= date_object and date_object <= today_date:
        difference = today_date - date_object
        i = difference.days
        return math.floor(i)
    return math.floor(i)
