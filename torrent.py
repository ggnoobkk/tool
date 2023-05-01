import os
import re
import time
from bs4 import BeautifulSoup
import requests
import colorama
from colorama import init, Fore, Back, Style

# Inicializa o colorama para impressão de cores no console
colorama.init()

# Define as constantes usadas no programa
IP_PROMPT = 'ip'
LANGUAGE_STRING = 'en'
FIRST_USE = 'Visto pela primeira vez: '
LAST_USE = 'visto pela última vez: '
TORRENT_CATEGORY = 'category: '
NAME_TORRENT = 'nome do arquivo: '
SIZE_TORRENT = 'tamanho do arquivo: '
SAVE_CHOICE = 'Salvar? y/n '

# Define os cabeçalhos usados nas requisições HTTP
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36",
    "Connection": "keep-alive",
    "Host": "iknowwhatyoudownload.com",
    "Referer": "https://iknowwhatyoudownload.com"
}

# Imprime o banner do programa
print(Fore.GREEN)
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

# Pede o endereço IP do usuário e se deseja salvar os resultados em um arquivo
ip = input(f"{IP_PROMPT}: ")
save = input(f'{SAVE_CHOICE}').lower()
print('\n')

def get_torrents(ip_address):
    """
    Faz uma requisição HTTP para o site 'iknowwhatyoudownload.com' para buscar os torrents baixados pelo endereço
input()
