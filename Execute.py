from Extract import *
from Transform import *
from Load import *

if __name__ == '__main__':
    
    # Extract
    print('Extracting \n')
    sql_df = create_sql_if_not_exists()
    trades_df = insider_trades()
    
    # Transform
    print('Transforming \n')
    transformed_df = filter_trades(trades_df, sql_df)
        
    # Load
    print('Loading \n')
    print('Trades for:')
    to_sql(transformed_df)
    print('\nProcess finished. Check full database for more information')
