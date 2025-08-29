import random

def main():
    
    # Prompt the user for their age
    age = int(input("Enter your age: "))

    # List of days of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Randomly select a day
    day = random.choice(days)
    print(f"Today is {day}.")

    # Determine base ticket price based on age using a conditional expression
    price = 12 if age >= 18 else 8

    # Apply Wednesday discount if applicable
    if day == "Wednesday":
        price -= 2  # Subtract $2
        print("It's Wednesday! You get a $2 discount.")
        print(f"Your ticket price is: ${price}")
    else:
        print(f"Your ticket price is: ${price}")

# Entry-point guard: runs main() only if script is executed directly
if __name__ == "__main__":
    main()
