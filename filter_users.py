import json
import logging

def filter_users_by_name(name: str) -> list[dict]:
    """Filter users by name from a JSON file and return the results."""
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            users = json.load(file)
    except FileNotFoundError:
        logging.error("users.json file not found.")
        return []
    except json.JSONDecodeError:
        logging.error("users.json is not a valid JSON file.")
        return []

    filtered_users = [user for user in users if user.get("name", "").lower() == name.lower()]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with name '{name}'")

    return filtered_users


def filter_by_age(age_to_filter: int) -> list[dict]:
    """Filter users by age from a JSON file and return the results."""
    try:
        with open("users.json", "r", encoding="utf-8") as fileobj1:
            all_users = json.load(fileobj1)  # loads directly from file
    except FileNotFoundError:
        logging.error("Error: users.json file not found.")
        return []
    except json.JSONDecodeError:
        logging.error("Error: users.json is not valid JSON.")
        return []

    # Filter by age
    filtered_users = [user for user in all_users if user.get("age") == age_to_filter]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with age {age_to_filter}")

    return filtered_users


def filter_by_email(email_to_filter) -> list[dict]:
    """Filter users by email from a JSON file and return the results."""
    with open("users.json", "r") as fileobj1:
        content = fileobj1.read().strip()
        if not content:
            print("Error: users.json is empty.")
            return []
        try:
            all_users = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON format: {e}")
            return []

    # Filter users by exact email match
    filtered_users = [user for user in all_users if user.get("email") == email_to_filter]

    return filtered_users


def print_to_console(users: list[dict]) -> None:
    """Print the list of users to the console."""
    if not users:
        print("No users found.")
        return

    for user in users:
        print(user)


if __name__ == "__main__":
    """Main function to prompt user for filtering criteria and display results."""
    filter_option = input("What would you like to filter by? (Currently, 'name', 'age', 'email' is supported): ").strip().lower()
    
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        print_to_console(filter_users_by_name(name_to_search))
    elif filter_option == "age":
        age_to_search = int(input("Enter age to filter users: ").strip())
        print_to_console(filter_by_age(age_to_search))
    elif filter_option == "email":
        email_to_search = input("Enter email to filter users: ").strip()
        print_to_console(filter_by_email(email_to_search))
    else:
        print("Filtering by that option is not yet supported.")
