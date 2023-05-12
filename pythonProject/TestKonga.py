import os
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# initialize webdriver
os.environ['PATH'] += r"C:\seleniumdrivers"

driver = webdriver.Chrome()

# Open URL(https://www.konga.com/) and maximize window
driver.maximize_window()
driver.get("https://www.konga.com/")

if "https://www.konga.com/" in driver.current_url:
    # Pass
    print("Correct webpage")

else:
    # Fail
    print("Incorrect Webpage")

driver.implicitly_wait(20)

# To click on Login/Signup
logIn_SignUp = driver.find_element(By.XPATH, '//*[@id="nav-bar-fix"]/div[1]/div/div/div[4]/a')
logIn_SignUp.click()
driver.implicitly_wait(10)

# To Input the Username and Password data
username_input = driver.find_element(By.ID, "username").send_keys("etunnecharles@gmail.com")

password_input = driver.find_element(By.ID, "password").send_keys("123naija")

# To click on the login button
Login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[4]/section/section/aside/div[2]/div/form/div[3]/button')
Login_button.click()
driver.implicitly_wait(10)

# To click on Computer and Accessories button
computer_category = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Computers and Accessories')]"))
)
# execute the JavaScript code to click the element
driver.execute_script("arguments[0].click();", computer_category)
driver.implicitly_wait(10)

# To click on Laptops
Laptop = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/section[3]/section/div/section/div[2]/div[2]/ul/li[3]/a/label/span')))
driver.execute_script("arguments[0].click();", Laptop)
driver.implicitly_wait(20)

# Click on macbook
macbook_category_radio_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/section[3]/section/div/section/div[2]/div[2]/ul/li[3]/a/ul')))
macbook_category_radio_button[0].click()
driver.implicitly_wait(20)

# add item to cart
add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/section[3]/section/section/section/section/ul/li[1]/div/div/div[2]/form/div[3]/button')

# Select Address
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Proceed to Checkout')]")))
proceed_to_checkout_button = driver.find_element(By.XPATH, "//a[contains(text(),'Proceed to Checkout')]")
proceed_to_checkout_button.click()

# Continue to make payment
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue to payment')]")))
continue_to_payment_button = driver.find_element(By.XPATH, "//button[contains(text(),'Continue to payment')]")
continue_to_payment_button.click()

# Select a Card Payment Method
card_payment_button = driver.find_element(By.XPATH, "//label[contains(text(),'Card Payment')]")
card_payment_button.click()

# Input invalid card details
card_number_field = driver.find_element(By.XPATH, "//input[@placeholder='1234 5678 9012 3456']")
card_number_field.send_keys("123456781234567")

# Submit the payment form
submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit Payment')]")
submit_button.click()

# Print Out the error message: Invalid card number
error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
print(error_message.text)

# Close the iFrame that displays the input card Modal
close_button = driver.find_element(By.XPATH, "//button[contains(text(),'Close')]")
close_button.click()

# Quit the browser
driver.quit()
