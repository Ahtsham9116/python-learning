#========================================
# Character Frequency in Text
#========================================
sentence  = input("Enter a sentence:").lower().replace(" ","")
char_freq = {}
for char in sentence:
    if char.isalpha():  # Check if the character is an alphabet
        char_freq[char] = char_freq.get(char, 0) + 1
print("Character frequencies:")
for char, freq in char_freq.items():
    print(f"{char} => {freq}")