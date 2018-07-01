import requests
import re
import time
from multiprocessing import Pool
from requests.exceptions import RequestException
import json



def get_one_page(url):#1.获得网页

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text

    except RequestException:

#
        print('连接错误')
        return None#get_one_page(url)
def parse_one_page(html):#2.解释网页
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?<a href="(.*?)".*?title="(.*?)".*?<p class="star">(.*?)</p><p class="releasetime">(.*?)</p></dd>',re.S)
    items=re.findall(pattern,html)

    for item in items:
        # yield{#生成器，用在迭代器（for或者其他循环语句）后面挑选有用的数据
        yield{
           'index':item[0],
           'href':item[1],
           'movie':item[2],
           'time':item[3],
           'actos':item[4]

        }
def write_to_file(content):
    with open('maoyanmovie.txt','a',encoding='utf-8')as f:#'a'代表不删去任何内容加入
        f.write(json.dumps(content) + '\n') #json.dumps是为了转换成字符串
        f.close()

def main(number):#3.调用前面两个函数
    # headers={'Cookie':'td_cookie=18446744071409288433; uuid=1A6E888B4A4B29B16FBA1299108DBE9C400B2EEFB1837DC9AA2DAB9A6164ADEF; _lxsdk_cuid=162f11ded68c8-0d1e08b6f2220c-3f3c5701-100200-162f11ded68c8; _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9C400B2EEFB1837DC9AA2DAB9A6164ADEF; _csrf=e3824033c04c6543525f39d8b89f7bbede08f3989d63845f69f1f684b1f2656c; td_cookie=18446744071672374209; __mta=244177850.1524463693265.1525072432087.1525072598095.36; _lxsdk_s=1631565642d-d8a-fde-6a5%7C%7C22',
    #         'Host': 'maoyan.com',
    #         'Referer': 'http://maoyan.com/board',
    #         'Upgrade-Insecure-Requests': '1',}
    url='http://maoyan.com/board/4?offset='+str(number)
    html=get_one_page(url)
    print(html)
    content=parse_one_page(html)
    print(content)
    write_to_file(content)

if __name__=='__main__':#4.主函数
    for i in range(10):
        main(i*10)

#     pool=Pool()
#     pool.map(main,[i*10 for i in range(10)])#pool.map()函数





