import json
import os
import banner

def extract_basic_data(cl, target_username, target_folder, sys):
    # Using UTF-8 encoding to handle printing emojis
    sys.stdout.reconfigure(encoding="utf-8")

    try:
        # Fetch user information
        user_info = cl.user_info_by_username(target_username)

        # Extract only the required elements
        user_info_dict = {
            "User ID": user_info.pk,
            "Username": user_info.username,
            "Full Name": user_info.full_name,
            "Bio": user_info.biography,
            "Is private account": user_info.is_private,
            "Public email": user_info.public_email,
            "Followers": user_info.follower_count,
            "Following": user_info.following_count,
            "Posts": user_info.media_count,
            "Profile Picture": str(user_info.profile_pic_url_hd),
            "External URL": user_info.external_url,
        }

        os.system('cls' if sys.platform == 'win32' else 'clear')
        print(banner.head())

        # Print the extracted information
        print("\033[33mBasic User Information:\033[0m\n")
        for key, value in user_info_dict.items():
            print(f"    {key}: {value}")

        # Define the output directory and file path
        output_file = os.path.join(target_folder, "basic_info.json")

        # Ensure the directory exists
        os.makedirs(target_folder, exist_ok=True)

        # Save the user info dictionary to a JSON file
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(user_info_dict, json_file, ensure_ascii=False, indent=4)

        print(f"\n >>> User information saved to {output_file}")
        input("\033[36mPress ENTER to continue...\033[0m")



    #to haandle errors
    except Exception as e:
        print("\033[31mError:\033[0m", e)
        sys.exit()
