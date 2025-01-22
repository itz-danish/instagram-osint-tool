import json
import os
import banner


def extract_followers(cl, target_username, target_folder, sys, limit):

        # Get the target user ID
        user_id = cl.user_id_from_username(target_username)

        # Fetch followers with the specified limit
        followers = cl.user_followers(user_id, amount=limit)

        # Extract usernames and full names
        followers_data = [{"username": user.username, "full_name": user.full_name} for user in followers.values()]

        os.system('cls' if sys.platform == 'win32' else 'clear')
        print(banner.head())

        print("\033[33mList of Followers:\033[0m\n")

        # Create a directory to save the JSON file
        output_dir = target_folder
        os.makedirs(output_dir, exist_ok=True)

        # Save data to a JSON file
        output_file = os.path.join(output_dir, "followers.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(followers_data, f, indent=4, ensure_ascii=False)

        # Print usernames and full names
        for follower in followers_data:
            print(f"Username: {follower['username']}, Full Name: {follower['full_name']}")

        print(f"\nData saved in: {output_file}")
        input("Press ENTER to continue...")
