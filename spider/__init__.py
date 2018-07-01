import requests
import re
import time
from requests.exceptions import RequestException


for i in range(1,100):
   #try:
        a_url='http://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(i)+'.html'
        html_1=requests.get(a_url)
        # print(html_1.status_code)
    #except RequestException:
        #print('连接错误')
        html_1.encoding='gb2312'
        # print(html_1.text)
        # c_text=html_1.text
        time.sleep(2)
        b_list=re.findall('<a href="(.*?)" class="ulink">.*?</a>',html_1.text)
        # print(b_list)
        for n in b_list:

            #try:
            b_url='http://www.ygdy8.net'+str(n)
            html_2=requests.get(b_url)
            #except RequestException:
                #print('连接错误')
            html_2.encoding='gb2312'
                # print(html_2.text)
            d_list=re.findall('<a href="(.*?)">.*?</a></td>',html_2.text)
            for m in d_list:
                print(m)
                # print(d_list)
                with open('spider.txt','a',encoding='utf-8')as f:
                    f.write(m +'\n')
                    f.close()

                #with open('spider.txt','a',encoding='utf-8') as f:
                    #f.write(m+'\n')
                    #f.close()






