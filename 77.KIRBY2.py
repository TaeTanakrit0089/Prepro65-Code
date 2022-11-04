"""Never Gonna Give You Up"""


def my_main():
    """Never Gonna Give You Up"""
    health = int(input())
    killed = 0

    while health > 0:
        job = input()
        mon = input().lower()

        print("------------")
        if job == "none" or mon == "none":
            print(health, "HP left")
            print("Kirby won!")
            print("You had defeated", killed, "enemies")
            print("------------")
            break

        hero_attack = job_get_attack(job)
        #print("Job = ", job, " Attack = ", hero_attack)

        mon_attack = getatk_mons(mon)
        mon_life = getlife_mons(mon)
        #print("mon = ", mon, " attack = ", mon_attack, " mon_life = ", mon_life)

        health = health - mon_attack
        mon_life = mon_life - hero_attack

        if mon_life <= 0 and mon != "heal" and health > 0:
            print("- " + mon + " had defeated -")
            killed = killed + 1

        if health > 0:
            print(health, "HP left")
        else:
            print(health, "HP left")
            print("GameOver!")
            print("You had defeated", killed, "enemies")

        print("------------")


def job_get_attack(job1):
    """job_get_attack"""
    attack = 0
    if job1 == "sword":
        attack = 4
    elif job1 == "magic":
        attack = 2
    elif job1 == "sleep":
        attack = 0
    elif job1 == "master":
        attack = 9
    return attack


def getlife_mons(mon1):
    """getlife_mons"""
    mon_life = 0
    if mon1 == "waddle dee":
        mon_life = 2
    elif mon1 == "laser ball":
        mon_life = 3
    elif mon1 == "waddle doo":
        mon_life = 5
    elif mon1 == "heal":
        mon_life = 0
    return mon_life


def getatk_mons(mon2):
    """getatk_mons"""
    mon_atk = 0
    if mon2 == "waddle dee":
        mon_atk = 1
    elif mon2 == "laser ball":
        mon_atk = 2
    elif mon2 == "waddle doo":
        mon_atk = 3
    elif mon2 == "heal":
        mon_atk = -2
    return mon_atk


my_main()
