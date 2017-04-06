import datetime as dt
import random
from time import sleep

from selenium import webdriver


def populate_survey(page_info):
    driver = webdriver.Chrome()
    driver.get(page_info['website'])

    for page in page_info['pages']:
        if 'currency_range_text' in page:
            for currency_range in page['currency_range_text']:
                value = random.uniform(currency_range['min'], currency_range['max'])
                currency_input = driver.find_element_by_id(currency_range['id'])
                currency_input.send_keys('{:.2f}'.format(value))
        if 'date_text' in page:
            for date_text in page['date_text']:
                the_date = dt.datetime.now() - dt.timedelta(days=date_text['days_ago'])
                date_input = driver.find_element_by_id(date_text['id'])
                date_input.send_keys(the_date.strftime('%m/%d/%Y'))
        if 'int_range_text' in page:
            for int_text in page['int_range_text']:
                value = random.randint(int_text['min'], int_text['max'])
                int_input = driver.find_element_by_id(int_text['id'])
                int_input.send_keys('{:.2f}'.format(value))
        if 'string_text' in page:
            for string_text in page['string_text']:
                string_input = driver.find_element_by_id(string_text['id'])
                string_input.send_keys(string_text['key'])
        if 'radio' in page:
            for radio in page['radio']:
                radio_input = driver.find_element_by_id(radio)
                driver.execute_script('arguments[0].click();', radio_input)

        if 'continue' in page:
            driver.find_element_by_id(page['continue']).click()
            sleep(2)
        else:
            driver.find_element_by_id(page_info['continue']).click()
            sleep(2)

    sleep(20)


