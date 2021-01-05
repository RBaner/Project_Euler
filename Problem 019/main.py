def sol(start,stop,start_day):
    """
    give start/stop years (Jan 1 Start -> Dec 31 Stop) as well as
    start_day as a number (0,7) with sunday being 0.
    e.g. sol(1901,2000,2) finds all sunday firsts of months between
    jan 1 1901,dec 31 2000 inclusive given that jan 1 1901 is a tuesday
    """
    day = start_day
    count = 0
    months = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for year in range(start,stop+1):
        leap = False
        if (year %4 == 0 and year%100 != 0) or (year%400 == 0):
            leap = True
        for month in months:
            if type(month) == list:
                day += month[leap]
                if (day+1)%7 == 0:
                    count += 1
            else:
                day+= month
                if (day+1)%7 == 0:
                    count += 1
    return(count)
