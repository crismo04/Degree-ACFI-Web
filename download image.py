from bs4 import BeautifulSoup
import requests


def get_google_img(query):
    """
    gets a link to the first google image search result
    :param query: search query string
    :result: url string to first result
    """
    url = "https://www.google.com/search?q=" + str(query) + "&source=lnms&tbm=isch"
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find("img",{"class":"t0fcAb"})

    if not image:
        return 
    return image['src']


if __name__ == '__main__':
    query = input("patata")
    print(get_google_img(query) or "no image found")