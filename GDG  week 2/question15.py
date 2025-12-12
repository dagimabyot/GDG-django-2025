sentence = input("Enter sentence: ").lower()
words = sentence.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)
