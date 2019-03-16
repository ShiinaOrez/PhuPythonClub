if __name__ == "__main__":
    num = input("Number: ")
    if len(num) != 5:
        print("[Error 1]: Number's length must be 5!")
    else:
        flag = True
        for c in range(5):
            if num[c] != num[5-c-1]:
                flag = False
        print(flag)
