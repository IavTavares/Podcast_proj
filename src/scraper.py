
from bs4 import BeautifulSoup
#from utilities.constants import *
import json
import requests
import re
from utilities.filesystem import *

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

def podcast_name_from_url(episode_url):
    string = re.search(r"podcasts\/(.*)\/", episode_url).group(1) 
    return string.replace("-","_")


def url_mp3_list(episode_url):
    """episode_url is an element from the list returned by episode_list function
    It returns a list of url for the mp3 files"""
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
                name = file_name(episode_url)
                if not file_Q(os.path.join(folder_path,name)):
                    episode_mp3_url = url_mp3_list(episode_url)[0]
                    r = requests.get(episode_mp3_url, allow_redirects=True)
                    file_path = folder_path+"/"+name
                    if r.headers.get('content-type')=="audio/mpeg":
                        if file_Q(file_path):
                            print(f"{file_path} already exists")
                        else:
                            with open(file_path, 'wb') as f:
                                    f.write(r.content)
                    else:
                            print(f"No audio/mpeg file was downloaded for {name}!")
                else:
                    print(f"File {name} already exists in {folder_path}")

if __name__=="__main__":
    
    ep_list_concordance = episode_list(url_concordance)
    if not folder_Q(folder_path_concordance):
        create_folder(folder_path_concordance)

    download_mp3(ep_list_concordance,folder_path_concordance)