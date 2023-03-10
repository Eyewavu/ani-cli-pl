from colorama import Fore
from importlib import import_module
from src.search import search
from src.episodes import get_episodes
from src.players import get_player_ids
from src.video import get_video_link
from src.utils import cls, createMenu
from subprocess import run as summon
import argparse

def cli():
    parser =argparse.ArgumentParser("Anime CLI *PL*")
    parser.add_argument("-s","--search",type=str)

    args =parser.parse_args()
    
    series_found =False
    series_link =""

    if args.search != None:
      results =search( args.search )
      list_items =list(map(lambda item: f"{Fore.GREEN}\"{item['title']}\" {Fore.BLUE}{item['episodes']}",results))
      answer =createMenu(list_items)

      if answer == 0: return
      series_found =True
      series_link =results[answer -1]['link']

    episode_found =False
    episode_link =""

    if series_found:
      results =get_episodes(series_link)
      list_items =list(map(lambda item: f"{Fore.GREEN}\"{item['title']}\" {Fore.GREEN if item['avaiable'] else Fore.RED}{'✓' if item['avaiable'] else 'x'}",results))
      answer =createMenu(list_items)

      if answer == 0: return      
      episode_found =True
      episode_link = results[answer -1]['link']
      
    player_found =False
    playerid =""

    if episode_found:
      results =get_player_ids(episode_link)
      list_items =list(map(lambda item: f"{Fore.GREEN}\"{item['source']}\" {Fore.WHITE}{item['quality']} {Fore.RED}{item['dub_lang']} {Fore.WHITE}{item['sub_lang']}",results))
      answer =createMenu(list_items)

      if answer == 0: return
      player_found =True
      playerid =results[answer -1]['id']
    
    if player_found:
      video_url =get_video_link(playerid)
      print(f"video found at: {video_url}")
      summon(["mpv",video_url])