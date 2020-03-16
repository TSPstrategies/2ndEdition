import pandas as pd
import numpy as np


# read in the years file 

years = pd.read_csv("years.csv", header=None)
years = years.loc[0:, 0]


# read in the contributions file

monthly_contributions = pd.read_csv("monthly_contributions.csv", header=None)
monthly_contributions = monthly_contributions.loc[0:, 0]

# read in the U.S. 10-year gov't bond returns data 

tenyear_file = "10_yr_historical.csv"
tenyear = pd.read_csv(tenyear_file)

# convert the annual 10-year interest rate to a monthly rate, and add '1'

ty = tenyear['interest_rate']
ty = ((ty / 12) * .01) + 1
tenyear['monthly_interest'] = ty
# tenyear = tenyear.fillna(1)

#read in the SP stock index data
sp_file = "sp_comp_1900_2019.csv"
sp = pd.read_csv(sp_file)

# fill in the "NaN" dividend column with 0 
sp.fillna({'dividend':0})

# calculate the month-over-month change in the SP index and convert the dividend rate to a monthly (or quarterly/annual, depending on the type of calculation you are conducting)

sp_pct = sp['sp_composite_price']
sp_pct = sp_pct.pct_change()
sp['change'] = sp_pct + 1
sp = sp.fillna(1)
sp['adj_divs'] = sp['dividend'] / 12

# transition 'date' to datetime dtype
sp['date'] = pd.to_datetime(sp['date'])
tenyear['date'] = pd.to_datetime(tenyear['date'])

sp_indexed = sp.set_index('date')
tenyear_indexed = tenyear.set_index('date')


# iterate X number of year periods (see X) of the SP index AND gov't bonds from 1900, with increasing contributions and with 
# dividends reinvested, at 65-35

sp500_govtbonds_allYears_increasingContr_Divs = pd.DataFrame()

for year in years:
    total_return = []
    future_year = year + 34  # X
    x = 0
    rolling_total_sp = 0
    rolling_total_gov = 0
    rolling_total = 0
    dividends = 0
    df_sp = sp_indexed.loc[lambda x : x.index.year >= year]
    df_sp = df_sp.loc[lambda x: x.index.year <= future_year]
    df_gov = tenyear_indexed.loc[lambda x : x.index.year >= year]
    df_gov = df_gov.loc[lambda x: x.index.year <= future_year]
    
#     number  = len(increasing_contributions)
    contributions = monthly_contributions[0:420]  # for 35 years of contribitions; for 30 years of contributions, change to [0:360]
    total_dividends = []
    for contribution in contributions:

        sp_contribution = contribution * .65 # adjust as necessary; change to 1 for all-stock, or 0 for no stock portfolio
        gov_contribution = contribution * .35 # adjust as necessary; change to 0 for no bonds, or 1 for all bond portfolio 
        rolling_total_sp = ((sp_contribution + rolling_total_sp) * df_sp.iloc[x, 2]) + dividends
        dividends = (rolling_total_sp / df_sp.iloc[x, 0]) * df_sp.iloc[x, 3] 

        rolling_total_gov = (gov_contribution + rolling_total_gov) * df_gov.iloc[x, 1]

        rolling_total = rolling_total_sp + rolling_total_gov
        total_return.append(rolling_total.round(decimals=2))

        
# to rebalance annually: 
        # if x % 12 == 0:
        #     rolling_total_sp = rolling_total * .65
        #     rolling_total_gov = rolling_total * .35
        # else:
        #     pass
        
        x += 1
    conts_sum = pd.Series(contributions)

    print(f"The total returns from investing ${conts_sum.sum()} from {year} is ${rolling_total.round(decimals=2)}")
    
# save results to csv for each run 
    sp500_govtbonds_allYears_increasingContr_Divs[year] = total_return
    # sp500_govtbonds_allYears_increasingContr_Divs.to_csv(f"sp500_govtbonds_100GFund_allYears_increasingContr_Divs_35yrs.csv")
    # sp500_govtbonds_allYears_increasingContr_Divs.to_csv(f"sp500_govtbonds_100CFund_allYears_increasingContr_Divs_35yrs.csv")
    sp500_govtbonds_allYears_increasingContr_Divs.to_csv(f"sp500_govtbonds_6535_allYears_increasingContr_Divs_35yrs.csv")
    # sp500_govtbonds_allYears_increasingContr_Divs.to_csv(f"sp500_govtbonds_6535_allYears_increasingContr_Divs_35yrs_Rebalance.csv")


