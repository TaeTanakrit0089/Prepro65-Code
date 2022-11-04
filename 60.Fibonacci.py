"""I see a little silhouetto of a man"""
def main(mercury):
    """Scaramouch, Scaramouch, will you do the Fandango"""
    if mercury == 0:
        return 0
    elif mercury == 1:
        return 1
    else:
        return main(mercury-1) + main(mercury-2)

print(main(int(input())))
