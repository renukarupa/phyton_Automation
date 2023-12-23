string = input(" Enter a string: ")
string = string.lower()
str = reversed(string)
if list(string) == list(str):
    print("True, palindrom string")
else:
    print("Flase, Not a palindrom string")