import yfinance
import pandas

# API Notes:
# 

def get_stock_data(ticker: str, start: str, end: str,) -> pandas.DataFrame:
    return yfinance.download(ticker, start=start, end=end, group_by="ticker")

# Testing
test = get_stock_data('AAPL MSFT', '2020-01-01', '2020-01-10')
print(test)