from bs4 import BeautifulSoup
import requests

if __name__ == "__main__" :
    try :
        url = 'http://www.motie.go.kr/motie/ne/presse/press2/bbs/bbsList.do?bbs_cd_n=81'
        # custom_headers = {
        #     'Accept': 'application/json, text/javascript, */*; q=0.01',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        #     'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        #     'Referer': 'https://cuk.or.kr/information/03.asp'
        # }
        # request = requests.request("GET", url, headers=custom_headers)
        request = requests.request("GET", url)
        html = request.content.decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")
        article_container = soup.find('table', {'class':'default_tb'})
        articles = article_container.find_all('div',{'class':'ellipsis'})
        for article in articles:
            url = 'http://www.motie.go.kr/motie/ne/presse/press2/bbs/'+article.find('a')['href']
            request = requests.request("GET", url)
            html = request.content.decode('utf-8')
            article_soup = BeautifulSoup(html, "html.parser")

            title     = article_soup.find('td',{'class':'subject'}).text.strip()
            content   = article_soup.find('div', {'class':'contTx'}).text.strip()
            writer    = article_soup.find('tbody',{'class':'t_bg'}).find_all('td')[1].text
            writetime = article_soup.find('tbody',{'class':'t_bg'}).find_all('td')[4].text
    except Exception as e:
        print(e)