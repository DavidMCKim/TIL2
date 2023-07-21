from bs4 import BeautifulSoup
from database.mssql_helper import MSSQLConnector
from datetime import datetime
import os
import re
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

class Twitter():
    def __init__(self) -> None:
        # # 크롬드라이버 실행 전 비정상 종료 케이스 처리
        # pwd = subprocess.check_output(['pwd'])
        # path = re.sub(r'\s', '', str(pwd, 'utf-8')) + '/cache'
        # try :
        #     res = subprocess.call([f'ls -al {path} | grep SingletonLock'], shell=True)
        #     res = subprocess.call([f'rm -rf {path}/SingletonLock'], shell=True)
        # except :
        #     pass
        # finally :
        #     res = subprocess.call(["kill -9 $(ps -ef | grep chrome | awk '{print $2}')"], shell=True)
        
        # # 디버그 모드 크롬드라이버 실행
        # subprocess.Popen(f'google-chrome --no-sandbox --headless=new --disable-gpu --disable-dev-shm-usage --disable-blink-features --disable-3d-apis --remote-debugging-port=9222 --user-data-dir={path}', shell=True)

        self.options = Options()
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.3')
        # self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = None
    
    def Twitter_Crawl(self, keyword, startdate, enddate, companyCode):
        try:
            result = True
            login_result = self.Login_Twitter('id','pw')
            if not login_result:
                raise Exception("로그인 실패")
            
            page_url = f"https://twitter.com/search?q={keyword}since:{startdate}until:{enddate}&src=typd&f=live&vertical=default"
            

            self.driver.get(page_url)
            time.sleep(5)

            soup = BeautifulSoup(self.driver.page_source,'html.parser')

            no_div = soup.find_all('div',{'class':'css-1dbjc4n'})
            for div in no_div:
                if (div.text == 'No results' or '대한 검색 결과 없음' in div.text):
                    result = False
                    break
            
            while(result):
                divs = soup.find_all('div',{'data-testid':'cellInnerDiv'})
                if len(divs) > 0:
                    for div in divs:
                        writer     = div.find('a', {'class':'css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l'})['href'][1:]
                        url        = 'https://twitter.com' + div.find('div',{'class':'css-1dbjc4n r-18u37iz r-1q142lx'}).find('a')['href']
                        temp_contents   = div.find('div',{'dir':'auto'}).text.strip()
                        contents   = re.sub('#[A-Za-z0-9가-힣]+', '', temp_contents).strip().replace('\n',' ')
                        hashtags   = ' '.join(re.findall('#[A-Za-z0-9가-힣]+', temp_contents))
                        title      = contents[:20] + "...."
                        wrtieTime  = div.find('div',{'class':'css-1dbjc4n r-18u37iz r-1q142lx'}).find('time')['datetime']
                        count_div  = div.find('div', {'role':'group'})
                        imgUrl = ''
                        isImg = div.find('img')
                        if isImg:
                            imgUrl = isImg['src'].strip()
                        OgDescription = title
                        AnalysisFlag = 'N'      
                        ImgFlag = 'N'
                        CompanyCode = companyCode
                        AutoCrawlFlag = 'Y'            

                        # 찾아서 추가
                        cmtCount   = 0
                        viewCount  = 0
                        likeCount  = 0
                        reqCount   = 0
                        shareCount = 0   
                        if contents != '':
                            query = f'''

                            '''
                            MSSQLConnector.insert(query)




        except Exception as e:
            print(e)

    def Login_Twitter(self, login_id, login_pw):
        try:
            login_result = True
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options)
            login_url = 'https://twitter.com/login?lang=ko'
            self.driver.get(login_url)
            time.sleep(10)

            id_element = self.driver.find_element(By.NAME, "text")
            id_element.send_keys(f'{login_id}')
            time.sleep(5)
            id_element.send_keys(Keys.ENTER)
            time.sleep(5)

            pw_element = self.driver.find_element(By.NAME, "password")
            pw_element.send_keys(f'{login_pw}')
            time.sleep(3)
            pw_element.send_keys(Keys.ENTER)
            time.sleep(10)
        except Exception as e:
            login_result = False      

        return login_result        