📊 A. Price Drivers and Correlation

    What is the pairwise correlation between price, market cap, volume_24h, and circulating_supply?

        Use .corr() and heatmaps to uncover strong relationships.

    Does higher trading volume associate with higher market capitalization?

        Explore if coins with active trading are also the most valuable.

    How do coins with high supply compare in price to coins with low supply?

        Plot circulating_supply vs. price, use binning.

    Are there visible outliers that violate typical supply-price expectations?

        Spot unusual coins (e.g., high price despite large supply).

📈 B. Temporal and Volatility Analysis

    What is the average price volatility for each coin over time?

        Group by name and compute standard deviation of price.

    Which coins have the most consistent (stable) vs. volatile price movements?

        Use box plots of prices grouped by coin name.

    How does average trading volume and market cap change over the day (hourly trend)?

        Extract hour from timestamp, analyze time-based cycles.

    Do price spikes cluster at certain times (e.g., UTC hours or day boundaries)?

        Time-series histogram of change_6hrs by hour.

    Are there trends in average 6-hour price change over time globally?

        Line plot of average change_6hrs over time.

💹 C. Supply and Market Dynamics

    How does market cap influence price volatility?

        Compare volatility across market cap quantiles.

    What is the typical price range for coins in different supply ranges?

        Bin circulating_supply and analyze price distribution within bins.

    Which coins have rapidly increasing or decreasing prices in short periods?

        Detect coins with largest 6hr changes (positive/negative extremes).

    Is there a lag between volume surge and price movement?

        Compare volume vs. change_6hrs with shifted time windows.

📊 D. Comparative Performance and Rankings

    Which top 10 coins consistently rank highest in price, market cap, or volume?

        Time-based ranking analysis.

    Which coins have the best average short-term performance (change_6hrs)?

        Compute average and median change_6hrs per coin.

    Are high-price coins always high market cap coins?

        Check alignment between price and market cap rankings.

    Which coins consistently appear in the top or bottom by price change?

        Percentile ranking over multiple scraping time points.

🧮 E. Distribution and Outlier Exploration

    What is the price distribution for all coins?

        Histogram or KDE of price.

    Are there many coins priced under $1 (micro coins)?

        Count and compare low-priced coins.

    Which coins behave as outliers in price vs. market cap or supply space?

        Scatter plots with outlier annotations.

    Do any coins consistently defy expectations (e.g., low volume but high price)?

        Conditional filtering and visual inspection.

✅ Bonus: Visual Ideas

    Heatmaps for correlation

    Scatter plots with regression lines

    Box plots for volatility per coin

    Line plots for time-based trends

    Bar charts for top N coins

    Histograms/KDE for distributions