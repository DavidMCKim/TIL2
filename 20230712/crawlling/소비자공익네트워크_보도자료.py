from bs4 import BeautifulSoup
import requests

if __name__ == "__main__" :
    try :
        url = 'http://sobo112.or.kr/news/news.php'
        # custom_headers = {
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        #     'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        #     'Referer': 'https://www.dcinside.com/'
        # }
        # request = requests.request("GET", url, headers=custom_headers)

        request = requests.request("GET", url)

        html = request.content.decode('euc-kr')
        soup = BeautifulSoup(html, "html.parser")

        links = soup.find_all('a', {'class':'lnk'})
        list_link = [url+link['href'] for link in links]

        for link in list_link:
            request = requests.request("GET", link)
            html = request.content.decode('euc-kr')
            soup = BeautifulSoup(html, "html.parser")

            title     = soup.find('table', {'class':'AWbbs_view_table border'}).find_all('tr')[0].text.strip()
            content   = soup.find('div', {'id':'article-view-content-div'}).text.strip()
            writer    = soup.find('table', {'class':'AWbbs_view_table border'}).find_all('tr')[1].text.split('작성일')[0].split(':')[1].strip()
        
    except Exception as e:
        print(e)