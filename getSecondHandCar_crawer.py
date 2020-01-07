import requests
from bs4 import BeautifulSoup


def download_page(url):
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
   r = requests.get(url, headers=headers)  # 增加headers, 模拟浏览器
   return r.text


def get_content(html, page):
   soup = BeautifulSoup(html, 'html.parser')
   con = soup.find(class_='viewlist_ul')
   con_list = con.find_all('li', class_="list-photo-li")  # 找到列表
   for i in con_list:
       carName = i.find('h4', class_='card-name').string  # 获取车名
       unit = i.find('p', class_='cards-unit').string  # 获取unit
       priceEm = i.find('span', class_='pirce').find('em')
       price = f'${priceEm.string} ${priceEm.nextSibling}'  # price
       image = i.find('div', class_='img-box').find('img').attrs['src'] # price

       save_txt('\n'.join((carName, unit, price, image)))


def save_txt(*args):
   for i in args:
       with open('che168.txt', 'a', encoding='utf-8') as f:
           f.write(i)
           f.close()


def main():
   # 在二手车页面下方可以看到共有89页，构造如下 url，
   # 当然我们最好是用 Beautiful Soup找到页面底部有多少页。
   for i in range(0, 88):
        url = 'https://www.che168.com/guangzhou/a0_0msdgscncgpi1ltocsp1exx{}/?pvareaid=102179#currengpostion'
        html = download_page(url)
        get_content(html, i)

if __name__ == '__main__':
   main()