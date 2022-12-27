import pandas as pd

# 東証HPからDLしてきた銘柄コード一覧をdf化
def list_jp():
    stock_list = pd.read_excel("./data_j.xls")
    return stock_list
# print(df_data_j)

if __name__ == "__main__":
    list_jp()
