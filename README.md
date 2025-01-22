
---

# Instagram OSINT Tool  

This project is a Python-based Open Source Intelligence (OSINT) tool designed to scrape and extract detailed information from Instagram profiles using the **instagrapi** library. The tool simplifies the process by providing a menu-driven interface for gathering intelligence, making it easy to use even for beginners.  

---

## Features  
- **Session-based Login**:  
  - Log in using saved sessions or new credentials.  
  - Handles OTP verification during login.  
- **Data Extraction**:  
  - Fetch basic user information, including bio, follower count, and more.  
  - Retrieve followings of the target account.  
- **Data Management**:  
  - Automatically saves extracted data in the `target_dump` folder for future reference.  

---

## Installation  

### Prerequisites  
- Python 3.8 or later  
- Required Python libraries:  
  - `instagrapi`  
  - `pickle`  
  - `json`  
  - `re`  

### Installation Steps  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/itz-danish/instagram-osint-tool.git  
   cd instagram-osint-tool  
   ```  
2. Install the required libraries:  
   ```bash  
   pip install instagrapi    
   ```

---

## Usage  

### Running the Tool  
1. Execute the main script:  
   ```bash  
   python main.py  
   ```  

2. **Login Process**:  
   - The tool allows you to log in using an existing session or by entering new credentials.  
   - Most of the time, Instagram sends an OTP for verification during login.  
   - It's recommended to use a temporary account to avoid potential bans, as excessive data scraping can result in account restrictions.  

3. **Targeting**:  
   - After logging in, enter the target's Instagram username and press Enter.  
   - A menu will appear allowing you to choose the desired information to gather:  
     - Basic user information  
     - Followings  
   - The tool will save the extracted data in the `target_dump` folder for later use.  

---

## Example Outputs  

### Basic Information (`target_dump/basic_info.json`)  
```json  
{  
    "User ID": "123456789",  
    "Username": "exampleuser",  
    "Full Name": "Example User",  
    "Bio": "Photographer | Traveler | Creator",  
    "Is private account": false,  
    "Public email": "exampleuser@gmail.com",  
    "Followers": 1500,  
    "Following": 200,  
    "Posts": 50,  
    "Profile Picture": "https://example.com/profile_pic.jpg",  
    "External URL": "https://example.com"  
}  
```  

### Followings List (`target_dump/followings.json`)  
```json  
[  
    {"username": "followed_user1", "full_name": "Followed User One"},  
    {"username": "followed_user2", "full_name": "Followed User Two"}  
]  
```  

---

## Limitations  
- **Rate Limits**: Instagram enforces strict rate limits; avoid excessive data requests to prevent bans.  
- **Account Restrictions**: Using personal accounts for scraping may lead to bans. It's safer to use temporary accounts.  
- **Private Profiles**: Cannot fetch data from private profiles unless you are following them.  

---

## License  
This project is open source and available under the [MIT License](LICENSE).  

---

## Disclaimer  
This tool is intended for educational and ethical purposes only. Misuse of this tool to scrape or collect data without the account owner's consent may violate Instagram’s terms of service and privacy policy. Use responsibly.  

---

## Creator  
Made with ❤️ by **Mohammad Danish**  
- [LinkedIn](https://www.linkedin.com/in/mohammad-danish-76570a24a/)  
- [Instagram](https://www.instagram.com/_itz_danish_/)

---

