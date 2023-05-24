fin = open("message.txt", "r").read()
cipher = [pow(int(i), -1, 41) for i in fin.split()]
for i in cipher:
    if i < 27:
        print(chr(i + 96), end="")
    elif i < 37:
        print(i - 27, end="")
    else:
        print("_", end="")
