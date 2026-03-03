# 1️⃣ Basic if statement

temperature = 35

if temperature > 30:
    print("It is a hot day.")

print("Temperature check complete.\n")


# 2️⃣ if–else example

age = 17

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print()


# 3️⃣ if–elif–else example

marks = 78

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

print()


# 4️⃣ Logical operators example

username = "Ashfaq"
logged_in = True

if username == "Ashfaq" and logged_in:
    print("Welcome Ashfaq! Access granted.")

if username == "Admin" or username == "Ashfaq":
    print("You have special access.")

is_banned = False

if not is_banned:
    print("User account is active.")