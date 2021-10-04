import requests
from bs4 import BeautifulSoup
import numpy as np

URL :str = 'https://psnprofiles.com/leaderboard/all/jp'
# LASTPAGE: int = 6656
LASTPAGE: int = 10

def query(page: int) -> dict:
    return {'page': page}

# def save
def main():
    level_list = np.array([])

    for page in range(LASTPAGE):
        print('page:', page)
        res = requests.get(URL, params = query(page))
        soup = BeautifulSoup(res.text, 'lxml')
        table = soup.find(id='leaderboard')
        all_li = table.find_all('li')
        for li in all_li:
            level_list = np.append(level_list, int(li.text))
    
    print(level_list)
    np.savetxt('psn_level.csv', level_list, fmt='%i')
    
if __name__ == '__main__':
    main()
