import random

# Data
people = [
    {"name": "John", "profession": "Engineer", "followers": 1000},
    {"name": "Peter", "profession": "Doctor", "followers": 2000},
    {"name": "Rahul", "profession": "Teacher", "followers": 3000},
    {"name": "Rohan", "profession": "Lawyer", "followers": 4000},
    {"name": "Sabrina", "profession": "Actor", "followers": 500},
]

def get_random_person(exclude=None):
    """Returns a random person from the list, excluding the given person."""
    while True:
        person = random.choice(people)
        if person != exclude:
            return person

def display_options(person1, person2):
    """Displays the two options to the user."""
    print("\nWho do you think has more followers?")
    print(f"Option 1: {person1['name']} ({person1['profession']})")
    print(f"Option 2: {person2['name']} ({person2['profession']})")

def higher_lower_game():
    """Main function to run the Higher or Lower game."""
    score = 0
    print("Welcome to the Higher or Lower Game!")
    
    # Initial two options
    person1 = get_random_person()
    person2 = get_random_person(exclude=person1)
    
    while True:
        # Display options
        display_options(person1, person2)
        
        # Get user input
        user_choice = input("Enter your choice (1 or 2): ").strip()
        
        if user_choice not in ['1', '2']:
            print("Invalid input. Please enter '1' or '2'.")
            continue

        # Determine if the user's choice is correct
        chosen_person = person1 if user_choice == '1' else person2
        other_person = person2 if user_choice == '1' else person1

        if chosen_person["followers"] > other_person["followers"]:
            score += 1
            print(f"Correct! {chosen_person['name']} has more followers. Your score: {score}")
            # Update options: Winner stays, compare with a new person
            person1 = chosen_person
            person2 = get_random_person(exclude=person1)
        else:
            print(f"Wrong! {chosen_person['name']} has fewer followers than {other_person['name']}.")
            print(f"Game Over! Your final score: {score}")
            break

# Start the game
if __name__ == "__main__":
    higher_lower_game()
