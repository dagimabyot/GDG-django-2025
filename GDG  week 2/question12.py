total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        try:
            total += int(line)
        except:
            pass
print("Sum =", total)
