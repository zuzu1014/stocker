import FinanceDataReader as fdr

# 삼성전자(005930) 전체 (1996-11-05 ~ 현재)
df = fdr.DataReader('005930')

# Apple(AAPL), 2017-01-01 ~ Now

print(df)