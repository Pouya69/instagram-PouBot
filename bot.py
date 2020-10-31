from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint, choice
import random
from selenium.webdriver.chrome.options import Options

used_usernames = []
used_agents = []  # Used User-Agents.


# Utility functions :
def generate_username():
    while True:
        result = ""
        names = ["bost", "pouya", "aali", "123", "00", "0", "thwe", "caat", "mortsal", "bagaby", "bbxcc", "dogdz", "tremsgg", "djap", "8y01", "232612", "lolp", "hotows", "kokacs", "lucasoa", "loranika", "ryadn", "cyan", "kokawp"]
        for i in range(3):
            result.join(choice(names))
        if result not in used_usernames:
            used_usernames.append(result)
            break
    return result


def random_user_agent():
    file = open("user_agents.txt", "r+")
    agent = random.choice(file.readlines())
    if agent not in used_agents:
        used_agents.append(agent)
        return agent
    file.close()


def finish():
    file = open("used_user_agents.txt", "w+")
    for agent in used_agents:
        file.write(agent)
    for username in used_usernames:
        file.write(username)
    file.close()


# Classes :
class InstaBot:
    # Initializing the values.
    signed_in = False
    username = ""
    email = ""
    password = ""
    full_name = ""
    code = ""
    hashtags = []
    prev_user_list = []
    new_followed = []
    tag = -1
    followed = 0
    likes = 0
    comments = 0

    def __init__(self, driver, email, full_name, password, hashtags):
        self.email = email
        self.full_name = full_name
        self.password = password
        self.hashtags = hashtags
        opts = Options()
        opts.add_argument("user-agent=" + random_user_agent())
        self.web_driver = webdriver.Chrome(executable_path=driver, chrome_options=opts)

    def create_insta_ac(self):
        insta_username = generate_username()
        id_email_phone = 'emailOrPhone'
        id_full_name = 'fullName'
        id_username = 'username'
        id_password = 'password'
        id_btn = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button'
        url = "https://www.instagram.com/"
        web_driver = self.web_driver
        sleep(2)
        web_driver.get(url)
        username_inst = web_driver.find_element_by_name(id_username)
        pass_inst = web_driver.find_element_by_name(id_password)
        em_inst = web_driver.find_element_by_name(id_email_phone)
        fullname_inst = web_driver.find_element_by_name(id_full_name)
        btn = web_driver.find_element_by_xpath(id_btn)
        em_inst.send_keys(self.email)
        fullname_inst.send_keys(self.full_name)
        username_inst.send_keys(insta_username)
        pass_inst.send_keys(self.password)
        btn.click()
        sleep(2)
        year = web_driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]')
        year.click()
        sleep(1)
        value = web_driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[36]')
        value.click()
        sleep(1)
        return True

    def login_insta(self):
        web_driver = self.web_driver
        sleep(2)
        web_driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)

        username = web_driver.find_element_by_name('username')
        username.send_keys(self.email)
        password = web_driver.find_element_by_name('password')
        password.send_keys(self.password)

        button_login = web_driver.find_element_by_css_selector(
            'body > div > section > main > div > article > div > div > div > form > div > button > div')
        button_login.click()
        sleep(3)

        not_now = web_driver.find_element_by_css_selector('body > div > div > div > div > div > button.aOOlW.HoLwm')
        not_now.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications
        return True

    def start_job(self):
        web_driver = self.web_driver
        for hashtag in self.hashtags:
            self.tag += 1
            web_driver.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.tag] + '/')
            sleep(5)
            first_thumbnail = web_driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

            first_thumbnail.click()
            sleep(randint(1, 2))
            try:
                for x in range(1, 200):
                    username = web_driver.find_element_by_xpath(
                        '/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text

                    if username not in self.prev_user_list:
                        # If we already follow, do not unfollow
                        if web_driver.find_element_by_xpath(
                                '/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                            web_driver.find_element_by_xpath(
                                '/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                            self.new_followed.append(username)
                            self.followed += 1

                            # Liking the picture
                            button_like = web_driver.find_element_by_xpath(
                                '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span')

                            button_like.click()
                            self.likes += 1
                            sleep(randint(18, 25))

                            # Comments and tracker
                            comm_prob = randint(1, 10)
                            print('{}_{}: {}'.format(hashtag, x, comm_prob))
                            if comm_prob > 7:
                                self.comments += 1
                                web_driver.find_element_by_xpath(
                                    '/html/body/div/div/div/div/article/div/section/span/button/span').click()
                                comment_box = web_driver.find_element_by_xpath(
                                    '/html/body/div/div/div/div/article/div/section/div/form/textarea')

                                if comm_prob < 7:
                                    comment_box.send_keys('dada eyval!')
                                    sleep(1)
                                elif 6 < comm_prob < 9:
                                    comment_box.send_keys('Nice work :)')
                                    sleep(1)
                                elif comm_prob == 9:
                                    comment_box.send_keys('Nice TRACK!!')
                                    sleep(1)
                                elif comm_prob == 10:
                                    comment_box.send_keys('So cool! :)')
                                    sleep(1)
                                # Enter to post comment
                                comment_box.send_keys(Keys.ENTER)
                                sleep(randint(22, 28))

                        # Next picture
                        web_driver.find_element_by_link_text('Next').click()
                        sleep(randint(25, 29))
                    else:
                        web_driver.find_element_by_link_text('Next').click()
                        sleep(randint(20, 26))
            # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
            except:
                continue

        for n in range(0, len(self.new_followed)):
            self.prev_user_list.append(self.new_followed[n])

        print(self.username + ' Liked {} photos.'.format(self.likes))
        print(self.username + ' Commented {} photos.'.format(self.comments))
        print(self.username + ' Followed {} new people.'.format(self.followed))
        return True

    def verify_account(self, code):
        web_driver = self.web_driver
        code_section = web_driver.find_element_by_name("email_confirmation_code")
        code_section.send_keys(code)
        sleep(1)
        button_confirm = web_driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[2]/button")
        button_confirm.click()
        return True


class Email:

    def __init__(self, path):
        opts = Options()
        opts.add_argument("user-agent=" + random_user_agent())
        self.web_driver = webdriver.Chrome(executable_path=path, chrome_options=opts)

    def get_new_email(self):
        url2 = "https://temp-mail.org/en/"
        web_driver = self.web_driver
        sleep(5)
        web_driver.get(url2)
        sleep(3)
        email_temp = web_driver.find_element_by_id('mail')
        final_mail = email_temp.text
        return final_mail

    def get_verification_code(self):
        web_driver = self.web_driver
        code = ""
        while True:
            try:
                sleep(5)
                text = web_driver.find_element_by_class_name("viewLink title-subject").text
                if text.contains("Instagram code"):
                    code = text.replace(" is your Instagram code", "")
                if not code == "":
                    break
                else:
                    continue
            except:
                continue
        return code


