"""LOS POLLOS HERMANOS"""


def check(gus):
    """LOS POLLOS HERMANOS"""
    if gus >= 15501:
        print("7th Layer : The Final Maelstrom")
        curse = "Certain death."
    elif gus >= 13001:
        print("6th Layer : The Capital of the Unreturned")
        curse = "Loss of humanity or death, or under specific conditions, the Blessing."
    elif gus >= 12001:
        print("5th Layer : Sea of Corpses")
        curse = "Complete sensory deprivation, confusion and self-harming behavior."
    elif gus >= 7001:
        print("4th Layer : The Goblets of Giants")
        curse = "Intense pain throughout the body and bleeding from every orifice."
    elif gus >= 2601:
        print("3rd Layer : Great Fault")
        curse = "Vertigo combined with visual and auditory hallucinations."
    elif gus >= 1351:
        print("2nd Layer : Forest of Temptation")
        curse = "Intense nausea, headaches, and numbness of limbs."
    else:
        print("1st Layer : Edge of the Abyss")
        curse = "Light dizziness and nausea."
    return curse


def main(name1, height1, direction1):
    """LOS POLLOS HERMANOS"""
    print("Name :", name1)
    if direction1 == "UP":
        print("Curse :", check(height1))
    elif direction1 == "DOWN":
        check(height1)
        print("Curse : -")


main(input(), int(input()), input())
print("---")
main(input(), int(input()), input())
print("---")
main(input(), int(input()), input())
