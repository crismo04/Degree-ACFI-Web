from bs4 import BeautifulSoup
import requests


# Función para webscraping para guardar una imagen para cada item en el catálogo.
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
   images = soup.find_all('img')
   img_src_list = [img['src'] for img in images if 'src' in img.attrs]

   if not img_src_list:
       return "no image found"
   return img_src_list[1]

# if __name__ == '__main__':
#    print(get_google_img('patata'))