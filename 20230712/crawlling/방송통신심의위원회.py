# from bs4 import BeautifulSoup
# import requests

# if __name__ == "__main__" :
#     try :
#         url = 'http://kocsc.or.kr/PageLink.do/cop/bbs/selectBoardList.do'
#         custom_headers = {
#             'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#             'Accept-Encoding' : 'gzip, deflate',
#             'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#             'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#             'Origin': 'http://kocsc.or.kr'
#         }
#         request = requests.request("POST", url, headers=custom_headers)
#         # request = requests.request("GET", url)
#         html = request.content.decode('utf-8')
#         soup = BeautifulSoup(html, "html.parser")
#         articles = soup.find_all('td',{'class':'tbleft'})[1:]
#         for article in articles:
#             url = 'https://kats.go.kr/'+article.find('a')['href']
#             request = requests.request("GET", url)
#             html = request.content.decode('utf-8')
#             article_soup = BeautifulSoup(html, "html.parser")

#             title     = article_soup.find_all('tr')[0].text.strip()
#             content   = article_soup.find_all('tr')[3].text.strip()
#             writer    = article_soup.find_all('tr')[1].find_all('td')[0].text.strip()
#             writetime = article_soup.find_all('tr')[1].find_all('td')[2].text.strip()
#     except Exception as e:
#         print(e)

import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re

def ReplacePrice(price):
    """ 가격에서 숫자만 추출 """
    regex_price = re.compile('[^0-9]')
    result = int(re.sub(regex_price,'',price))

    return result        

if __name__ == "__main__" :
    try :
        url = 'http://kocsc.or.kr/mainPage.do'
        options = Options()

        options.add_argument('--incognito')
        # options.add_argument('--headless')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        options.add_argument("lang=ko_KR")
        # options.add_argument("Referer=www.coupang.com")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})

        # driver.get('https://www.coupang.com/')
        # driver.delete_all_cookies()
        # time.sleep(3)
        
        # driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
        # driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")

        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        product_list = soup.findAll("a", {"class": "baby-product-link"})

        print(len(product_list))

        for idx, item in enumerate(product_list) :
            try :
                url = "https://www.coupang.com" + item['href']
                driver.delete_all_cookies()
                driver.get(url)
                time.sleep(2)

                item_soup = BeautifulSoup(driver.page_source, 'html.parser')

                if item_soup.find('div', {'class' : 'used-badge-area'}) is not None or item_soup.find('title', {'class' : 'login__content login__content--adult'}) is not None:
                    continue

                title = item_soup.find('h2', {'class': 'prod-buy-header__title'}).text
                review_count = item_soup.find('span', {'class': 'count'}).text
                if review_count is not None :
                    review_count = int(re.sub(r'\D', '', item_soup.find('span', {'class': 'count'}).text))
                else :
                    review_count = 0
                origin_price = item_soup.find('span', {'class': 'origin-price'}) 
                disc_price = item_soup.find('span', {'class': 'total-price'}) 
                if origin_price is None :
                    origin_price = disc_price
                
                if review_count > 0 :
                    review_next_page = True
                    # 리뷰 수집
                    driver.delete_all_cookies()
                    driver.find_element(By.CLASS_NAME, 'moveAnchor').send_keys(Keys.ENTER)

                    driver.find_element(By.CLASS_NAME, 'moveAnchor').send_keys(Keys.ENTER)
                    time.sleep(3)
                    driver.find_element(By.CLASS_NAME, 'sdp-review__article__order__sort__newest-btn').send_keys(Keys.ENTER)
                    time.sleep(2)
                    rv_soup = BeautifulSoup(driver.page_source, 'html.parser')
                    
                    now_page = rv_soup.find('button', {'class':'js_reviewArticlePageBtn'})
                    # rv_count = int(rv_soup.find('div', {'class': 'js_reviewArticleTotalCountHiddenValue'})['data-total-count'])
                    # if rv_count > 0 :
                    rv_list = rv_soup.find_all('article', {'class': 'js_reviewArticleReviewList'})
                    rv_user = []
                    if rv_list is not None :
                        while review_next_page:
                            try:                                
                                for rv in rv_list :
                                    # 리뷰 내용 없을 때 처리 해야함
                                    try :
                                        rv_name = rv.find('span', {'class' : 'sdp-review__article__list__info__user__name'}).text.strip()

                                        # 도움수
                                        try:
                                            rv_likecount = rv.find('span', {'class': 'js_reviewArticleHelpfulCount'}).text
                                        except:
                                            rv_likecount = 0

                                        rv_user.append(rv_name)
                                    except Exception as ex :
                                        print(traceback.print_exc())
                                try:
                                    rv_soup = BeautifulSoup(driver.page_source, 'html.parser')
                                    active_button = ReplacePrice(rv_soup.find('button', {'class':'sdp-review__article__page__num--active'}).text)
                                except:
                                    active_button = 10
                                    review_next_page = False

                                if review_next_page and len(rv_list)%5 == 0:
                                    driver.find_element(By.XPATH, "//button[contains(@class, 'sdp-review__article__page__num--active')]/following-sibling::button").send_keys(Keys.ENTER)
                                else:
                                    break             
                            except Exception as ex:
                                print(traceback.print_exc())
            except :
                print(traceback.format_exc())

        driver.delete_all_cookies()

    except :
        print(traceback.format_exc())
        
     