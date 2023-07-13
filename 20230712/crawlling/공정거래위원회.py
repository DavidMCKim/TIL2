from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
import re


if __name__ == "__main__" :
    try :
        options = Options()

        options.add_argument('--incognito')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        options.add_argument("lang=ko_KR")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})        


        url = 'https://www.ftc.go.kr/www/ReportUserList.do?key=10&rpttype=1'
        driver.get(url)
        time.sleep(1)
        driver.maximize_window()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        links = soup.find_all('td',{'class':'subject'})
        article_numbers = [re.sub(r'[^0-9]', '', link.find('a')['href']) for link in links]

        for article_number in article_numbers:
            try:
                article_url = f'http://www.ftc.go.kr/www/selectReportUserView.do?key=10&rpttype=1&report_data_no={article_number}'
                driver.get(article_url)
                time.sleep(2)
                article_soup  = BeautifulSoup(driver.page_source, 'html.parser')

                title     = article_soup.find('tr', {'class':'subject'}).text.strip().split('제목\n')[1]
                writer    = article_soup.find('tbody').find_all('td')[1].text.strip()
                writetime = article_soup.find('tbody').find_all('td')[2].text.strip()

                driver.find_element(By.XPATH, '//*[@id="formx"]/fieldset/table/tbody/tr[3]/td/ul/li[3]/a[2]/img').click()     
                last_tab = driver.window_handles[-1]
                driver.page_source         
                driver.switch_to.window(window_name=last_tab)
                time.sleep(1)

                pdf_soup  = BeautifulSoup(driver.page_source, 'html.parser')
                max_page = int(pdf_soup.find('div', {'id':'total-page'}).text)
                driver.find_element(By.TAG_NAME, "body").click()
                for i in range(max_page-2):
                    time.sleep(1)
                    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
                pdf_soup  = BeautifulSoup(driver.page_source, 'html.parser')
                pdf_texts = pdf_soup.find_all('span', {'class':'text'})
                content = ''.join([i.text for i in pdf_texts])
                time.sleep(3)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:
                print(e)

    except Exception as e:
        print(e)
