import requests 
from bs4  import BeautifulSoup 
import bs4.element
import datetime


def rank_news_crawling():
    base_url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111" \

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    # web page information 
    res = requests.get(base_url, headers = headers)
    # parsing 
    soup = BeautifulSoup(res.text, 'html.parser')
    lis4 = soup.find('ul', class_='rankingnews_list').find_all("li", limit=50)
    news_list=[] 

    for li in lis4:
        news_info = {
            "title" : li.a.string,
            "links" : li.a["href"],
            "upload_time" : li.span.string,
            "img_src" : li.img["src"]

        }
        news_list.append(news_info)


    return news_list 

def save_list(list):
    with open('test.txt', 'w', encoding='UTF-8') as f:
        for information in informations:
            for key, value  in information.items():
                f.write(f"{key} : {value} \n")
            f.write("\n")


informations = rank_news_crawling()
save_list(list)







