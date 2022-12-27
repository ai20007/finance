import os
import time
import pandas_datareader.data as web
import pandas as pd


# 銘柄DF化
def list_jp():
    stock_list_df = pd.read_excel("./data_j.xls")
    return stock_list_df


# データ保存
def data_jp(ticker_symbol):
    start = '2012-01-01'  # 開始日
    end = '2021-12-31'  # 終了日
    ticker_symbol_dr = str(ticker_symbol) + ".JP"  # 銘柄コード
    df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start, end=end)  # データ取得
    df.to_csv(os.path.dirname(__file__) + '\s' + str(ticker_symbol) + '_jp.csv')  # csv保存


# スクレイピング
def main(wait_time):
    stock_list = list_jp()
    length = len(stock_list)
    # DFをndarrayに変換して高速化
    stock_list_code = stock_list["コード"].values
    # プライム/スタンダード/グロースの3つに該当する物のみ抽出
    stock_list_group = stock_list["市場・商品区分"].values
    for i in range(length):
        if stock_list_group[i] == ("プライム（内国株式）" or "スタンダード（内国株式）" or "グロース（内国株式）"):
            code_num = stock_list_code[i]
            data_jp(code_num)
            time.sleep(wait_time)


# プログラムを自動で走らせる間隔(秒)を設定
if __name__ == "__main__":
    main(300)
