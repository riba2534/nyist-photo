import re
import base64
import requests
import time
import os
import shutil
import random
#地址：https://kan.msxiaobing.com/ImageGame/Portal?task=yanzhi&feid=d89e6ce730dab7a2410c6dad803b5986
#一分钟10个，一小时120个，一天360个
upload_url = 'http://kan.msxiaobing.com/Api/Image/UploadBase64'
comp_url = 'https://kan.msxiaobing.com/Api/ImageAnalyze/Process'
# proxies = {
#         "http": "http://183.230.177.170:8081/"
#
#     }

# proxies=proxies
def get_img_url(file_name):
    with open(file_name,'rb') as f:
        img_base64=base64.b64encode(f.read())
    r=requests.post(upload_url,data=img_base64)
    print(r.json())
    url='https://mediaplatform.msxiaobing.com' + r.json()['Url']
    return url


def get_score(img_url):
    sys_time = int(time.time())
    payload = {'service': 'yanzhi',
               'tid': '7531216b61b14d208496ee52bca9a9a8'}
    form = {
        'MsgId': str(sys_time) + '733',
        'CreateTime': sys_time,
        'Content[imageUrl]': img_url,
    }
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Cookie':'_ga=GA1.2.1597838376.1504599720; _gid=GA1.2.1466467655.1504599720; ai_user=sp1jt|2017-09-05T10:53:04.090Z; cpid=YDLcMF5LPDFfSlQyfUkvMs9IbjQZMiQ2XTJHMVswUTFPAA; salt=EAA803807C2E9ECD7D786D3FA9516786; ARRAffinity=3dc0ec2b3434a920266e7d4652ca9f67c3f662b5a675f83cf7467278ef043663; ai_session=sQna0|1504664570638.64|1504664570638'+str(random.randint(11, 999)),
        'Referer': 'https://kan.msxiaobing.com/ImageGame/Portal?task=yanzhi&feid=d89e6ce730dab7a2410c6dad803b5986'
    }
    r = requests.post(comp_url,params=payload, data=form,headers=headers)
    print(r.json())
    text=r.json()['content']['text']
    return text



def save_judge(name):
    pattern = r'\d\.\d'
    if name[-3:] == 'JPG':
        url = get_img_url(name)
        score_text=get_score(url)
        print(score_text)
        if re.findall(pattern,score_text):
            score = re.findall(pattern, score_text)[0]
        else:
            score=score_text[:2]
        with open('log.txt','a') as log:
            log.write(score_text+':'+name+'\n')
        new_name=score+'-'+name
        os.rename(name,new_name)

def main():

    os.chdir('D:\\我的程序\\Python\\nyist_photo\\南阳理工所有照片')
    file_list=os.listdir()
    for file_name in file_list:
        if len(file_name)==20:
            try:
                save_judge(file_name)
            except:
                print('在'+file_name+'暂停了一次')
                time.sleep(60)
                main()



if __name__ == '__main__':
    main()








