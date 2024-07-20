import argparse
from database import add_user, authenticate_user, add_password, get_password
from encryption import generate_key

def main():
    parser = argparse.ArgumentParser(description="Password Manager")
    parser.add_argument('--generate-key', action='store_true', help="Generate a new encryption key")
    parser.add_argument('--add-user', help="Add a new user")
    parser.add_argument('--login', help="Login")
    parser.add_argument('--add-password', help="Add a password")
    parser.add_argument('--get-password', help="Get a password")
    args = parser.parse_args()

    if args.generate_key:
        generate_key()
        print("Encryption key generated.")
    elif args.add_user:
        username = input("Username: ")
        password = input("Password: ")
        add_user(username, password)
        print("User added.")
    elif args.login:
        username = input("Username: ")
        password = input("Password: ")
        if authenticate_user(username, password):
            print("Login successful.")
        else:
            print("Invalid credentials.")
    elif args.add_password:
        site = input("Site: ")
        username = input("Username: ")
        password = input("Password: ")
        add_password(site, username, password)
        print("Password added.")
    elif args.get_password:
        site = input("Site: ")
        username = input("Username: ")
        password = get_password(site, username)
        print(f"Password: {password}")

if __name__ == "__main__":
    main()
