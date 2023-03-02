import time
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from dates import *


def getHTMLdocument(url):
    response = requests.get(url)

    return response.text


def get_daily_price(url_list, day_8, day_7, day_6, day_5, day_4, day_3, day_2, day_1):
    count = 0
    Path = "C:\Program Files (x86)\chromedriver.exe"
    ser = Service(Path)
    driver = webdriver.Chrome(service=ser)

    for url in url_list:
        try:
            if count % 200 == 0:
                time.sleep(10)
            driver.get(url)

            if WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal__activator'))):
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'modal__activator'))).click()

                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'is-modal')))
                get_s = driver.find_element(By.CSS_SELECTOR,
                                            '#app > div > div > section.marketplace__content > section > div > div.product-details__product > section.product-details__price-guide > div > h3 > div > div.modal__overlay.modal__normal.modal__overlay-fullscreen > div > div > section.modal__content.modal__content__scrollable > section > section.latest-sales.sales-history-snapshot__latest-sales > ul')
                all_sales = get_s.find_elements(By.TAG_NAME, 'li')
                d = all_sales[-1]
                dates = d.find_element(By.CLASS_NAME, 'date').text
                ''' check if we got to the point that we need'''
                while times_equal(dates) <= 8:
                    try:
                        WebDriverWait(driver, 2).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, 'sales-history-snapshot__load-more'))).click()
                        all_sales = get_s.find_elements(By.TAG_NAME, 'li')
                        d = all_sales[-1]
                        dates = d.find_element(By.CLASS_NAME, 'date').text

                    except:
                        break

                price_day_1 = 0
                price_day_2 = 0
                price_day_3 = 0
                price_day_4 = 0
                price_day_5 = 0
                price_day_6 = 0
                price_day_7 = 0
                price_day_8 = 0

                count_sales_1 = 0
                count_sales_2 = 0
                count_sales_3 = 0
                count_sales_4 = 0
                count_sales_5 = 0
                count_sales_6 = 0
                count_sales_7 = 0
                count_sales_8 = 0
                for sale in all_sales:
                    date = sale.find_element(By.CLASS_NAME, 'date').text
                    if date == '':
                        continue
                    else:
                        price = sale.find_element(By.CLASS_NAME, 'price').text
                        price = price.replace(" ", "")
                        price = price.replace("$", "")
                        price = price.replace("\n", "")
                        price = price.replace(",", "")
                        keep = times_equal(date)
                        if keep == 0:
                            price_day_8 = price_day_8 + float(price)
                            count_sales_8 = count_sales_8 + 1
                        elif keep == 1:
                            price_day_7 = price_day_7 + float(price)
                            count_sales_7 = count_sales_7 + 1
                        elif keep == 2:
                            price_day_6 = price_day_6 + float(price)
                            count_sales_6 = count_sales_6 + 1
                        elif keep == 3:
                            price_day_5 = price_day_5 + float(price)
                            count_sales_5 = count_sales_5 + 1
                        elif keep == 4:
                            price_day_4 = price_day_4 + float(price)
                            count_sales_4 = count_sales_4 + 1
                        elif keep == 5:
                            price_day_3 = price_day_3 + float(price)
                            count_sales_3 = count_sales_3 + 1
                        elif keep == 6:
                            price_day_2 = price_day_2 + float(price)
                            count_sales_2 = count_sales_2 + 1
                        elif keep == 7:
                            price_day_1 = price_day_1 + float(price)
                            count_sales_1 = count_sales_1 + 1

                if price_day_7 == 0:
                    price_day_7 = price_day_8
                    count_sales_7 = count_sales_8
                if price_day_6 == 0:
                    price_day_6 = price_day_7
                    count_sales_6 = count_sales_7
                if price_day_5 == 0:
                    price_day_5 = price_day_6
                    count_sales_5 = count_sales_6
                if price_day_4 == 0:
                    price_day_4 = price_day_5
                    count_sales_4 = count_sales_5
                if price_day_3 == 0:
                    price_day_3 = price_day_4
                    count_sales_3 = count_sales_4
                if price_day_2 == 0:
                    price_day_2 = price_day_3
                    count_sales_2 = count_sales_3
                if price_day_1 == 0:
                    price_day_1 = price_day_2
                    count_sales_1 = count_sales_2

                if price_day_2 == 0:
                    price_day_2 = price_day_1
                    count_sales_2 = count_sales_1
                if price_day_3 == 0:
                    price_day_3 = price_day_2
                    count_sales_3 = count_sales_2
                if price_day_4 == 0:
                    price_day_4 = price_day_3
                    count_sales_4 = count_sales_3
                if price_day_5 == 0:
                    price_day_5 = price_day_4
                    count_sales_5 = count_sales_4
                if price_day_6 == 0:
                    price_day_6 = price_day_5
                    count_sales_6 = count_sales_5
                if price_day_7 == 0:
                    price_day_7 = price_day_6
                    count_sales_7 = count_sales_6
                if price_day_8 == 0:
                    price_day_8 = price_day_7
                    count_sales_8 = count_sales_7

                if count_sales_8 >= 1:
                    day_8[count] = "{:.2f}".format((price_day_8 / count_sales_8)) + "$"
                if count_sales_7 >= 1:
                    day_7[count] = "{:.2f}".format((price_day_7 / count_sales_7)) + "$"
                if count_sales_6 >= 1:
                    day_6[count] = "{:.2f}".format((price_day_6 / count_sales_6)) + "$"
                if count_sales_5 >= 1:
                    day_5[count] = "{:.2f}".format((price_day_5 / count_sales_5)) + "$"
                if count_sales_4 >= 1:
                    day_4[count] = "{:.2f}".format((price_day_4 / count_sales_4)) + "$"
                if count_sales_3 >= 1:
                    day_3[count] = "{:.2f}".format((price_day_3 / count_sales_3)) + "$"
                if count_sales_2 >= 1:
                    day_2[count] = "{:.2f}".format((price_day_2 / count_sales_2)) + "$"
                if count_sales_1 >= 1:
                    day_1[count] = "{:.2f}".format((price_day_1 / count_sales_1)) + "$"

            count += 1
        except:
            count += 1

    return day_8, day_7, day_6, day_5, day_4, day_3, day_2, day_1


def fill_list(card_name, day_8, day_7, day_6, day_5, day_4, day_3, day_2, day_1):
    for card in card_name:
        day_1.append("0")
        day_2.append("0")
        day_3.append("0")
        day_4.append("0")
        day_5.append("0")
        day_6.append("0")
        day_7.append("0")
        day_8.append("0")
    return day_8, day_7, day_6, day_5, day_4, day_3, day_2, day_1
