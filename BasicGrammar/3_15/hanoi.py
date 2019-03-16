def hanoiStep(n, fro, to, aux):
    if n == 1:
        print("Move disk 1 from", fro, "to", to)
        return
    hanoiStep(n-1, fro, aux, to)
    print("Move disk", n, "from", fro, "to", to)
    hanoiStep(n-1, aux, to, fro)

def hanoi(n):
    hanoiStep(n, "A", "C", "B")

if __name__ == "__main__":
    n = int(input("Number: "))
    hanoi(n)
