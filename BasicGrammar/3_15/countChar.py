import re

if __name__ == "__main__":
    count = [0, 0, 0, 0]
    en_re = re.compile(r'[A-Za-z]')
    num_re = re.compile(r'[0-9]')
    string = input("Please input the string:")
    for char in string:
        if re.match(en_re, char):
            count[0] += 1
        elif re.match(num_re, char):
            count[1] += 1
        elif char == " ":
            count[2] += 1
        else:
            count[3] += 1

    print("En-Char:", count[0])
    print("Number :", count[1])
    print("Space  :", count[2])
    print("El-Char:", count[3])
