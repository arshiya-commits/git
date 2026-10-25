
# Student Login Feature

students = {
    "arshi123": "pass123",
    "student001": "welcome123"
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in students and students[username] == password:
    print("Login successful! Welcome,", username)
else:
    print("Invalid username or password.")
