import requests
from bs4 import BeautifulSoup
import json


URL = "https://www.radiofrance.fr"
url_affaires = "https://www.radiofrance.fr/franceculture/podcasts/affaires-etrangeres"
url_concordance = "https://www.radiofrance.fr/franceculture/podcasts/concordance-des-temps"
url_culture = "https://www.radiofrance.fr/franceculture/podcasts/cultures-monde"
url_eco = "https://www.radiofrance.fr/franceculture/podcasts/entendez-vous-l-eco"

page = requests.get(url_affaires)

soup = BeautifulSoup(page, 'html.parser')
results = soup.find_all("div", class_="CardDetails-title svelte-690u24")

episode_list = []

for result in results:
    link = result.find("a")
    episode_url = URL + link.attrs["href"]
    episode_list.append(episode_url)


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