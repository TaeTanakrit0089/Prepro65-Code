"""I see a little silhouetto of a man"""


def main():
    """Scaramouch, Scaramouch, will you do the Fandango"""
    firstday = int(input())
    firsthour = int(input())
    lastday = int(input())
    lasthour = int(input())
    if lastday == firstday:
        #sameday
        counthours = lasthour - firsthour
    else:
        #notsameday
        counthours = (24-firsthour) + (24 * (lastday-firstday-1)) + lasthour
    if  (counthours < 0) or (firsthour >= 24) or (lasthour >= 24) or \
            (firstday >= 365) or (lastday >= 365) or (firstday <= 0) or \
                (lastday <= 0) or (firsthour < 0) or (lasthour < 0):
        print("error")
    else:
        print("%d day %d hour" % (counthours // 24, (counthours % 24)))
        print("%d baht" % calculate(counthours))


def calculate(bo1):
    """Thunderbolts and lightning, very, very frightening me"""
    summer = 0
    #Less than 2 hours
    if bo1 <= 2:
        summer = 0
    else:
        #morethan 1 day (24hours)
        if bo1 > 24:
            summer += ((bo1 // 24) * 200)
            summer += calculate(bo1 % 24)
        #1 day
        elif bo1 == 24:
            summer += 200
        #less than 1 day
        elif bo1 <= 24:
            if bo1 <= 12:
                summer += 15*bo1
            else:
                summer += 200

    # 1st week discount
    if bo1 >= 168:
        summer -= (bo1//168)*300
    # 4th week discount
    if bo1 >= 672:
        summer -= 500
    return summer


main()
