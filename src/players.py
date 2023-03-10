from pyquery import PyQuery as pq
from requests import get
from src.utils import fetch
import re

def get_player_ids( link:str ):
  d =fetch(f"https://shinden.pl{link}")

  results =[]
  players =d("tbody>tr")
  for this in players:
    item =d(this)

    results.append({
      "source": item.find(".ep-pl-name").text(),
      "quality": item.find(".ep-pl-res").text(),
      "dub_lang": item.find(".ep-pl-alang").text(),
      "sub_lang": item.find(".ep-pl-slang").text(),
      "id": str(item.find(".ep-buttons a").attr("id")).replace("player_data_",""),
    })

  return [ item for item in results if item["source"] != "" ]
