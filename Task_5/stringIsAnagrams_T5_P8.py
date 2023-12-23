first_string = input("Enter the String :")
second_string = input("Enter the string :")
if len(first_string) != len(second_string):
    print("Not Anagrams")
else:
    if sorted(first_string) == sorted(second_string):
        print("True, String are Anagrams")
    else:
        print("Flase, String are not Anagrams")
