import requests
from bs4 import BeautifulSoup

def yandex(musician, compose):
    request = requests.get("https://music.yandex.ru/search?text=" + compose).text
    soup = BeautifulSoup(request).find()
    links = []
    for f in soup.findAll('div', title=True):
        for e in f.findChildren():
            if e.text.lower() == compose:
                try:
                    link = ("https://music.yandex.ru" + str(e['href']))
                except:
                    continue
                newrequest = requests.get(link).text
                ultrasoup = BeautifulSoup(newrequest).find()
                flag = False
                for k in ultrasoup('span'):
                    if flag == False:
                        try:
                            if "artists" in str(k['class']):
                                for n in k.findChildren():
                                    if n['title'].lower() == musician:
                                        links.append(link)
                                        flag = True
                                        break
                        except:
                            continue
                break
    return links


def vk(musician, compose):
    page = requests.get(f'https://vrit.me/?q={"%".join(compose.split())}')
    soup = BeautifulSoup(page.text, 'html.parser')
    list_mus = soup.find_all('div')[0]
    m = list_mus.find_all(class_='audios')[0]
    flag = False
    for i in m.findChildren():
        if flag == False:
            for k in i.findChildren(class_="info"):
                m = k.find(class_="artist")
                if str(m.text).lower() == musician.lower():
                    l = k.find('a', href=True)
                    link = ("https://vrit.me"+l['href'])
                    req = requests.get(link)
                    filename = str(compose.replace(' ', '')+'.mp3')
                    with open(filename, 'wb') as f:
                        f.write(req.content)
                    return filename
                    flag = True
                    break


vk('lil nas x', 'old town road')
