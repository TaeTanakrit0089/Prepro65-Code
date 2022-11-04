"""So you think you can stop me and spit in my eye"""


def findx(hector1):
    """So you think you can love me and leave me to die"""
    if hector1 == 'sword':
        hector2 = 4
    elif hector1 == "magic":
        hector2 = 3
    elif hector1 == 'sleep':
        hector2 = 0
    elif hector1 == 'master':
        hector2 = 9
    return hector2


def main():
    """Oh, baby, can't do this to me, baby"""
    health = int(input())
    anta_defeated = 0
    first = 0
    i = 1
    while i > 0:
        if health <= 0:
            print("------------")
            gameover(health, anta_defeated)
        prota = input().lower()
        anta = input().lower()
        prota_damage = findx(prota)
        anta_hp = 0
        anta_damage = 0

        if anta == 'waddle dee':
            anta_hp = 2
            anta_damage = 1
        elif anta == 'laser ball':
            anta_hp = 3
            anta_damage = 2
        elif anta == 'waddle doo':
            anta_hp = 5
            anta_damage = 3
        elif anta == 'heal':
            anta_hp = 0
            anta_damage = -2
        elif anta == 'none':
            if first == 0:
                anta_final = health - anta_damage
            print("------------")
            print(anta_final, "HP left")
            print("Kirby won!")
            print("You had defeated", anta_defeated, "enemies")
            print("------------")
            break

        first = 1
        anta_final = health - anta_damage
        print("------------")
        if (health >= anta_damage) and (prota_damage > anta_hp) and \
            (anta != 'heal') and (health > 0):
            #print("- %s had defeated -" % anta)
            print("-", anta, "had defeated -")
            anta_defeated += 1
        if anta_final <= 0:
            gameover(anta_final, anta_defeated)
            break
        else:
            print(anta_final, "HP left")
            health -= anta_damage
        print("------------")
        i = i


def gameover(hector1, hector2):
    '''Just gotta get out, just gotta get right outta here'''
    print("%d HP left" % hector1)
    print("GameOver!")
    print("You had defeated", hector2, "enemies")
    print("------------")


main()
