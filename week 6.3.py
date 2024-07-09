import re

def is_valid_phone(phone):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    return pattern.match(phone) is not None

def is_valid_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return pattern.match(email) is not None

def get_valid_phone():[h]
    while True:
        phone = input("Enter your phone number: ")
        if is_valid_phone(phone):
            return phone
        else:
            print("Invalid phone number. Please try again.")

def get_valid_email():
    while True:
        email = input("Enter your email ID: ")
        if is_valid_email(email):
            return email
        else:
            print("Invalid email ID. Please try again.")

phone = get_valid_phone()
email = get_valid_email()

print(f"Valid phone number: {phone}")
print(f"Valid email ID: {email}")
