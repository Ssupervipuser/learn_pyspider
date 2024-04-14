import requests

"""
爬虫代码实现步骤
1.准备url地址和请求头参数
2.发送数据
3.解析保存数据
4.定义入口函数
"""


class TieBa():

    def __init__(self, ):
        # 准备url地址和请求头参数
        self.url = 'https://tieba.baidu.com/f?kw=%E5%BC%B1%E6%99%BA&ie=utf-8&pn=0'
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
        }



    def get_data(self):
        # 发送数据
        response = requests.get(url=self.url, headers=self.headers)
        return response.content.decode()

    def save_data(self, data):
        # 解析保存数据
        with open('tieba.html', 'w', encoding='utf8') as f:
            f.write(data)

    def run(self):
        # 定义入口函数,在类的内部，实现各个功能函数之间的协调调用
        data = self.get_data()
        self.save_data(data)


if __name__ == '__main__':
    tieba = TieBa(3)
    tieba.run()
