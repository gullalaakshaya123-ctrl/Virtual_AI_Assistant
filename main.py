
from src.assistant_features import (
    get_user_name,
    show_date,
    show_time,
    tell_joke,
    motivational_quote,
    random_fact,
    number_guessing_game,
    show_help,
    activity_recommendation,
    perceptron_demo
)


def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", num1 + num2)

        elif operator == "-":
            print("Result:", num1 - num2)

        elif operator == "*":
            print("Result:", num1 * num2)

        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print("Result:", num1 / num2)

        else:
            print("Invalid operator!")

    except ValueError:
        print("Please enter valid numbers!")


def main():
    print("=" * 40)
    print("       VIRTUAL AI ASSISTANT")
    print("=" * 40)

    name = get_user_name()

    while True:
        print(f"\nHello {name}! How can I help you?")
        print("\n1. Calculator")
        print("2. Date")
        print("3. Time")
        print("4. Joke")
        print("5. Motivational Quote")
        print("6. Random Fact")
        print("7. Number Guessing Game")
        print("8. Help")
        print("9. AI Activity Recommendation")
        print("10. ML Perceptron Demo")
        print("11. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            calculator()

        elif choice == "2":
            show_date()

        elif choice == "3":
            show_time()

        elif choice == "4":
            tell_joke()

        elif choice == "5":
            motivational_quote()

        elif choice == "6":
            random_fact()

        elif choice == "7":
            number_guessing_game()

        elif choice == "8":
            show_help()

        elif choice == "9":
            activity_recommendation()

        elif choice == "10":
            perceptron_demo()

        elif choice == "11":
            print(f"Goodbye {name}! Have a wonderful day!")
            break

        else:
            print("Sorry, I didn't understand that command. Please try again.")


if __name__ == "__main__":
    main()
