import banner
import os
import json
import re


def extract_posts_data(cl, target_username, target_folder, sys):
    # Get the user ID of the target profile
    user_id = cl.user_id_from_username(target_username)

    # Fetch all posts of the target user
    posts = cl.user_medias(user_id, amount=0)  # amount=0 fetches all posts

    # Extract post data
    post_data = []
    for post in posts:
        post_url = f"https://www.instagram.com/p/{post.code}/"  # Construct post URL
        post_info = {
            "Post ID": post.id,
            #replacing multiple consecutive spaces into single space and replacing new line by a space
            "Caption": re.sub(r'\s+', ' ', post.caption_text.replace("\n"," ")).strip() or "No Caption",
            "Likes": post.like_count,
            "Comments": post.comment_count,
            "Post URL": post_url,
            "Media Type": {
                1: "Photo",
                2: "Video",
                8: "Album"
            }.get(post.media_type, "Unknown"),
            "Posted On": str(post.taken_at),
        }
        post_data.append(post_info)

    # Clear the terminal and show banner
    os.system('cls' if sys.platform == 'win32' else 'clear')
    print(banner.head())

    # Print posts data in the desired format
    print("\nPosts Data:\n")
    for i, post in enumerate(post_data, start=1):
        print(f"{i}.")
        for key, value in post.items():
            print(f"    {key}: {value}")
        print("\n--- X --- X --- X --- X ---\n")  # Add a blank line between posts

    # Save data to a JSON file
    output_dir = target_folder
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "posts.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(post_data, f, indent=4, ensure_ascii=False)

    print(f"\nData saved in: {output_file}")
    input("\nPress ENTER to continue...")
