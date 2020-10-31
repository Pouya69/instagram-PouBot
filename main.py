#!/usr/bin/env python3
from bot import Email, InstaBot, finish

# This project is a simple tool made by myself to show the way that selenium and Python web scarping works.
# The library is the bot.py file. Do not edit it unless you know what are you doing!
# We use Chrome Selenium.
# Thanks to my friend Nima for having fun with him and completing the project with him.

if __name__ == '__main__':
    chrome_path = r'chromedriver'
    hashtags = ["my", "hashtags"]  # Your hashtags that your Instagram posts have.
    password = "PasswordIsDjango@123"  # Your password for the bots.
    fullname = "Dj Cat"  # The bots' full name.

    email_page = Email(chrome_path)  # Initializing the Email object
    email = email_page.get_new_email()

    bot = InstaBot(chrome_path, email, fullname, password, hashtags)  # Initializing the Instagram Bot object
    status = bot.create_insta_ac()  # Creating a new Instagram account
    
    code = email_page.get_verification_code()
    bot.verify_account(code)
    bot.login_insta()

    bot.start_job()
    finish()
