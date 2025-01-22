import json
import os
import banner


def extract_followings(cl, target_username, target_folder, sys, limit):
    # Using UTF-8 encoding to handle printing emojis
    sys.stdout.reconfigure(encoding="utf-8")

    # Fetch the user ID of the target profile
    user_id = cl.user_id_from_username(target_username)

    # Fetch followings with the limit
    followings = cl.user_following(user_id, amount=limit)

    followings_data = [{"username": user.username, "full_name": user.full_name} for user in followings.values()]

    os.system('cls' if sys.platform == 'win32' else 'clear')
    print(banner.head())

    print("\033[33mList of Followings:\033[0m\n")
    
    # Create a directory to save the JSON file
    output_dir = target_folder
    os.makedirs(output_dir, exist_ok=True)

    # Save data to a JSON file
    output_file = os.path.join(output_dir, "followings.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(followings_data, f, indent=4, ensure_ascii=False)

    # Print usernames and full names
    for follower in followings_data:
        print(f"Username: {follower['username']}, Full Name: {follower['full_name']}")

    print(f"\nData saved in: {output_file}")
    input("Press ENTER to continue...")
