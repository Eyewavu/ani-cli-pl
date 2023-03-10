from colorama import Fore
from pyquery import PyQuery as pq
from requests import get
import os

def fetch( url:str ):
  headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Cookie": "cb-rodo=enabled;",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en,q=0.7"
  }

  response =get(url,headers=headers)
  return pq(response.content)

def cls():
  os.system("cls" if os.name=="nt" else "clear")

def createMenu( arr:list ):
  current_answer =-1
  while current_answer == -1:
    print(f"{Fore.YELLOW} 0. {Fore.RED} (Exit){Fore.RESET}")

    for i,item in enumerate(arr):
      index =f"{i+1: }" if i+1 < 10 else str(i+1)
      
      print(f"{Fore.YELLOW}{index}. {item}{Fore.RESET}")


    response =input(f"Your answer (0-{len(arr)}): ")
    current_answer =int(response) if response.isdigit() else -1
    current_answer =0 if response == "q" else current_answer
    cls()
  
  return current_answer
