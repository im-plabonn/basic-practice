word = input("Enter or paste texts here: ")
count = 0
for i in word:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i=="u"):
        count+=1
print(f"Totel {count} vowels found in you text!")
        