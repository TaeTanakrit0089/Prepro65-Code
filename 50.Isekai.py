"""Welcome To Los Pollos Hermanos"""
import math

def my_main():
    """Welcome To Los Pollos Hermanos"""
    gusx1 = float(input())
    gusy1 = float(input())
    distance = float(input())
    degree = int(input())
    hectora = math.sin(math.radians(degree))*distance
    hectorb = math.cos(math.radians(degree))*distance
    saulx2 = hectorb + gusx1
    sauly2 = hectora + gusy1
    print("%.2f" % saulx2)
    print("%.2f" % sauly2)

my_main()
