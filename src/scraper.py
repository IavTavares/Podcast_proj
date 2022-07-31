import requests
from bs4 import BeautifulSoup

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