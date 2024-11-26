import re
def valid_email(email):
    if re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
        return True
    else:
        return False

Email=[ "email@gmail.com",
"user_name123@yahoo.com",
"john-doe@domain.org",
"plainaddress",
"@missingusername.com",
"username@.com",
]
for email in Email:
    print(f"{email}: {'Valid' if valid_email(email) else 'Invalid'}")

