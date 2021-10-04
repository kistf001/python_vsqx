import datetime 

def timeStemp():
    now = datetime.datetime.now()
    a1 = str(now.year).zfill(4)
    a2 = str(now.month).zfill(2)
    a3 = str(now.day).zfill(2)
    a4 = str(now.hour).zfill(2)
    a5 = str(now.minute).zfill(2)
    a6 = str(now.second).zfill(2)
    return a1+a2+a3+"_"+a4+a5+a6
