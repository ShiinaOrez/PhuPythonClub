ExchangeRate = 0.15

if __name__ == "__main__":
    str = input("Input String: ")
    if str.startswith("RMB"):
        slice = str.split("RMB")
        num = float(slice[1])
        res = num*ExchangeRate
        print("USD %.2f" % res)
    if str.startswith("USD"):
        slice = str.split("USD")
        num = float(slice[1])
        res = num/ExchangeRate
        print("RMB %.2f" % res)
