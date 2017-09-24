# /usr/bin/env python3

import requests
from parsel import Selector
import random
from os import path as opath
import pymysql
from datetime import datetime

class Food:
    ''' 保存字段 '''
    def __init__(self, name, imgUrl, price):
        self.name = name
        self.imgUrl = imgUrl
        self.price = price

class Mysql:
    ''' mysql数据插入 '''
    def __init__(self, sql, params=None):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': 'car990226',
            'db': 'xiaohuo',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()

        self.sql = sql
        self.params = params

    def Insert(self):
        try:
            row = self.cursor.execute(self.sql, self.params)
            self.conn.commit()
            return row
        except:
            self.conn.rollback()
        finally:
            self.cursor.close()       
            self.conn.close()


class XiachufangSpider:
    '''下厨房网站爬虫'''
    def __init__(self, url):
        self.url = url
        self.food_list = []

    def get_user_agent(self):
        '''获取随机User-Agent'''
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        ]
        ua = random.choice(user_agent_list)
        return ua

    def get_html(self, url):
        '''请求网页内容'''
        headers = {
            'User-Agent': self.get_user_agent(),
        }
        try:
            r = requests.get(url=url, headers=headers, timeout=5)
            r.raise_for_status()
            r.encoding = 'UTF-8'
            return r.text
        except:
            return 'request error'

    def get_imgUrl(self, link):
        '''获取图片地址'''
        doc = Selector(self.get_html(link))
        imgUrl = doc.xpath('//div[@class="cover image expandable block-negative-margin"]/img/@src').extract_first()
        return imgUrl

    def get_info(self):
        '''解析网页内容'''
        doc = Selector(self.get_html(self.url))
        base = doc.xpath('//div[@class="normal-recipe-list"]/ul/li/a')
        for food in base:
            name = food.xpath('./div[@class="info pure-u"]/p[@class="name"]/text()').extract_first().strip()
            item = []
            for i in name:
                if i in (' ', '（','）','～','【','】','~','：','-','！','」','「'): # 剔除name中含有的元组内的字符
                    continue
                item.append(i)
            name = ''.join(item)
            link = 'http://www.xiachufang.com' + food.xpath('./@href').extract_first()
            imgUrl = self.get_imgUrl(link)
            price = str(random.randint(15,40))
            
            afood = Food(name, imgUrl, price)
            self.food_list.append(afood)

    def push_to_mysql(self):
        '''数据保存到MySQL数据库'''
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 获取当前时间

        for afood in self.food_list:
            # 处理保存的字段
            name = afood.name
            price = afood.price
            time = now 
            image = afood.imgUrl
            menu_id = random.randint(1,5)
            print(name)

            # conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='car990226',db='xiaohuo',charset='utf8',cursorclass=pymysql.cursors.DictCursor)

            # try:
            #     with conn.cursor() as cursor:
            #         sql = 'insert into takeout_food (name, price, time, image, menu_id) values (%s,%s,%s,%s,%s)'
            #         cursor.execute(sql, (name, price, time, image, menu_id))
            #         conn.commit()
            # finally:
            #     conn.close()

            sql = 'insert into takeout_food (name, price, time, image, menu_id, introduce, isright) values (%s,%s,%s,%s,%s,%s,%s)'
            params = (name, price, time, image, menu_id, '', False)
            
            mysql = Mysql(sql, params)
            mysql.Insert()


if __name__ == '__main__':
    url = 'http://www.xiachufang.com/category/40076/?page=2'
    xcf = XiachufangSpider(url)
    xcf.get_info()
    xcf.push_to_mysql()