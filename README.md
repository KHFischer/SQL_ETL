# SQL_ETL

## ETL pipeline:
## Extract database containing investment portfolio from SQL.
## Extract insider trading data from day before rundate. 

## Transform if there are insider trades in the instruments in the portfolio the SEC EDGAR data is added to the dataframe. 

## Load the data with insider trades back to SQL and log the instrumens with insider trades to the console. If there are no insider trades the original database is kept unchanged.
