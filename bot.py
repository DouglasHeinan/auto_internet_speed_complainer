from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        service = Service(r"C:\Users\dough\OneDrive\Documents\chromedriver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        button.click()
        time.sleep(45)
        down_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data .download-speed").text
        up_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data .upload-speed").text
        return up_speed, down_speed

    def tweet_at_provider(self, password, email, username, tweet_text):
        self.driver.get("https://twitter.com/home")
        time.sleep(1)
        email_input = self.driver.find_element(By.CSS_SELECTOR, "input")
        time.sleep(1)
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(1)
        username_input = self.driver.find_element(By.CSS_SELECTOR, "input")
        username_input.send_keys(username)
        username_input.send_keys(Keys.ENTER)
        time.sleep(1)
        password_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input")
        time.sleep(1)
        password_inputs[1].send_keys(password)
        password_inputs[1].send_keys(Keys.ENTER)
        time.sleep(1)
        tweet = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-ltr")
        tweet.send_keys(tweet_text)
        tweet_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_btn.click()
        self.driver.close()
        self.driver.quit()
