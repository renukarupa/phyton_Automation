import re
def validate_phone_number(regex, mobile_number):
    match = re.search(regex, mobile_number)
    if match:
        return True
    return False

pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

test_phone_numbers = [ "+880 20 1234 5678", "02012345678", "+88001054 694200"]

for number in test_phone_numbers:
    print(f"{number}: {validate_phone_number(pattern, number)}")
