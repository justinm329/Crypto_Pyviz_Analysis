# Import libraries and dependencies
import pandas as pd
import hvplot.pandas

import yfinance as yf

import seaborn as sns
import panel as pn
import matplotlib.pyplot as plt
%matplotlib inline

# Donwload data from yfinance
crypto_df = yf.download(tickers = "BTC-USD ETH-USD DOGE-USD ADA-USD", start = "2021-09-01", end = "2021-10-01")

# Slice for "Adj Close" column only
close_df = crypto_df["Adj Close"]

# Visualize top rows
close_df.head()

# Get daily returns, drop null values
daily_returns = close_df.pct_change().dropna()*100

# Visualize top rows
daily_returns.head()

# Get average daily returns
average_returns = daily_returns.mean()*100
average_returns

# Create bar chart
return_bar = average_returns.hvplot.bar(
               xlabel = "Crypto Tickers", 
               ylabel = "Average Percentage Change", 
               title = "Cryptocurriences Average Percentage Change on September 2021")

# Create line chart
return_line = daily_returns.hvplot.line(
               xlabel = "Date", 
               ylabel = "Percentage Change", 
               title = "Cryptocurriences Daily Returns",
               legend = "right")

# Create correlation heatmap
def correlation_plot():
    correlation_fig = plt.figure()
    correlation = sns.heatmap(daily_returns.corr()).set_title("Correlation Heatmap")
    plt.close(correlation_fig)
    return pn.pane.Matplotlib(correlation_fig, tight=True)

# Build dashboard
dashboard = pn.Column(
    "#Cryptocurrencies Analysis Dashboard",
    return_bar,
    "The bar chart above displays the average percentage change for each of the analyzed cryptocurrencies. The higher the percentage change the better for the investor, since he/she would have a better return on his/her investment.",
    "Acording to the bar chart, Bitcoin (BTC-USD) represnts the best option for investors interested in cryptocurrencies.",
    return_line,    
    "The line chart above visualizes the daily returns for the analyzed cryptocurrencies. This helps investors understand the cryptocurrencies volatility over time and in respect with one another.",
    "According to the line chart, it can be assumed that these four cryptocurrencies follow a similar trend across time.",
     correlation_plot(),
    "The correlation heatmap above helps understanding the dependency between the four analyzed cryptocurrencies.",
    "According to the correlation plot, all four cryptocurrencies have strong positive correlation between each other, which means that if the value of one cryptocurrency increases, it is expected that the value of the other ones will increase as well.",
    "*---*",
    "***Dashboard Created by: Justin Farnan***")

# Visualize dashboard
dashboard