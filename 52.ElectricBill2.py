"""Welcome To Los Pollos Hermanos"""


def main():
    """Welcome To Los Pollos Hermanos"""
    gusfring1 = [int(input()), int(input()), int(
        input()), int(input()), int(input())]

    print("TV %d Watt %d ea for %d hours\n%.2f unit."
          % (gusfring1[0], 1, 3, float((gusfring1[0]*3/1000) * 30)))
    print("Microwave %d Watt %d ea for %d hours\n%.2f unit."
          % (gusfring1[1], 1, 1, float((gusfring1[1]*1/1000) * 30)))
    print("Hair dryer %d Watt %d ea for %.1f hours\n%.2f unit."
          % (gusfring1[2], 1, 0.5, float((gusfring1[2]*0.5/1000) * 30)))
    print("light bulb %d Watt %d ea for %d hours\n%.2f unit."
          % (gusfring1[3], 4, 5, float((gusfring1[3]*5/1000) * 30 * 4)))
    print("Refrigerator %d Watt %d ea for %d hours\n%.2f unit."
          % (gusfring1[4], 1, 24, float((gusfring1[4]*24/1000) * 30)))


main()
