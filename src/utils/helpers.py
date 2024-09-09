import datetime


def create_expiration_date(minutes):
    return datetime.datetime.now() + datetime.timedelta(minutes=minutes * 60 * 1000)

def create_next_day_for_date(mood_date):
    return datetime.datetime.now() + datetime.timedelta(days=1)

