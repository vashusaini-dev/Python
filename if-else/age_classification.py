def main():

    # Prompt the user to enter their age and convert input to integer
    age = int(input("Enter your age: "))

    # Determine the age category using if-elif-else statements
    if age < 13:
        print("You are a child.")  # Child: age less than 13
    elif age < 20:
        print("You are a teenager.")  # Teenager: age 13 to 19
    elif age < 60:
        print("You are an adult.")  # Adult: age 20 to 59
    else:
        print("You are a senior citizen.")  # Senior citizen: age 60 and above

# Entry point guard: ensures main() runs only when script is executed directly
if __name__ == "__main__":
    main()
