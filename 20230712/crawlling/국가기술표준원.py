from bs4 import BeautifulSoup
import requests

if __name__ == "__main__" :
    try :
        url = 'https://kats.go.kr/content.do?cmsid=240'
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
        articles = soup.find_all('td',{'class':'tbleft'})[1:]
        for article in articles:
            url = 'https://kats.go.kr/'+article.find('a')['href']
            request = requests.request("GET", url)
            html = request.content.decode('utf-8')
            article_soup = BeautifulSoup(html, "html.parser")

            title     = article_soup.find_all('tr')[0].text.strip()
            content   = article_soup.find_all('tr')[3].text.strip()
            writer    = article_soup.find_all('tr')[1].find_all('td')[0].text.strip()
            writetime = article_soup.find_all('tr')[1].find_all('td')[2].text.strip()
    except Exception as e:
        print(e)