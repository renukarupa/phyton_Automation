print("************  Total Vowel & Indiviual Vowels  ************")
input_string = input("Enter a String")
input_string = input_string.casefold()
vowels = "aeiou"
vowelsdata = {}.fromkeys(vowels,0)
totalvowelcount = 0
for character in input_string:
    if character in vowels:
        vowelsdata[character] += 1
        totalvowelcount += 1
print("Total vowels:", totalvowelcount)
for vowel in vowelsdata:
    print(vowels,"=>", vowelsdata[vowel])