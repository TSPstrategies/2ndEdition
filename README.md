# TSP Investing Strategies, 2nd Edition

This repo provides the scripts, data, and sample graphics cited in 'TSP Investing Strategies: Building Wealth While Working for Uncle Sam", 2nd Edition, and associated articles. 

### Data

I used the interest rate of the 10-year U.S. Government Bond, calculated monthly, as a proxy for the TSP's G Fund. This is saved in this repo as "10_yr_historical.csv". 

I referenced multiple data sets when building the composite index for U.S. stocks, that served as a proxy for the TSP's C Fund. For example, I referenced close prices and monthly returns for the S&P 500, available at https://finance.yahoo.com/quote/^GSPC?p=^GSPC. 

For month-end SP composite prices from 1900 to 1927, I referenced Case-Shiller’s “U.S. Stock Markets 1871-Present and CAPE Ratio,” available at http://www.econ.yale.edu/~shiller/data.htm. I also referenced this dataset for early dividend rates by month. 

The SP data is saved in this repo as "sp_comp_1900_2019.csv". 

### Scripts

The main script comparing returns between the U.S. stock index (C Fund) and the U.S. 10-year (G Fund) is titled "historical_returns.py". I attempted to comment all of the steps I took in the script to conduct the analyses. 

### Sample Graphics

Sample graphics from the 2nd edition are in the Book_Graphics folder.

Additional graphics for reference are kept in Additional_Graphics folder. 
