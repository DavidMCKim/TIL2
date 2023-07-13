from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager



if __name__ == "__main__" :
    try :
        options = Options()

        options.add_argument('--incognito')
        # options.add_argument('--headless')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        options.add_argument("lang=ko_KR")
        # options.add_argument("Referer=www.coupang.com")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})        


        url = 'https://www.foodsafetykorea.go.kr/portal/fooddanger/suspension.do?menu_no=2713&menu_grp=MENU_NEW02'
        driver.get(url)
        time.sleep(1)
        driver.maximize_window()
        select = Select(driver.find_element(By.NAME, 'show_cnt'))
        select.select_by_value('60')
        time.sleep(1)
        driver.find_element(By.ID,'show_cnt-btn').send_keys(Keys.ENTER)
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        links = soup.find_all('a', {'class':'recall fancybox.ajax'})
        list_link = ['https://www.foodsafetykorea.go.kr/' + link['href'] for link in links ]

        for link in list_link:
            try:
                driver.get(link)
                time.sleep(2)
                article_soup  = BeautifulSoup(driver.page_source, 'html.parser')
                title     = article_soup.find('tbody').find('th', {'class':'title'}).text.strip()
                writetime = article_soup.find('tbody').find_all('td')[0].text
               
                driver.switch_to.frame('synapDocPreviewFrame')
                article_soup  = BeautifulSoup(driver.page_source, 'html.parser')
                max_page = int(article_soup.find('div', {'id':'total-page'}).text)
                driver.switch_to.default_content()
                driver.find_element(By.TAG_NAME, "iframe").click()
                for i in range(max_page-2):
                    time.sleep(1)
                    driver.find_element(By.TAG_NAME, "iframe").send_keys(Keys.PAGE_DOWN)

                final_article = ''
                driver.switch_to.frame('synapDocPreviewFrame')
                article_soup  = BeautifulSoup(driver.page_source, 'html.parser')
                articles = article_soup.find_all('div',{'class':'contents-page'})
                for article in articles:
                    if article != '':
                        final_article += article.text
                content = final_article.strip()
                driver.switch_to.default_content()
            except Exception as e:
                print(e)
        
        # custom_headers = {
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        #     'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
        # }
        # request = requests.request("GET", url, verify=False)

        # html = request.text
        # soup = BeautifulSoup(html, "html.parser")
        
        # links = soup.find('tbody').find_all('a')
        # list_link = ['https://www.kca.go.kr/home/sub.do'+link['href'] for link in links]

        
    except Exception as e:
        print(e)

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# wait = WebDriverWait(self.driver, 10)
# page_element = wait.until(EC.presence_of_element_located((By.ID, 'page__input')))
# pw_element = wait.until(EC.presence_of_element_located((By.ID, 'pw')))

# self.driver.execute_script(
#     f"arguments[0].setAttribute('value', '{self.login_id}')", id_element
# )
# time.sleep(1)        