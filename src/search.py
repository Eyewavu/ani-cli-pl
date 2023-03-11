import urllib
from src.utils import fetch

def search( query:str ):
  d =fetch(f"https://shinden.pl/series?search={urllib.parse.quote(query)}")

  list_items =d(".div-row")
  results =[]

  for this in list_items:
    item =d(this)

    results.append({
      "title": item.find("h3>a").text() or "",
      "episodes": item.find(".episodes-col").attr("title") or "",
      "link": item.find("h3>a").attr("href") or ""
    })

  return [ item for item in results if item["link"] != "" ]
