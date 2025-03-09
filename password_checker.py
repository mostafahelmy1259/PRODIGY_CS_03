password = input("Please enter your password: ")

def password_checker(password):
    score = 0
    criteria = [
        len(password) >= 8,
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(char in "!@#$%^&*()_+-=[{]}" for char in password)
    ]
    score = sum(criteria)  # Count the number of criteria met
    return score

score = password_checker(password)

if score == 5:
    print("Strong Password!")
elif score >= 3:
    print("Medium Strength Password!")
else:
    print("Weak Password!")
