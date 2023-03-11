import re
from src.utils import fetch

def get_episodes( link:str ):
  d =fetch(f"https://shinden.pl{link}/episodes")

  results =[]
  episodes =d(".list-episode-checkboxes>tr")

  for this in episodes:
    item =d(this)

    results.append({
      "link": item.find("a").attr("href") or "",
      "title": item.find(".ep-title").text(),
      "date": item.find(".ep-date").text(),
      "id": int(item.find("td:nth-child(1)").text()),
      "lang": re.findall(r'(?<=title=").+(?=">)', str(item.find(".flag-icon").parent().html())) or [],
      "avaiable": "fa-check" in (item.find("i").attr("class") or "")
    })

  return [ item for item in results if item["link"] != "" ]
