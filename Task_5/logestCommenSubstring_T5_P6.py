from difflib import SequenceMatcher
string_one = input(" Enter the string one : ")
string_two = input(" Enter the string two : ")
match = SequenceMatcher(None,string_one,string_two).find_longest_match(0,len(string_one),0,len(string_two))
print(match)
print(string_one[match.a:match.a+match.size])
print(string_two[match.b:match.b+match.size])
