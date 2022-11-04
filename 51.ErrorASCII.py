"""Welcome To Los Pollos Hermanos"""


def main():
    """Welcome To Los Pollos Hermanos"""
    gusfring1 = input()
    gusfirst = gusfring1.find('"')
    guslast = gusfring1.rfind('"')
    if(gusfirst == -1) and (guslast == -1):
        print("No error")
    else:
        gusnum = int(gusfring1[gusfirst+1:guslast])
        gusfinal = chr(int(gusnum))
        print(gusfring1[:gusfirst] + gusfinal + gusfring1[guslast+1:])


main()
