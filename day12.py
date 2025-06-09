import re

# Task: to validate gmail addresses using regex
def validate_gmail_address(email):
    pattern = r'^([a-zA-Z0-9._%+-]+)@gmail\.com$'
    if re.match(pattern, email):
        print(f"{email} is Valid.")
    else:
        print(f"{email} is Invalid.")

test_emails = [
    "user@gmail.com",
    "user@codebasics.com",
    "user@IDC.com"
]
for email in test_emails:
    validate_gmail_address(email)