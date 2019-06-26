import requests
from bs4 import BeautifulSoup


def yandex(musician, compose):
    request = requests.get("https://music.yandex.ru/search?text=" + '%20'.join(compose.lower().split(' '))).text
    soup = BeautifulSoup(request).find()
    links = []
    flag = False
    for f in soup.findAll('div', title=True):
        for e in f.findChildren():
            if e.text.lower() == compose.lower():
                try:
                    link = ("https://music.yandex.ru" + str(e['href']))
                except:
                    continue
                newrequest = requests.get(link).text
                ultrasoup = BeautifulSoup(newrequest).find()
                for k in ultrasoup('span'):
                        try:
                            if "artists" in str(k['class']):
                                for n in k.findChildren():
                                    if musician.strip().lower() in n.text.strip().lower():
                                        links.append(link)
                                        flag = True
                                        break
                        except:
                            continue
    if flag:
        return links[0]
    else:
        return None


def vk(musician, compose):
    page = requests.get(f'https://vrit.me/?q={"%20".join(compose.lower().split())}')
    soup = BeautifulSoup(page.text, 'html.parser')
    list_mus = soup.find_all('div')[0]
    try:
        m = list_mus.find_all(class_='audios')[0]
    except:
        return None, None, None
    flag = False
    for i in m.findChildren():
        if not flag:
            for k in i.findChildren(class_="info"):
                m = k.find(class_="artist")
                duration = k.find(class_="duration").text
                icon = i.findChildren(class_="cover")
                icon = icon[0]['style'][23:-3]
                if musician.strip().lower() in str(m.text).lower() :
                    l = k.find('a', href=True)
                    link = ("https://vrit.me" + l['href'])
                    req = requests.get(link)
                    filename = str('tracks/' + compose.replace(' ', '') + '.mp3')
                    with open(filename, 'wb') as f:
                        f.write(req.content)
                    flag = True
                    break

    if flag:
        return filename, duration, icon
    else:
        return None, None, None
