"""LOS POLLOS HERMANOS"""


def main():
    """LOS POLLOS HERMANOS"""
    min_personerson = int(input())
    person = int(input())

    if person > min_personerson:
        second_person = person
    else:
        second_person = min_personerson
        min_personerson = person

    for i in range(8):
        person = int(input())

        if (person < second_person) and (person != min_personerson):
            second_person = person

        if person < min_personerson:
            second_person = min_personerson
            min_personerson = person
        i = i

    print("Almost the min :", second_person)


main()
