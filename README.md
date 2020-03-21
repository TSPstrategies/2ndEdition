# TSP Investing Strategies, 2nd Edition

This repo provides the data, scripts, and sample graphics cited in _[TSP Investing Strategies: Building Wealth While Working for Uncle Sam, 2nd Edition](https://www.amazon.com/dp/B085R72HX3)_, and associated articles. 

### Data

I used the interest rate of the 10-year U.S. Government Bond, calculated monthly, as a proxy for the TSP's G Fund. This is saved in this repo as "10_yr_historical.csv". 

I referenced multiple data sets when building the composite index for U.S. stocks, that served as a proxy for the TSP's C Fund. For example, I referenced close prices and monthly returns for the S&P 500, available at https://finance.yahoo.com/quote/^GSPC?p=^GSPC. 

For month-end S&P composite prices from 1900 to 1927, I referenced Case-Shiller’s “U.S. Stock Markets 1871-Present and CAPE Ratio,” available at http://www.econ.yale.edu/~shiller/data.htm. I also referenced this dataset for early dividend rates by month. 

The combined S&P data is saved in this repo as "sp_comp_1900_2019.csv". 

The monthly contributions file lists contributions from $250 in the first 12 months (the first year), and the contributions increase by 5% each year to year 40. 

### Scripts

The main script comparing returns between the U.S. stock index (C Fund) and the U.S. 10-year (G Fund) is titled "historical_returns.py". I attempted to comment all of the steps I took in the script to conduct the analyses. 

See the interactive returns calculator at https://thrifty.ninja to test the scripts and underlying data with additional variables such as fees. 

The 20- and 30-year periods from 1988 onward match very closely with real-world monthly TSP return data. Compare the returns with those in the beta TSP returns calculator available at https://returns.tspstrategies.com. To compare returns, set the variables to $30,000 starting salary, 5% contribution rate, and either 20 or 30 years, and match the C and G Fund data with those in the 20- and 30-year calculated data from the 10-year and S&P datasets. 

The results can also be compared dynamically between returns calculators when using the same inputs, such as the same start and end year, the same salary, contributions, etc., from 1988 to 2019. 

### Sample Graphics

Sample graphics from the 2nd edition are in the Book_Graphics folder.

Additional graphics for reference are kept in Additional_Graphics folder. 
