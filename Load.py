def to_sql(res):
    
    conn = sqlite3.connect('stock_database')
    c = conn.cursor()
    
    if len(res) == 0:
        print('No trades for any of the instruments provided. ')
    else:
        res.to_sql('stocks', conn, if_exists='replace', index=False)
        
        print((res.instrument_symbol).unique())
