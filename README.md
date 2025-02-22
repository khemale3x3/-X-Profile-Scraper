# -X-Profile-Scraper
This script automates the process of scraping Twitter (X) profile details from an Excel file containing profile links. It extracts information such as username, bio, followers, following, location, and website.

Steps of the Twitter (X) Profile Scraper
1️⃣ Set Up the WebDriver
Install and configure Selenium WebDriver using webdriver_manager.
Open a Chrome browser with specific options.
2️⃣ Prompt for Manual Login
Directs the user to manually log into X (Twitter).
Waits until the user reaches the homepage (https://x.com/home).
3️⃣ Load Profiles from Excel
Reads an Excel file containing profile URLs.
Checks if the Profile Link column exists.
4️⃣ Scrape Profile Data
Opens each profile URL in the browser.
Extracts username, bio, followers, following, location, and website.
Uses WebDriverWait to ensure elements are loaded.
5️⃣ Store Results in Excel
Saves the scraped data in a new Excel file.
6️⃣ Close the Browser
Exits the WebDriver after scraping is complete.
✅ Scraping process completed! 🚀


Why is This Useful?
Automates data collection from Twitter.
Extracts user details without API restrictions.
Saves data in an Excel file for easy access.
Avoids bot detection with manual login and delays.
