valid_sales = []
with open("sales.txt", "r") as f:
    for line in f:
        try:
            valid_sales.append(int(line))
        except:
            pass  
print("Total sales =", sum(valid_sales))
