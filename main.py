import requests
from bs4 import BeautifulSoup

#the following is the path to the log file, that contains the URL that has the Convenace (PULL) data, it is needed to be web sracpped
# the history needs to be run first for it to work
path_to_client_file = '"C:\Program Files (x86)\Steam\steamapps\common\Wuthering Waves\Client\Saved\Logs\Client.log"'

def scrape(url):
    page = requests.get(url)
    output = BeautifulSoup(page.text, 'html.parser')
    print(output)
if __name__ == '__main__':
    scrape('https://aki-gm-resources-oversea.aki-game.net/aki/gacha/index.html#/record?svr_id=10cd7254d57e58ae560b15d51e34b4c8&player_id=900821775&lang=en&gacha_id=100042&gacha_type=1&svr_area=global&record_id=05d82552e5052ca46f766c7f5283d915&resources_id=064fae5f9d6473420112230ebfbd69f0&platform=PC')