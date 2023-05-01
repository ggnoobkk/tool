import os
os.system('cls' if os.name == 'nt' else 'clear')
from requests import get
from bs4 import BeautifulSoup
import requests, re, time, colorama, random, os
from colorama import init, Fore, Back, Style
colorama.init()


input_string = 'ip'
launage_str = 'en'
first_use = 'Visto pela primeira vez: '
last_use = 'visto pela última vez: '
torrent_category = 'category: '
name_torrent = 'nome do arquivo: '
size_torrent = 'tamanho do arquivo: '
save_choice = 'Salvar? y/n '

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36",
    "Connection": "keep-alive",
    "Host": "iknowwhatyoudownload.com",
    "Referer": "https://iknowwhatyoudownload.com"
}
print (f'{Fore.GREEN}')
print(f"""

 ______   ___   ____   ____     ___  ____   ______ 
|      | /   \ |    \ |    \   /  _]|    \ |      |
|      ||     ||  D  )|  D  ) /  [_ |  _  ||      |
|_|  |_||  O  ||    / |    / |    _]|  |  ||_|  |_|
  |  |  |     ||    \ |    \ |   [_ |  |  |  |  |  
  |  |  |     ||  .  \|  .  \|     ||  |  |  |  |  
  |__|   \___/ |__|\_||__|\_||_____||__|__|  |__|  
                                                    
              > Created by baalware
""")

ip = input(f"{input_string}: ")
save = input(f'{save_choice}').lower()
print('\n')

page = get(f"https://iknowwhatyoudownload.com/{launage_str}/peer/?ip=" + ip,
           headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find(class_="table").find("tbody")
torrents = table.find_all("tr")
results = []
import os
os.system('cls' if os.name == 'nt' else 'clear')
print(f"""

 ______   ___   ____   ____     ___  ____   ______ 
|      | /   \ |    \ |    \   /  _]|    \ |      |
|      ||     ||  D  )|  D  ) /  [_ |  _  ||      |
|_|  |_||  O  ||    / |    / |    _]|  |  ||_|  |_|
  |  |  |     ||    \ |    \ |   [_ |  |  |  |  |  
  |  |  |     ||  .  \|  .  \|     ||  |  |  |  |  
  |__|   \___/ |__|\_||__|\_||_____||__|__|  |__|  
                                                    
              > Created by baalware
""")
for torrent in torrents:
    first, last = torrent.find_all(class_="date-column")
    first, last = first.text, last.text
    category = torrent.find(class_="category-column").text
    name = torrent.find(class_="name-column").text.replace("\n", '').replace('    ', '')
    size = torrent.find(class_="size-column").text
    result = f'{first_use}{first}, {last_use}{last}, {torrent_category}{category}, {name_torrent}{name}, {size_torrent}{size}\n\n'
    results.append(result)
    print ('----------------------------------------')
    print(f'{name_torrent}{Fore.YELLOW}{name}\n{Fore.GREEN}{first_use}{Fore.YELLOW}{first}\n{Fore.GREEN}{last_use}{Fore.YELLOW}{last} \n{Fore.GREEN}{torrent_category}{Fore.WHITE}{category} \n{Fore.GREEN}{size_torrent}{Fore.RED}{size}')
    print (f'{Fore.GREEN}----------------------------------------')

if save == 'y':
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(f'==========={ip}==========\n\n')
        for i in results:
            f.write(i)
input()
