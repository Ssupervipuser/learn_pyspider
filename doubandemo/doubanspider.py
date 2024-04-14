import json

import requests

"""
1.url https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0
headers
2.get data
3.parse
4.save
5.run
"""


class DouBan:

    def __init__(self):
        self.url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'

        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
        }

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        # print(response.content.decode())
        return response.content.decode()

    def parse_data(self, data):
        # 解析响应获取数据
        results = json.loads(data)
        # print(results)
        results_list = results['subjects']
        # 定义列表，用来保存提取的数据
        data_list = []
        for item in results_list:
            temp = {}
            temp['title'] = item['title']
            temp['url'] = item['url']
            data_list.append(temp)

        return data_list

    def save_data(self, data_list):
        f = open('json_data', 'w',encoding='utf8')
        for data in data_list:
            json_data = json.dumps(data,ensure_ascii=False)
            f.write(json_data)
        f.close()

    # def __del__(self):
    #     self.file.close()

    def run(self):
        try:
            data = self.get_data()
            # print(data)
            data_list = self.parse_data(data)
        except Exception as e:
            print(e)
        self.save_data(data_list)


if __name__ == '__main__':
    douban = DouBan()
    douban.run()
