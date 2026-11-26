import random
from datetime import datetime


def get_user_name():
    name = input("What is your name? ").strip()

    if name:
        print(f"Nice to meet you, {name}!")
        return name

    return "User"


def show_date():
    print("Today's date:", datetime.now().strftime("%d-%m-%Y"))


def show_time():
    print("Current time:", datetime.now().strftime("%I:%M:%S %p"))


def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer go to the doctor? It had a virus!",
        "Why was the Python programmer confused? Because he couldn't find his snake!",
        "Why do computers never get tired? They have lots of RAM!",
        "Why did the developer go broke? Because he used up all his cache!"
    ]
    print(random.choice(jokes))


def motivational_quote():
    quotes = [
        "Believe in yourself and never stop learning.",
        "Success starts with small steps.",
        "Dream big and work hard.",
        "Every day is a new opportunity.",
        "Don't give up. Great things take time."
    ]
    print(random.choice(quotes))


def random_fact():
    facts = [
        "Python was named after Monty Python, not the snake.",
        "The first computer programmer was Ada Lovelace.",
        "The Internet and the World Wide Web are not the same.",
        "A byte contains 8 bits.",
        "Artificial Intelligence helps computers perform intelligent tasks."
    ]
    print(random.choice(facts))


def number_guessing_game():
    number = random.randint(1, 100)
    print("\nI selected a number between 1 and 100!")

    while True:
        try:
            guess = int(input("Guess the number: "))

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print("Correct! You guessed it!")
                break

        except ValueError:
            print("Please enter a valid number.")


def show_help():
    print("\n--- HELP ---")
    print("1. Calculator - Basic arithmetic")
    print("2. Date - Today's date")
    print("3. Time - Current time")
    print("4. Joke - Random joke")
    print("5. Quote - Motivational quote")
    print("6. Fact - Random fact")
    print("7. Game - Number guessing")
    print("8. Help - Available features")
    print("9. AI - Activity recommendation")
    print("10. ML - Perceptron demo")
    print("11. Exit - Close assistant")


def activity_recommendation():
    print("\n--- AI ACTIVITY RECOMMENDATION ---")
    mood = input(
        "How are you feeling (happy, tired, bored, stressed)? "
    ).lower().strip()

    if mood == "happy":
        print("Recommendation: Enjoy a fun activity or learn something new!")
    elif mood == "tired":
        print("Recommendation: Take a short rest and drink some water.")
    elif mood == "bored":
        print("Recommendation: Try reading, drawing or playing a game!")
    elif mood == "stressed":
        print("Recommendation: Take deep breaths and listen to relaxing music.")
    else:
        print("Recommendation: Take a break and choose an activity you enjoy!")


def perceptron_demo():
    print("\n--- SIMPLE PERCEPTRON DEMO ---")

    inputs = [1, 0]
    weights = [0.5, -0.4]
    bias = 0.1

    weighted_sum = sum(
        i * w for i, w in zip(inputs, weights)
    ) + bias

    output = 1 if weighted_sum >= 0 else 0

    print("Inputs:", inputs)
    print("Weights:", weights)
    print("Bias:", bias)
    print("Weighted Sum:", weighted_sum)
    print("Perceptron Output:", output)