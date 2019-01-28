from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import dateutil
from datetime import datetime
import json
import FbBot


class Parser(FbBot):

    def __init__(self, posts = []):
        super().__init__()
        self.posts = posts

    @staticmethod
    def get_id(post):
        # ToDo: parse ID
        # i.e 'feed_subtitle_247;171844246207985;2175324222526634;2175324222526634;1548655205:-4404398567812951017:5:0'
        # 171844246207985 = post_id, 2175324222526634 = photo is
        return post.find_element_by_xpath("//div[@class='_5pcp _5lel _2jyu _232_']").get_attribute('id').split(';')[1]

    @staticmethod
    def get_timestamp(post):
        """
        get timestamp of a single post as WebElement
        """
        time = post.find_elements_by_xpath("//*[@class='_5pcq']/abbr").get_attribute('title')
        return datetime.timestamp(dateutil.parser.parse(time))

    def parse_post(self):
        l = []
        for post in self.posts:
            d = dict()
            d['id']= self.get_id(post)
            d['timestamp'] = self.get_timestamp(post)
            l.append(d)
        return l
