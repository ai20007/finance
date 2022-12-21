import os
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime as dt

def main(ticker_symbol):
    start = '2012-01-01' # 開始日
    end = '2021-12-31' # 終了日
    ticker_symbol_dr = str(ticker_symbol) + ".JP" # 銘柄コード
    df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start, end=end) # データ取得
    df.to_csv(os.path.dirname(__file__) + '\s_stock_data_' + str(ticker_symbol) + '.csv') # csv保存
