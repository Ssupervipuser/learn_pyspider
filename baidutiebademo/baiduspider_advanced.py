import requests

"""
爬虫代码实现步骤
1.准备url地址和请求头参数
2.发送数据
3.解析保存数据
4.定义入口函数
"""
#升级版爬取多个页面

class TieBa():

    def __init__(self, pn):
        # 准备url地址和请求头参数
        self.url = 'https://tieba.baidu.com/f?kw=%E5%BC%B1%E6%99%BA&ie=utf-8&pn='
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
        }

        # 生成不同页数的url地址
        self.url_list = [self.url + str(x * 50) for x in range(pn)]
        print(self.url_list)

    def get_data(self,url):
        # 发送数据
        response = requests.get(url=url, headers=self.headers)
        return response.content.decode()

    def save_data(self, data, index):
        # 解析保存数据
        file_name = 'tieba_' + str(index) + '.html'
        with open(file_name, 'w', encoding='utf8') as f:
            f.write(data)

    def run(self):
        # 定义入口函数,在类的内部，实现各个功能函数之间的协调调用
        # 循环列表
        for url in self.url_list:
            data = self.get_data(url)
            index = self.url_list.index(url)
            print('url_index=', index)
            self.save_data(data, index)


if __name__ == '__main__':
    tieba = TieBa(3)
    tieba.run()
