from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

# Load login information from the YAML file
with open('login_info.yaml', 'r') as file:
    conf = yaml.load(file, Loader=yaml.SafeLoader)

myFbEmail = conf['fb_user']['email']
myFbPassword = conf['fb_user']['password']

# Initialize the WebDriver
driver = webdriver.Chrome()

def login(url, usernameId, username, passwordId, password, submitButtonId):
    try:
        driver.get(url)
        driver.find_element(By.ID, usernameId).send_keys(username)
        driver.find_element(By.ID, passwordId).send_keys(password)
        driver.find_element(By.ID, submitButtonId).click()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

# Perform login
login("https://www.facebook.com/", "email", myFbEmail, "pass", myFbPassword, "loginbutton")
