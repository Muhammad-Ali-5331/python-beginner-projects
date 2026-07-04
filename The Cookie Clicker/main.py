import time  # For handling time-based actions
from selenium import webdriver  # For automating browser actions
from selenium.webdriver.common.by import By  # For locating elements in the DOM
from selenium.webdriver.common.keys import Keys  # For interacting with keyboard actions

# -------------------------- Browser Setup -------------------------- #

# Initialize the Chrome WebDriver to control the browser
driver = webdriver.Chrome()

# Open the Cookie Clicker game website
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# -------------------------- Locating Elements -------------------------- #

# Find the cookie element that will be clicked repeatedly
cookie = driver.find_element(by=By.ID, value="cookie")

# -------------------------- Timer Setup -------------------------- #

# Timeout for stopping the game after 5 minutes
timeout = time.time() + 60 * 5

# Set a separate timer for making purchases, initially 1 minute from the start
time_for_buying = time.time() + 60 * 1

# -------------------------- Game Automation Loop -------------------------- #

# Infinite loop to automate clicking and purchasing
while True:
    # Simulate a click on the cookie
    cookie.click()

    # Check if the timeout period (5 minutes) has been reached
    if time.time() > timeout:
        # Fetch the cookies-per-second (CPS) value
        cookies_per_second = driver.find_element(by=By.ID, value="cps").text
        print(cookies_per_second)  # Print the final CPS value
        break  # Exit the loop and stop the game

    else:
        # Try block to handle purchasing items from the store
        try:
            # Fetch the current amount of cookies available (money) and convert it to an integer
            my_money = int(driver.find_element(by=By.ID, value="money").text.replace(',', ''))

            # Find all items in the store, represented by <b> elements inside #store
            store = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")

            # -------------------------- Processing Store Items -------------------------- #

            # Extract the name and price of each item
            # Method 1: Use list comprehension and split the text at ' - '
            # items_list = [item.text.split(' - ') for item in store]; items_list.pop()

            # Method 2: Exclude empty text elements and split the text to separate names and prices
            items_list = [item.text.split(' - ') for item in store if item.text]

            # Separate item names and prices into separate lists
            items_names = [item[0] for item in items_list]  # Extract the names
            items_prices = [int(item[1].replace(',', '')) for item in items_list]  # Extract and clean prices

            # -------------------------- Purchasing Items -------------------------- #

            # Iterate over item prices in descending order to buy the most expensive affordable item
            for item_price in items_prices[::-1]:  # Start with the most expensive item
                if my_money >= item_price:  # Check if enough cookies are available
                    # Find the corresponding item button using its ID (e.g., "buyCursor")
                    item_to_buy = driver.find_element(by=By.ID, value=f"buy{items_names[items_prices.index(item_price)]}")

                    # Simulate a click to purchase the item
                    item_to_buy.click()

            # Reset the buying timer to check again after 5 seconds
            time_for_buying = time.time() + 5

        except Exception as e:
            # Handle any errors that occur during the purchasing process
            print("Error Caused while Purchasing Item", e)