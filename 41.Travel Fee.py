'''Welcome to Los Pollos Hermanos'''


def main():
    '''Welcome to Los Pollos Hermanos'''
    national = ""
    thai = True

    #**********************************Input
    thai1 = input()
    if thai1 == "Y":
        thai = True
    elif thai1 == "N":
        thai = False
        national = input()
    age1 = int(input())
    discount1 = input()
    if discount1 == "Y":
        discount = True
        percentdis = int(input())
    else:
        discount = False

    #**********************************Calculate
    if (age1 > 60) or (age1 <= 10):
        gussum = 0
    elif (age1 > 10) and (age1 <= 20):
        gussum = 20
    else:
        gussum = 40

    if thai == False:
        gussum = gussum * 5

    if (national == "Vietnam") or (national == "Singapore") or (national == "India"):
        gussum = gussum / 2

    if discount == True:
        gussum = gussum * (100-percentdis) / 100

    print("%.2f" % gussum)


main()
