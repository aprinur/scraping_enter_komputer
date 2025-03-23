from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from src.models import Items
import pandas as pd
import datetime
import time
import os


def get_html(url):
    try:
        proxy = ''
        chrome_option = Options()
        chrome_option.add_argument(f'--proxy-server={proxy}')
        driver = webdriver.Chrome(options=chrome_option)
        driver.get(url)
        return driver.page_source
    except Exception as e:
        print(f'error on get_html: {e}')


def save_to_file(item: list[Items], filename):
    save_dir = os.path.join(os.path.expanduser('~'), 'Download')
    date = datetime.datetime.now().strftime('%d_%B_%Y')

    excel_dir = os.path.join(save_dir, f'{filename}_{date}.xlsx')
    csv_dir = os.path.join(save_dir, f'{filename}_{date}.csv')

    items_dicts = [i.__dict__ for i in item]
    df = pd.DataFrame(items_dicts)
    df.to_excel(excel_dir, index=False)
    df.to_csv(csv_dir, index=False)
