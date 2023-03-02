from bs4 import BeautifulSoup
from get_daily_price import *
from get_info import get_information
from edit_and_predict import *


def get_data_frame(url):
    soup = BeautifulSoup(url, 'html.parser')
    card_name = list()
    card_id = list()
    rarity = list()
    prices = list()
    link_to_card = list()
    day_1 = list()
    day_2 = list()
    day_3 = list()
    day_4 = list()
    day_5 = list()
    day_6 = list()
    day_7 = list()
    day_8 = list()

    new_url = soup.find('select', attrs={'name': 'set'})
    for option in new_url.findAll('option'):
        add = option["value"]
        card_name, card_id, rarity, link_to_card, prices = get_information(
            getHTMLdocument(f"https://shop.tcgplayer.com/price-guide/yugioh/" + add), card_name, card_id, rarity,
            link_to_card, prices)

        if len(card_id) > 4000:
            break

    day_8, day_7, day_6, day_5, day_4, day_3, day_2, day_1 = fill_list(card_name, day_8, day_7, day_6,
                                                                                       day_5, day_4, day_3, day_2,
                                                                                       day_1)

    day_8, day_7, day_6, day_5, day_4, day_3, day_2, day_1 = get_daily_price(link_to_card, day_8,
                                                                             day_7, day_6, day_5, day_4,
                                                                             day_3, day_2, day_1)
    data = pd.DataFrame(
        {"card_name": card_name, "card_id": card_id, "rarity": rarity, "link": link_to_card, "price": prices,
         "day 1": day_1, "day 2": day_2, "day 3": day_3, "day 4": day_4, "day 5": day_5, "day 6": day_6,
         "day 7": day_7, "day 8": day_8})

    data = edit_df(data)

    day_9 = predict_day_9(data)
    data['day 9'] = day_9
    return data

