import re

phone_regex = (r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
phone_number = "(123) 456-7890"
match = re.search(phone_regex, phone_number)

print(match)