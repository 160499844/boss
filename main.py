"""boss直聘自动打招呼机器人"""

import requests
import time
from selenium import webdriver
import pickle
import os


#https://www.zhipin.com/web/geek/recommend?expectId=43803049&sortType=1&page=2&salary=405&experience=104&districtCode=0&cityCode=101280100

geckodriver_path = r'D:\development\chromedriver_win32\geckodriver.exe'

headers = {
        'referer': 'https://www.zhipin.com/web/geek/recommend?expectId=43803049&sortType=1&page=3&salary=405&experience=104&districtCode=0&cityCode=101280100',
        'cookie': 'lastCity=101280800; _bl_uid=83kd9ee57b4aXLun33XbkqyatXt5; __g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1603979036,1605417948,1606056023; t=NGO6kpifJh5SDF1h; wt=NGO6kpifJh5SDF1h; wt2=vGDIA5f2ch5SDF1h; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1606059623; __c=1606056022; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Frecommend%3FexpectId%3D43803049%26sortType%3D1%26page%3D2%26salary%3D405%26experience%3D104%26districtCode%3D0%26cityCode%3D101280100&r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K60000avpXkFvm720nxGT6Gosg5nHH4Uiz8XaCYi0MVJ0lEIvNEX7G1pP3MHWS4syou-7eHwcoEd0u08YW-wvCffHjmuA_6G3EthD5IXk2woR7CGGL81y-N2BYcTln8pIWgg33yaExsK4GHeflb_itDAMH9TN71KRgz6WYimkD3RCcCcwUqWPvn9nMY1K6v_OMW3PCWrMVO-vZAOPWtCYcPo5AtA.DR_NR2Ar5Od663rj6t8AGSPticrZA1AlaqM766WHGek3hcYlXE_sgn8mE8kstVerQKMks4OgSWS534Oqo4yunOogEOtZV_zyUr1oWC_knmx5I9LtTrzEj4SrZuEse59sSX1jexo9vxQ5jWl3cMYAn5M8seSrZug9tOZj_L3IMs4t5MEseQnrOv3x5kseS1jeIMgVHC3ZHgng8WWlsk8sHfGmEIjfEl1F8xnhA6kNfCm3t5Zv3TMds45osTZK4TPHtU3bmTMdWHGs45ogu1RdrYG4TXGmuCyrPIMZBC0.U1Yk0ZDqmhq1TsKspynqn0KY5yFETLn0pyYqnWcd0ATqUvwlnfKdpHdBmy-bIfKspyfqP0KWpyfqrjf0UgfqnH0krNtknjDLg1csPH7xnH0zndt1nHcsg1DsPjwxn1msnfKopHYs0ZFY5Hnk0AFG5HDdPNtkPH9xnW0Yg1ckPsKVm1Yknj0kg1D3PWmdnHDLPHwxnW0dnNtkg1Dsn-tknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5HbLP16dnjnzP0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyIlpZ940A-bm1dcHbD0IA7zuvNY5Hm1g1KxnHRs0ZwdT1YkPWTvPjb3nWfsrj04njmYPHTznsKzug7Y5HDvnjmsPHmsnW0sn1m0Tv-b5yDkPWNWryf3nj0sPAPWmH00mLPV5HTzPj7AwH-jnWu7rjI7PYf0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0Aw-I7qWTADqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg1f1nH04rHNxPjnknjb4PNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00uAPWujY0IZF9uARqP1msnW0z0AFbpyfqwDD3PYRkPRDYnbNafbmvnHT1wDDYP1bzPYD1f104P160UvnqnfKBIjYs0Aq9IZTqn0KEIjYk0AqzTZfqnBnsc1Dsc1cWrj0zrHnsnWDWnWnsnj0WnWnsnj08nj0snj0sc1DWnBnsczYWna3snjb3rHDWni3krH6snj00TNqv5H08rHFxna3sn7tsQW0sg108PHuxna3dP7tsQWn10AF1gLKzUvwGujYs0APzm1YYPHm1%26ck%3D5252.5.73.976.178.1074.218.133%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.300.0%26wd%3D%26bc%3D110101&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-pc-BOSS-JD02-B19KA02084%26plan%3D%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-cp%26unit%3D%25E5%2593%2581%25E7%2589%258C-%25E9%2580%259A%25E7%2594%25A8%26keyword%3Dboss%26bd_vid%3D10307847496468453041%26csource%3Dboctb&s=3&friend_source=0&s=3&friend_source=0; __a=71435295.1597327419.1605417948.1606056022.202.7.21.21; __zp_stoken__=1a50bOENMGA46ZltOJF9sY11oUFdSE114VGxNNGkiIGxOOjUpGhUDBRBACERzJWFKHiY2VXR3Qn9eY0BlKTB0OT4hVXF%2FZV44eiV0GRobGRtFMyoYN2Q4Xy4EVX1vB1F9GHc8RkZ9RwA0QAkGPg%3D%3D',
        'token': '2P2RjPhK2cfnEh8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }

def openChat(session,jobId,lid,sessionId):
    """打招呼"""
    url = "https://www.zhipin.com/wapi/zpgeek/friend/add.json"
    params={
        "jobId":jobId,
        "lid":lid,
        "sessionId":sessionId,
    }
    js = session.get(url,params=params,headers=headers).json()
    code = js['code']
    if code == 0:
        print(js)
    else:
        print('\033[31m%s\033[0m' %js['message'])

def getWorks(session,url):

    try:
        js = session.get(url, headers=headers).json()
        date = js['zpData']
        sessionId = date['sessionId']
        jobList = date['jobList']
        #print("sessionId=%s" % sessionId)
        for item in jobList:
            print(item)

            jobId = item['encryptBrandId']
            lid = item['lid']

            openChat(session, jobId, lid, sessionId)

            time.sleep(15)
    except Exception as e:
        print(js)
        print('\033[31m请求出错,错误原因:%ss\033[0m' %e)

if __name__ == '__main__':

    session = requests.session()
    session.verify = False
    session.get('https://www.zhipin.com/web/geek/recommend')


    for page in range(10,1,-1):
        page_url = 'https://www.zhipin.com/wapi/zpgeek/recommend/job/list.json?' \
                   'expectId=43803049&sortType=1&page=%s&salary=405&payType=&degree=&experience=104&stage=&scale=&districtCode=0&businessCode=' % str(page)
        getWorks(session,page_url)
