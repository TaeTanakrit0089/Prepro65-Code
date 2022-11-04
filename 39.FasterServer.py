'''Welcome to Los Pollos Hermanos'''


def main():
    '''Welcome to Los Pollos Hermanos'''
    gusnum1 = int(input())
    gustext1 = (input())
    gusnum2 = int(input())
    gustext2 = (input())
    server1 = convert(gusnum1, gustext1)
    server2 = convert(gusnum2, gustext2)
    if server1 < server2:
        print("Server A, %.06f second" % server1)
        print("Faster than server B , %d times" % (server2/server1))
    elif server1 > server2:
        print("Server B, %.06f second" % server2)
        print("Faster than server A , %d times" % (server1/server2))
    else:
        print("equal")


def convert(hector1, hector2):
    '''Last chance to look at me Hector'''
    if hector2 == "Millisecond":
        ding = hector1 / 10**3
    elif hector2 == "Microsecond":
        ding = hector1 / 10**6
    elif hector2 == "Nanosecond":
        ding = hector1 / 10**9
    elif hector2 == "Picosecond":
        ding = hector1 / 10**12
    return ding


main()
