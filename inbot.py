import random
import time
import os
import datetime
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# display = Display(visible=0, size=[1920, 1080])
# display.start()


class inbot:

    def __init__(self, username, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username
        self.password = password
        self.selected_comment_text = []

    def countdown(self, count):
        timeout = count
        while timeout >= 0:
            min, sec = divmod(timeout, 60)
            timecounter = '{:02d}:{:02d}'.format(min, sec)
            print(f'Reiniciando script em {timecounter}', end='\r')
            time.sleep(1)
            timeout = timeout - 1

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/login/")
        time.sleep(10)
        driver.find_element(
            By.XPATH, value="//input[@name='username']").send_keys(self.username)
        driver.find_element(
            By.XPATH, value="//input[@name='password']").send_keys(self.password)
        time.sleep(5)
        driver.find_element(
            By.XPATH, value="//button[@type='submit']").click()
        time.sleep(5)

        if driver.title == 'Instagram':
            print(self.timelog() + 'Login ok.')
        else:
            print(self.timelog() + 'Falha de login!.')
            exit()

    def getprofile(self, profile):
        driver = self.driver
        driver.get(f'https://www.instagram.com/{profile}/')
        print(self.timelog() + f'Acessando perfil {profile}')
        time.sleep(10)

    def check_pics(self):
        link_list = []
        driver = self.driver
        pics = driver.find_elements(By.TAG_NAME, value='a')
        pined = driver.find_elements(
            By.CSS_SELECTOR, "svg[aria-label='Pinned post icon']")

        for pic in pics:
            link = pic.get_attribute('href')
            search_links = link.find('/p/')
            if search_links != -1:
                link_list.append(link)
                print(link)

        time.sleep(5)
        driver.get(link_list[0 + len(pined)])
        time.sleep(5)

    def check_commented(self):

        number_of_comments = []
        driver = self.driver
        time.sleep(5)

        comments = driver.find_elements(By.TAG_NAME, value='a')
        for comment in comments:
            link_profile = comment.get_attribute('href')
            get_profile = link_profile.find('/' + self.username + '/')
            if get_profile != -1:
                number_of_comments.append(link_profile)

        if len(number_of_comments) > 1:
            print(self.timelog() + 'Post já tem comentário!')
        else:
            print(self.timelog() + 'Post não tem comentário!')
            print(self.timelog() + 'Iniciando comentário')
            self.comment()

    @staticmethod
    def digitando_como_humano(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.uniform(0.1, 0.5))

    def comment(self):
        comment_text = ['comment 1', 'comment 2',
                        'comment 3', 'comment 4', 'comment 5']
        driver = self.driver
        time.sleep(5)
        while True:
            comment_in = random.choice(comment_text)
            print(self.timelog(
            ) + f'Selecionando comentário, tamanho do array {len(self.selected_comment_text)}')
            if comment_in not in self.selected_comment_text:
                break
        self.selected_comment_text.append(comment_in)
        if len(self.selected_comment_text) == len(comment_in):
            self.selected_comment_text.clear()
            print(self.timelog() + 'Reinicianto array de comentários')
        driver.find_element(
            By.CSS_SELECTOR, value="[placeholder='Add a comment…']").click()
        comment_box = driver.find_element(
            By.CSS_SELECTOR, value="[placeholder='Add a comment…']")
        self.digitando_como_humano(comment_in, comment_box)
        comment_box.send_keys(Keys.RETURN)
        print(self.timelog() + 'Comentário Ok!')
        time.sleep(5)

    def timelog(self):
        now = datetime.datetime.now()
        data_format = now.strftime("%Y-%m-%d %H:%M:%S -- ")
        return data_format


profiles = ['profiles', 'profile1', 'profile2', 'profile3', 'profile4...']


def main_loop():
    start = inbot("username", 'password')
    start.login()
    while True:
        for profile in profiles:
            start.getprofile(profile)
            start.check_pics()
            start.check_commented()

        start.countdown(900)


main_loop()
