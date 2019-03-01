def factorial(n):
    f = 1
    for i in range(n+1):
        if i != 0:
            f *= i
    return f

if __name__ == "__main__":
    n = int(input("Input the N: "))
    sum = 0
    for i in range(n+1):
        if i != 0:
            sum += factorial(i)
    print(sum)
