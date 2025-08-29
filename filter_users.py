import json

def filter_users_by_name(name):
    """Filter users by name from a JSON file and print the results."""
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)

def filter_by_age(age_to_filter):
    """Filter users by age from a JSON file and print the results."""
    with open("users.json", "r") as fileobj1:
        content = fileobj1.read().strip()
        if not content:
            print("Error: users.json is empty.")
            return  # or raise an exception
        all_users = json.loads(content)

    # Continue with filtering...
    filtered_users = [user for user in all_users if user.get("age") == age_to_filter]
    print(filtered_users)


if __name__ == "__main__":
    """Main function to prompt user for filtering criteria and display results."""
    filter_option = input("What would you like to filter by? (Currently, 'name' and 'age' is supported): ").strip().lower()
    
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter age to filter users: ").strip())
        filter_by_age(age_to_search)
    else:
        print("Filtering by that option is not yet supported.")
