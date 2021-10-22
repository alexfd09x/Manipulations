def monthgen (month,leapness):
    m1 = 31
    if leapness == True:
        m2 = 29
    else:
        m2 = 28
    m3 = 31
    m4 = 30
    m5 = 31
    m6 = 30
    m7 = 31
    m8 = 31
    m9 = 30
    m10 = 31
    m11 = 30
    m12 = 31
    if month == 0 :
        month = 0
    elif month == 1 :
        month = m1
    elif month == 2 :
        month = m1 + m2
    elif month == 3 :
        month = m1 + m2 + m3
    elif month == 4 :
        month = m1 + m2 + m3 + m4
    elif month == 5 :
        month = m1 + m2 + m3 + m4 + m5
    elif month == 6 :
        month = m1 + m2 + m3 + m4 + m5 + m6
    elif month == 7 :
        month = m1 + m2 + m3 + m4 + m5 + m6 + m7
    elif month == 8 :
        month = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8
    elif month == 9 :
        month = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9
    elif month == 10:
        month = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10
    elif month == 11:
        month = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11
    elif month == 12:
        month = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11 + m12
    else:
        month=0
    return month
def nothing (): nothing = null


