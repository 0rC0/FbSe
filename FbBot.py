from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from dateutil import parser
from datetime import datetime
import json

# ToDo: Logger


class FbBot():

    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            j = json.load(f)
        self.first = j['first_name']
        self.last = j['last_name']
        self.profile = j['ff_profile_path']
        self.email = j['email']
        self.pw = j['pw']
        self.to_visit = j['pages_to_visit']
        self.data_file = j['data']
        self.data_seen = self.read_data_seen() if self.read_data_seen() else []
        self.b = webdriver.Firefox(self.profile)

    def __str__(self):
        return '{0} {1}'.format(str(self.first), str(self.last))

    def login(self):
        # ToDo: digit slowly mail/pw
        self.b.get('https://facebook.com')
        self.b.find_element_by_id('email').send_keys(self.email)
        self.b.find_element_by_id('pass').send_keys(self.pw)
        self.b.find_element_by_id('loginbutton').click()
        try:
            WebDriverWait(self.b, 10).until(ec.presence_of_element_located((
                By.XPATH, "//span[@class='_1vp5' and contains(text(), '{0}')]".format(self.first))))
        except BaseException as e:
            print(e, 'Login failed!')

    def logout(self):
        # ToDo: is the right page?
        try:
            WebDriverWait(self.b, 10).until(ec.presence_of_element_located((
                By.XPATH, "//span[@class='_1vp5' and contains(text(), '{0}')]".format(self.first))))
            self.settings_menu()
            logout = self.b.find_element_by_xpath("//*[contains(text(), 'Log Out')]")
            logout.click()
        except BaseException as e:
            print(e, 'Not logged in or not Facebook page!')

    def settings_menu(self):
        settings_menu = self.b.find_element_by_id('userNavigationLabel')
        settings_menu.click()

    def scroll_down(self, y, n=1):
        # A post is 680 - 900/1000 (depends on the comments showed)
        for i in range(n):
            self.b.execute_script('window.scrollBy(0, {0});'.format(y))

    def scroll_to_post(self, element):
        self.b.execute_script("arguments[0].scrollIntoView(true);", element)

    def go_to_page(self, page):
        # ToDo: this has to become a: search page name, click on the 1st search result
        self.b.get(page)

    def write_json(self, data):
        with open(self.data_file, 'w') as f:
            json.dump(data, f)

    def read_data_seen(self):
        with open(self.data_file, 'r') as f:
            return json.load(f)

    def not_read(self, news):
        """
        :return: True if something in the new data is not in read
        """
        return all([(b in self.data_seen) for b in news])

    def get_timestamps(self):
        posts = self.b.find_elements_by_xpath("//*[@class='_5pcr userContentWrapper']//div[@class='_6a _5u5j']")
        if not posts:
            self.scroll_down()
        times = [p.get_attribute('title') for p in posts[0].find_elements_by_xpath("//*[@class='_5pcq']/abbr")]
        timestamps = [datetime.timestamp(parser.parse(i)) for i in times]
        return timestamps

    def get_ids(self):
        # ToDo: parse ID
        # i.e 'feed_subtitle_247;171844246207985;2175324222526634;2175324222526634;1548655205:-4404398567812951017:5:0'
        # 171844246207985 = post_id, 2175324222526634 = photo
        posts = self.b.find_elements_by_xpath("//*[@class='_5pcr userContentWrapper']//div[@class='_6a _5u5j']")
        ids = [p.get_attribute('id').split(';')[1] for p in posts[0].find_element_by_xpath("//div[@class='_5pcp _5lel _2jyu _232_']")]
        return ids

    def read_timeline(self):
        """
        Main function, read timeline posts until everything is seen
        """
        # FixMe: Infinite Loop
        self.login()
        read = False
        old_posts = (len(self.data_seen) if self.data_seen else 0)
        while not read:
            news = self.get_timestamps()
            read = not self.not_read(news)
            self.data_seen = self.data_seen.append(news)
            self.scroll_down(900, n=2)
        self.write_json(self.data_seen)
        print('{0} new posts'.format(str(len(self.data_seen - old_posts))))
        self.logout()