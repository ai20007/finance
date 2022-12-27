import time
import stock_list_jp
import stock_data_jp

def worker():
    df_stock_list = stock_list_jp.list_jp()
    length = len(df_stock_list)
    for i in range(length):
        code_num = df_stock_list["コード"][i]
        print(code_num)
        stock_data_jp.main(code_num)
        time.sleep(60)

if __name__ == "__main__":
    worker()
