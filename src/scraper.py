
from bs4 import BeautifulSoup
from constants import *
import json
import requests
import re


def episode_list(podcast_url):
    page = requests.get(podcast_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("div", class_="CardDetails-title svelte-690u24")
    list_ep = []
    for result in results:
        link = result.find("a")
        episode_url = URL + link.attrs["href"]
        list_ep.append(episode_url)
    return list_ep

def file_name(episode_url):
    string = re.search(r"([^\/]+$)", episode_url).group()
    res = string.strip("-0123456789")+".mp3"
    return res

def episode_mp3_list(episode_url):
    """episode_url is an element from the list returned by episode_list function"""
    episode_page = requests.get(episode_url)# ep_list_concordance[0])
    soup = BeautifulSoup(episode_page.content, 'html.parser')
    results = soup.find_all(type="application/ld+json")
    mp3_list = []
    for res in results:
        if "mp3" in res.text:
            json_dict= json.loads("".join(res))
            ep_mp3_url = json_dict['@graph'][0]["mainEntity"]["contentUrl"]
            mp3_list.append(ep_mp3_url)
    return mp3_list

def download_mp3(list_episodes:list, folder_path:str):
        for episode_url in list_episodes:
                episode_mp3 = episode_mp3_list(episode_url)[0]
                r = requests.get(episode_mp3, allow_redirects=True)
                name = file_name(episode_url)
                if r.headers.get('content-type')=="audio/mpeg":
                        with open(folder_path+"/"+name, 'wb') as f:
                                f.write(r.content)
                else:
                        print(f"No audio/mpeg file was downloaded for {name}!")

if __name__=="__main__":
    ep_list_concordance = episode_list(url_concordance)
    download_mp3(ep_list_concordance,folder_path_concordance)