
import random

# 2. Create the subjects
subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Rahul Gandhi",
    "A Group of Monkeys",
    "A Mumbai Cat",
    "Prime Minister Modi",
    "A College Student",
    "A Software Engineer",
    "A Famous YouTuber"
]

# Create the actions
actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

# Create the places or things
places_or_thinks = [
   "at the Red Fort",
    "in a Mumbai local train",
    "a plate of samosas",
    "in space",
    "in a forest",
    "inside a temple",
    "during an IPL match",
    "at a college canteen",
    "inside a software company",
    "on the moon"
]

# 3. Start the headline loop
while True:

    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_think = random.choice(places_or_thinks)

    headline = f"BREAKING NEWS: {subject} {action} {places_or_think}"

    print("\n" + headline)

    user_input = input(
        "\nDo you want another headline? (Yes/No): "
    ).strip().lower()

    if user_input == "no":
        break

# Print goodbye message
print("\nThank you for using the Fake News Headline Generator project!")