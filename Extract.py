import sqlite3
import pandas as pd
import numpy as np
from finvizfinance.insider import Insider
from datetime import datetime
from datetime import timedelta

def create_sql_if_not_exists():    
    conn = sqlite3.connect('stock_database')
    c = conn.cursor()

    c.execute('''
              CREATE TABLE IF NOT EXISTS stocks
              ([instrument_cik] INTEGER PRIMARY KEY, [instrument_symbol] TEXT, [current_price] INTEGER, 
               [shares_owned] INTEGER, [market_value] INTEGER)
              ''')

    AAPL = (320193,'AAPL',150, 500, 150*500)
    BTU = (1067242,'BTU',200, 1000, 200*1000)
    WMT = (104169,'WMT',150, 750, 150*750)
    MSFT = (789019,'MSFT',250, 100, 250*100)
    LLY = (59478,'LLY',375, 250, 375*250)

    c.execute(f'''
              INSERT or REPLACE INTO stocks (instrument_cik, instrument_symbol, current_price, shares_owned, market_value)

                    VALUES
                    {AAPL},
                    {BTU},
                    {WMT},
                    {MSFT},
                    {LLY}
              ''')                     

    conn.commit()

    sql_query = pd.read_sql_query('''
                                  SELECT * FROM stocks
                                  ''', conn)

    df = pd.DataFrame(sql_query, columns=['instrument_cik', 'instrument_symbol', 'current_price', 'shares_owned', 'market_value'])
    return df

def insider_trades():
    finsider = Insider(option='top owner trade')
    insiders = finsider.get_insider()
    
    yesterday = datetime.today() - timedelta(days=1)
    res = datetime.strftime(yesterday, '%b %d')
    
    recent_trades = insiders[(insiders.Date == res)]
    return recent_trades
