if __name__ == "__main__":
    with open("歌词.txt", "r+", encoding="UTF-8") as f:
        old = f.read()
        f.seek(0)
        f.write("千千阙歌\n陈慧娴\n")
        f.write(old)
    with open("歌词.txt", "a", encoding="UTF-8") as f:
        f.write("\n由环球唱片发行")
    with open("歌词.txt", "r", encoding="UTF-8") as f:
        for line in f.readlines():
            print(line)
    print("Ok")
