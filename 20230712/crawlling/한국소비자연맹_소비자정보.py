from bs4 import BeautifulSoup
import requests
import json

if __name__ == "__main__" :
    try :
        url = 'https://cuk.or.kr/include/sangdam_submit.asp?ord_mode=newest&page=&keyword=&area=&type=c&TnNo=3&_=1689050852391'
        custom_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://cuk.or.kr/information/03.asp'
        }
        request = requests.request("GET", url, headers=custom_headers)

        # request = requests.request("GET", url)

        html = request.content.decode('utf-8')
        articles = json.loads(html)
        for article in articles:
            no = article['no'].strip()
            area = article['area'].strip()
            article_link = f'https://cuk.or.kr/information/03_view.asp?TnNo=3&no={no}&page=1&area={area}&keyword=&ord_mode=newest'
            custom_headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                'Referer': 'https://cuk.or.kr/information/03.asp'
            }
            request = requests.request("GET", article_link, headers=custom_headers)
            article_html = request.content.decode('utf-8')
            article_soup = BeautifulSoup(article_html, "html.parser")            

            title     = article_soup.find('div', {'class':'view_tit'}).text.strip()
            content   = article_soup.find('td', {'class':'f19'}).text.strip()
            # writer    = 
            writetime = article_soup.find_all('table', {'class':'board-view'})[0].find('td').text
        
    except Exception as e:
        print(e)

