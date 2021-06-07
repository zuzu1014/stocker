import FinanceDataReader as fdr
import ast
from datetime import datetime, date, timedelta




class Strategy:

    def __init__(self):
        with open("./data/origin/stock_data.json", 'r') as f:
            stock_data = ast.literal_eval(f.readline())
        
        self.stock_data = stock_data
        self.today = date.today().isoformat()
        self.last_month = date.today() - timedelta(days=30)
        self.last_year = date.today() - timedelta(days=365)


    def get_price_data(self, code, start_date, end_date):

        df = fdr.DataReader(code, start_date, end_date)

        price = {}
        price['52_low'] = df['Close'].min()
        price['52_high'] = df['Close'].max()
        price['average'] = df['Close'].mean()

        print(price)

        return price



    def test(self):
        df = fdr.DataReader('068270', self.last_month, self.today)
        print(df)

a = Strategy()
a.test()
a.get_52_data('068270')