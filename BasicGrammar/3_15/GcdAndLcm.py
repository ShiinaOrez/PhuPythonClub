import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

if __name__ == "__main__":
    x = int(input("x: "))
    y = int(input("y: "))
    print("GCD:", math.gcd(x, y))
    print("LCM:", lcm(x, y))
