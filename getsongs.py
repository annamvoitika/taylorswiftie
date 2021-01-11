# -*- coding: utf-8 -*-

import os
import requests
import bs4
import pandas as pd

PATH = os.path.join("/", "Users", "YOUR USERNAME", "YOUR FOLDER")


def table_to_df(table):
           return pd.DataFrame([[th.text for th in row.findAll('th')] for row in table.tbody.findAll('tr')])

res = pd.DataFrame()
url = 'https://en.wikipedia.org/wiki/List_of_songs_recorded_by_Taylor_Swift'

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
table = soup.find(name='table', attrs={'class':'plainrowheaders'})
res = res.append(table_to_df(table))
res.to_csv(os.path.join(os.path.join(PATH, "table.csv")),
           index=None, sep=';', encoding='cp1252')
