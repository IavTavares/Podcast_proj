import requests
import json
import time
from utilities.constants import *

dev_server = ""
stage_server = ""
localhost = "localhost"

podcast_list = [url_affaires,url_concordance,url_culture,url_eco]
host = "0.0.0.0"
header_req = {'Content-Type':'application/json'}

for podcast_url in podcast_list:
    data = {"podcast_url": podcast_url}
    start = time.time()
    response = requests.post(host+"/list_episodes", headers=header_req, json=data)
    total_time = time.time()-start
    print(response.json())
    print("Total Time: {}".format(total_time))




