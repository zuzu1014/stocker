import FinanceDataReader as fdr
import json
import ast
import ast
from datetime import datetime, date, timedelta


def process_data(target):

    f = open("./data/origin/" + target + ".txt", 'r', encoding='UTF8')
    data = str(f.readlines()).replace("\\n", "")
    processed_data = ast.literal_eval(data)
    f.close()

    return processed_data


def fetch_data():
    pass


def load_data():
    global code_data
    global name_data
    global sector_data
    
    code_data = process_data("code")
    name_data = process_data("name")
    sector_data = process_data("sector")


def append_price_data(codes):

    today = date.today()
    last_year = today - timedelta(days=365)

    price_52_low = []
    price_52_high = []
    price_52_average = []

    for code in codes:
        df = fdr.DataReader(code, last_year, today)
        price_52_low.append(int(df['Close'].min()))
    
    print(price_52_low)

    




def merge_data():
    load_data()

    assert len(code_data) == len(name_data) == len(sector_data)

    stock_data = {}
    for i in range(len(code_data)):
        new_stock_data = {}
        new_stock_data['name'] = name_data[i]
        new_stock_data['sector'] = sector_data[i]

        stock_data[code_data[i]] = new_stock_data


    stock_data = json.dumps(stock_data, ensure_ascii=False, indent=4)
    print(stock_data)
    with open("./data/origin/stock_data.json", 'w', encoding='UTF8') as f:
        f.write(stock_data)
    #print(stock_data)


# fetch -> merger







merge_data()

#append_price_data(process_data("code"))

