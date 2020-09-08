from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)

        time.sleep(4)

    def searchHashtag(self, hashtag):
        bot = self.bot

        bot.get('https://www.instagram.com/explore/tags/' + hashtag)
        time.sleep(2)


    def likePhotos(self, amount):
        bot = self.bot

        bot.find_element_by_class_name('_9AhH0').click()

        i = 1
        while i <= amount:
            time.sleep(2)
            bot.find_element_by_class_name('wpO6b').click()
            time.sleep(2)
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            time.sleep(2)

            i += 1
        bot.get('https://instagram.com/' + self.username)


insta = InstagramBot('YOUR_USERNAME', 'YOUR_PASSWORD')    #write your username and password here
insta.login()
insta.searchHashtag('HASHTAG YOU WANNA SEARCH')           #write the name of hashtag you wanna search
insta.likePhotos(NO. OF PHOTOS TO LIKE)                   #Here write the no. of photos you wanna like
