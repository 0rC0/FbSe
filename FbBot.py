from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from dateutil import parser
from datetime import datetime
import json

'''
Example JSON config file
{
"email": "email",
"pw": "password",
"ff_profile_path": "path",
"pages_to_visit": ["url1",
                   "url2",
                   "url3"],
"data": "path file.json"
}
'''


class FbBot():

    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            j = json.load(f)
        self.profile = j['ff_profile_path']
        self.email = j['email']
        self.pw = j['pw']
        self.to_visit = j['pages_to_visit']
        self.data = j['data']
        self.b = webdriver.Firefox(self.profile)

    def login(self):
        # ToDo: check if the login had success
        #       digit slowly mail/pw
        self.b.get('https://facebook.com')
        self.b.find_element_by_id('email').send_keys(self.email)
        self.b.find_element_by_id('pass').send_keys(self.pw)
        self.b.find_element_by_id('loginbutton').click()

    def logout(self):
        # ToDo: is the right page?
        #      is the user logged?
        self.settings_menu()
        logout = self.b.find_element_by_xpath("//*[contains(text(), 'Log Out')]")
        logout.click()

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

    def get_timestamps(self):
        # can be ok to use the time frame as id?
        posts = self.b.find_elements_by_xpath("//*[@class='_5pcr userContentWrapper']//div[@class='_6a _5u5j']")
        if not posts:
            self.scroll_down()
        times = [p.get_attribute('title') for p in posts[0].find_elements_by_xpath("//*[@class='_5pcq']/abbr")]
        timestamps = set([datetime.timestamp(parser.parse(i)) for i in times])
        return timestamps

    def write_json(self, data):
        with open(self.data, 'w') as f:
            json.dump(data, f)