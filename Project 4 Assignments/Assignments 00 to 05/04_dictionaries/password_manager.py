import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    if email in stored_logins:
        stored_hash = stored_logins[email]
        password_hash = hash_password(password_to_check)
        return stored_hash == password_hash
    return False

if __name__ == "__main__":
    stored_logins = {
        "user1@example.com": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        "user2@example.com": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
    }
    
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.") 