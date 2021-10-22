def notime (dayx,monthx,yearx,lean):
    import time
    import sys
    import monthgen
    from datetime import date
    today= str(date.today())
    day = int(today[-2] + today[-1])
    month = int(today[5] + today[6])
    year = int(today[0] + today[1] + today[2] + today[3])
    dayx = int(date[-2] + date[-1])
    monthx = date[5] + date[6]
    monthx=int(monthx)
    yearx = date[0] + date[1] + date[2] + date[3]
    yearx=int(yearx)
    yeah = (yearx - year) * 365
    month = monthgen.monthgen(month,lean)
    monthx = monthgen.monthgen(monthx,lean)
    mouth = monthx-month
    da = (dayx - day)
    datte = da + mouth + yeah
    return datte
