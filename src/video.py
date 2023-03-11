from time import sleep
import re
import requests
from pyquery import PyQuery as pq
from src.utils import cls

AUTH ="X2d1ZXN0XzowLDUsMjEwMDAwMDAsMjU1LDQxNzQyOTM2NDQ%3D"
HEADERS ={
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
  "cache-control": "max-age=0",
  "referer": "https://shinden.pl/",
  "sec-fetch-dest": "document",
  "sec-fetch-mode": "navigate",
  "sec-fetch-site": "same-origin",
  "sec-fetch-user": "?1",
  "sec-gpc": "1",
  "upgrade-insecure-requests": "1",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

def get_video_link( playerid:str ):
  session =requests.Session()
  url1 =f"https://api4.shinden.pl/xhr/{playerid}/player_load?auth={AUTH}"
  url2 =f"https://api4.shinden.pl/xhr/{playerid}/player_show?auth={AUTH}&width=0&height=-1"

  session.get(url1,headers=HEADERS)
  for i in range(5):
    print(f"{5 -i} seconds remaining...")
    sleep(1)
    cls()

  response =session.get(url2,headers=HEADERS)
  d =pq(response.content)

  link =str(d("iframe").attr("src"))
  link =re.sub(r"^\/{2}","",link)
  if re.match(r"^https:\/{2}",link) is None:
    link =f"https://{link}"

  return link
