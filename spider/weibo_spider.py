# -*- coding: utf-8 -*-
import urllib
import urllib.request
import json
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class WeiboSpider(object):
    def __init__(self, uid):
        self.page_index = 1
        self.uid = uid
        self.page_url = "https://m.weibo.cn/api/container/getIndex?uid={0}&luicode=10000011&lfid=1076036006394101&display=0\
                    &retcode=6102&type=uid&value={0}&containerid=1076036006394101&page=".format(self.uid)
        self.content_url = "https://m.weibo.cn/status/"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
        self.pattern = re.compile(r'"text": "(.*)",')
        self.write_file = open(u"姑射山人.txt", "w", encoding = "utf-8")

    def run(self):
        while True:
            url_address = self.page_url + str(self.page_index)
            html_text = self.get_html(url_address)
            print(html_text)
            json_txt = json.loads(html_text)
            if json_txt["ok"] == 1:
                self.get_all_content_id(json_txt)
            else:
                break
            self.page_index += 1
            print(self.page_index)
        self.write_file.close()

    def get_html(self, url_address):
        req_http = urllib.request.Request(url_address, headers=self.headers)
        html = urllib.request.urlopen(req_http).read()
        return html.decode("utf-8")

    def get_all_content_id(self, json_data):
        cards = json_data["data"]["cards"]
        for card in cards:
            content_id = card["mblog"]["id"]
            url_address = self.content_url + content_id
            html_text = self.get_html(url_address)
            html_lines = html_text.split("\n")
            for line in html_lines:
                if '"text"' in line:
                    res = self.pattern.findall(line)[0]
                    res = res.replace("<br />", "\n")
                    res = re.sub(r'</?\w+[^>]*>', '', res)
                    print(res)
                    self.write_file.write(res + "\n\n")
                    break
                    # time.sleep(0.5)


if __name__ == '__main__':
    weibo_spider = WeiboSpider(6006394101)
    weibo_spider.run()
