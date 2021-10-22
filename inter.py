def dayint(date):
    day = int(date[-2] + date[-1])
    return day
def monthint(date):
    month = int(date[5] + date[6])
    return month
def yearint(date):
    year = int(date[0] + date[1] + date[2] + date[3])
    return year