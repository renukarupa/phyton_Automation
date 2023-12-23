string = input("Enter a String:")
vowels = "aeiouAEIOU"
result = " "
for character in string:
    if character not in vowels:
        result += character
print(result)