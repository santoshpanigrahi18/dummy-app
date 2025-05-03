def main():
    print("Welcome to the Dummy App Form")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    message = input("Enter your message: ")

    print("\n--- Form Submission Received ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    print("\nThank you for submitting the form!")

if __name__ == "__main__":
    main()

