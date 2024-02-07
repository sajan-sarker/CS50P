"""Checking edu email using regex"""
import re

def check_validation(email):
    
    pattern = r"^(\w+\.)?\w+@+(\w+\.)?\w+\.(edu|com|gov|net|org)$"
    
    if re.search(pattern, email, re.IGNORECASE):
        return "Valid!"
    else:
        return "Invalid!"

if __name__ == "__main__":
    email = input("Enter email account: ").strip()
    print(check_validation(email))
    #print(check_validation("sajanSarker@NoRThsouth.Edu"))