if __name__ == "__main__":
    with open("text1.txt", "r", encoding="UTF-8") as r:
        with open("text2.txt", "w", encoding="UTF-8") as w:
            i = 1
            for line in r.readlines():
                w.write(str(i) + line)
                i += 1
    print("OK")
