def filter_trades(trades, sql_database):
    sql_list = list(sql_database.instrument_symbol)
    filtered_trades = trades[trades['Ticker'].isin(sql_list)].rename({'Ticker':'instrument_symbol'}, axis=1)
    
    res = sql_database.merge(right=filtered_trades, how='inner', on='instrument_symbol')
    return res
