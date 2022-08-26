from tokenize import Number
import numpy as np
import pandas as pd

def main():
    sales_dataframe = pd.read_csv('sales_stats.csv')
    sales_dataframe[['entry_date','sold_date']] = sales_dataframe[['entry_date','sold_date']].apply(pd.to_datetime)
    sales_dataframe['days_inv'] = (sales_dataframe['sold_date'] - sales_dataframe['entry_date']) / np.timedelta64(1, 'D')
    print(sales_dataframe)
    sum_df = sales_dataframe.groupby(['product_id']).agg(
     sum_sale_price = ('sale_price','sum'),
     sum_cost = ('cost','sum'),
     sum_days_in_inv = ('days_inv', 'sum')
     ).reset_index()
    sum_df['profit_per_day'] = (sum_df['sum_sale_price'] - sum_df['sum_cost']) / sum_df['sum_days_in_inv']
    print(sum_df)
    number_of_products_to_buy = input("Enter how many products you wish to buy...")
    products_to_buy_df = sum_df.nlargest(n=int(number_of_products_to_buy), columns=['profit_per_day', 'product_id'])
    print('Top ', number_of_products_to_buy, ' products to buy:')
    print(products_to_buy_df)

if __name__ == "__main__":
    main()

