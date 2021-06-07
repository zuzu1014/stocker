import ast
import json
from datetime import datetime, date, timedelta

import FinanceDataReader as fdr
from utils.Tracker import *


def fetch_data():
    pass



def process_data(target):
    with open("./data/origin/" + target + ".txt", 'r', encoding='UTF8') as f:
        data = str(f.readlines()).replace("\\n", "")
        processed_data = ast.literal_eval(data)
   
    return processed_data



def load_data():
    
    global code_data
    global name_data
    global sector_data
    
    code_data = process_data("code")
    name_data = process_data("name")
    sector_data = process_data("sector")



def append_basic_data():
    global stock_data
    assert len(code_data) == len(name_data) == len(sector_data)

    stock_data = {}
    for i in range(len(code_data)):
        basic_data = {}
        basic_data['name'] = name_data[i]
        basic_data['sector'] = sector_data[i]

        stock_data[code_data[i]] = basic_data
        


def append_price_data():
    
    global stock_data
    
    today = date.today()
    last_year = today - timedelta(days=365)
    for code in code_data:
        df = fdr.DataReader(code, last_year, today)
        
        price_data = {}
        
        price_data['52_low'] = int(df['Close'].min())
        price_data['52_high'] = int(df['Close'].max())
        price_data['52_avg'] = int(df['Close'].mean())
        
        stock_data[code]['price'] = price_data



def save_data():
    
    global stock_data
    
    stock_data = json.dumps(stock_data, ensure_ascii=False, indent=4)
    with open("./data/origin/stock_data.json", 'w', encoding='UTF8') as f:
        f.write(stock_data)
        

def init_data():

    with Tracker() as T:
        T.append_tasks(load_data, append_basic_data, append_price_data, save_data)
        T.start()

