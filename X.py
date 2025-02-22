import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Function to wait for manual login
def wait_for_x_login(driver):
    print("🔑 Please log in to X (Twitter) manually.")
    driver.get("https://x.com/i/flow/login")
    
    while True:
        if "https://x.com/home" in driver.current_url:
            print("✅ Logged in successfully! Proceeding with scraping...")
            return
        time.sleep(5)

# Function to extract text from an element
def extract_element(driver, xpath, default="N/A"):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element.text.strip() if element.text.strip() else default
    except:
        return default

# Function to scrape X (Twitter) profile details
def scrape_x_profile(profile_url, driver):
    driver.get(profile_url)
    time.sleep(5)  # Allow time for page to load

    username = extract_element(driver, "//span[contains(@class, 'css-1jxf684')]", "N/A")
    bio_text = extract_element(driver, "//div[@data-testid='UserDescription']", "No bio available")
    followers_count = extract_element(driver, "//a[contains(@href, '/followers')]//span[contains(@class, 'r-qvutc0')]", "0")
    following_count = extract_element(driver, "//a[contains(@href, '/following')]//span[contains(@class, 'r-qvutc0')]", "0")
    location = extract_element(driver, "//span[@data-testid='UserLocation']//span[contains(@class, 'css-1jxf684')]", "N/A")
    website = extract_element(driver, "//a[contains(@href, 'http')]", "N/A")  # Extract website link

    return [profile_url, username, bio_text, followers_count, following_count, location, website]

# Function to process profiles from Excel
def process_x_profiles(input_file, output_file):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    df = pd.read_excel(input_file)
    
    if 'Profile Link' not in df.columns:
        print("⚠️ Error: 'Profile Link' column not found in the Excel file!")
        return
    
    profile_urls = df['Profile Link'].dropna().tolist()
    
    wait_for_x_login(driver)  # Wait for manual login
    
    results = []
    for index, profile_url in enumerate(profile_urls):
        print(f"🔍 Scraping {index+1}/{len(profile_urls)}: {profile_url}")
        scraped_data = scrape_x_profile(profile_url, driver)
        results.append(scraped_data)
        time.sleep(5)  # Avoid detection
    
    driver.quit()

    # Save results
    columns = ['Profile Link', 'Username', 'Bio', 'Followers', 'Following', 'Location', 'Website']
    results_df = pd.DataFrame(results, columns=columns)
    results_df.to_excel(output_file, index=False)
    print(f"✅ Scraping completed! Results saved to {output_file}")

# Run the scraper
input_file = "C:\\Users\\ACER\\Downloads\\x_profiles.xlsx"
output_file = "C:\\Users\\ACER\\Downloads\\x_results.xlsx"

process_x_profiles(input_file, output_file)
