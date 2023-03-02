from bs4 import BeautifulSoup


'''crawling'''


def get_information(url, card_name, card_id, rarity, link_to_card, prices):
    soup = BeautifulSoup(url, 'html.parser')
    for i in soup.findAll('tr', attrs={'class': 'odd'}):

        find_p = i.find('td', attrs={'class': 'marketPrice'})
        price = find_p.find('div').string
        if price.find("$") == -1:
            return card_name, card_id, rarity, link_to_card, prices
        price = price.replace(" ", "")
        prices.append(price)
        card = i.find('div', attrs={'class': 'productDetail'})
        card_name.append(card.find('a').string)

        id_tag = i.find('td', attrs={'class': 'number'})
        id = id_tag.find('div').string
        id = id.replace(" ", "")
        id = id.replace("\n", "")
        card_id.append(id)

        btn = i.find("button", {'class': "catalogGreenButton"})
        onclick = btn["onclick"]
        href = onclick.split("=")[1]
        href = href.replace("'", "")
        href = href.replace(";", "")
        link_to_card.append(href)

        find_r = i.find('td', attrs={'class': 'rarity'})
        rare = find_r.find('div').string
        rare = rare.replace(" ", "")
        rarity.append(rare)
    for i in soup.findAll('tr', attrs={'class': 'even'}):

        find_p = i.find('td', attrs={'class': 'marketPrice'})
        price = find_p.find('div').string

        if price.find("$") == -1:
            return card_name, card_id, rarity, link_to_card, prices
        price = price.replace(" ", "")
        prices.append(price)
        card = i.find('div', attrs={'class': 'productDetail'})
        card_name.append(card.find('a').string)

        id_tag = i.find('td', attrs={'class': 'number'})
        id = id_tag.find('div').string
        id = id.replace(" ", "")
        id = id.replace("\n", "")
        card_id.append(id)

        btn = i.find("button", {'class': "catalogGreenButton"})
        onclick = btn["onclick"]
        href = onclick.split("=")[1]
        href = href.replace("'", "")
        href = href.replace(";", "")
        link_to_card.append(href)
        
        find_r = i.find('td', attrs={'class': 'rarity'})
        rare = find_r.find('div').string
        rare = rare.replace(" ", "")
        rarity.append(rare)
    return card_name, card_id, rarity, link_to_card, prices
