# Prophet

In 2017, Facebook (now Meta) released its Prophet software as open source. This powerful tool was developed by Facebook engineers because its analysts were overwhelmed with the number of business forecasts demanded by managers. The developers of Prophet wanted to simultaneously solve two problems: 1 - completely automatic forecasting techniques are too brittle and inflexible to handle additional knowledge, and 2 - analysts who are consistently able to produce high-quality forecasts are rare and require extensive expertise. Prophet successfully solved both of these problems.

Prophet was designed so that forecasts produced with no parameter tuning or other optimizations are usually very high-quality. Nevertheless, with just a little bit of training, anyone can intuitively tweak the model and increase performance dramatically.

Prophet was designed to optimally handle business forecasting tasks, which typically feature any of these attributes:

- Time series data captured at the hourly, daily, or weekly level with ideally at least a full year of historical data
- Strong seasonality effects occurring daily, weekly, and/or yearly
- Holidays and other special one-time events that don’t necessarily follow the seasonality patterns but occur irregularly
- Missing data and outliers
- Significant trend changes that may occur with the launch of new features or products, for example
- Trends that asymptotically approach an upper or lower bound

Essentially, Prophet is an **additive regression model**. This means that the model is simply the sum of several (optional) components, such as the following:

- A linear or logistic growth trend curve
- An annual seasonality curve
- A weekly seasonality curve
- A daily seasonality curve
- Holidays and other special events
- Additional user-specified seasonality curves, such as hourly or quarterly, for example

