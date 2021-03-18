import scrapy
import sys
import os
import logging
import pymysql
import json

from code_spider.items import CodeSpiderItem

class CodeSpider(scrapy.spiders.Spider):
    MAX_RETRY = 10
    logger = logging.getLogger(__name__)
    name = 'code_spider'
    start_urls = []
    db = pymysql.connect('localhost', 'root', 'morning321', 'zhizaoshe_app')
    cursor = db.cursor()
    select_sql = 'SELECT url,id FROM url_list WHERE id NOT IN (SELECT s_id FROM save_data);'
    cursor.execute(select_sql)
    for i in cursor.fetchall():
        start_urls.append(i)

    def start_requests(self):
        print(len(self.start_urls))
        for par in self.start_urls:
            c_meta = {'s_id':par[1]}
            url = 'https://backend.fyzct.com/xuanxingtong/api/m/match/save/'
            yield scrapy.Request(url,method='POST',meta=c_meta,body=json.dumps(json.loads(par[0])),headers={'spaceUri':'参数请自行抓包','Content-Type': 'application/json'},callback=self.list_html)

    def list_html(self,response):
        html = json.loads(response.body.decode('utf-8'))
        # a_url = 'https://backend.fyzct.com/xuanxingtong/api/m/match/search?openId=ocJcI5__SnSVBk9TrBpVCBzIJ_YY&matchId={save_code}'.format(save_code=html['data'])
        a_url = 'https://backend.fyzct.com/xuanxingtong/api/m/match/search?openId=&matchId={save_code}'.format(save_code=html['data'])

        yield scrapy.Request(a_url,meta=response.meta,method='GET',headers={'spaceUri':'参数请自行抓包'},callback=self.t_html)


    def t_html(self,response):
        html = json.loads(response.body.decode('utf-8'))
        item = CodeSpiderItem()
        item['s_id'] = response.meta['s_id']
        item['save_code'] = json.dumps(html)
        yield item