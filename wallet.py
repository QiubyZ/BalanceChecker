from requests import Session
from bs4 import BeautifulSoup
from os import path
from threading import Thread
sesi = Session()

show_all_Token = True
debug_error = False

def real_path(file_name=r"/AdressWallet.txt"):
    with open(path.dirname(path.abspath(__file__)) + file_name) as openfile:
        return openfile.readlines()

def checker(adress, cari_koin=None):
    link = sesi.get(f"http://bscscan.com/address/{adress.strip()}")
    result = BeautifulSoup(link.text, "html.parser")
    try:
        listtoken = result.find("ul", {"class":"list list-unstyled mb-0"})
        token_list = listtoken.find_all_next("a", {"class": "link-hover d-flex justify-content-between align-items-center"})
        if(show_all_Token):
        	print(f"{adress}")
        for i in range(len(token_list)):
            Token_name = token_list[i].find("span", {"class":"list-name hash-tag text-truncate"}).text
            Token_value, symbl = token_list[i].find("span", {"class":"list-amount link-hover__item hash-tag hash-tag--md text-truncate"}).text.split(" ")
            details = f"{i}. {Token_name} {Token_value} {symbl}"
            if(show_all_Token):
            	if cari_koin == symbl:
            		print(f"\033[1;31m{details}\033[0m")
            	else:
            		print(f"{details}")
            else:
                if cari_koin == symbl:
                	print(f"{adress} | \033[1;31m{Token_value} {symbl}\033[0m")
                
    except Exception as e:
           if(debug_error):
           	print(f"{adress} | Tidak Ada List, {e}")
           else:
           	None

if __name__ == '__main__':
    find_symbol = input("Cari Symbol: ")
    if len(find_symbol) < 0:
        find_symbol = None
    for walet in real_path():
        checker(walet, find_symbol)