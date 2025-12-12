try:
    with open("message.txt", "r") as f:
        print(f.read().upper())
except:
    print("File not found")
